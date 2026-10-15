import os
import sqlite3
import logging
from datetime import datetime, time

import pytz
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from workouts import HOME_WORKOUTS, GYM_WORKOUTS

# ------------------ Configuration ------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
TIMEZONE_NAME = os.environ.get("TIMEZONE", "UTC")
SEND_HOUR = int(os.environ.get("SEND_HOUR", "7"))
SEND_MINUTE = int(os.environ.get("SEND_MINUTE", "0"))
DB_PATH = os.environ.get("DB_PATH", "subscribers.db")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set!")

TIMEZONE = pytz.timezone(TIMEZONE_NAME)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


# ------------------ Database ------------------
def init_db() -> None:
    con = sqlite3.connect(DB_PATH)
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS subscribers (
            chat_id INTEGER PRIMARY KEY,
            preference TEXT NOT NULL DEFAULT 'home'
        )
        """
    )
    con.commit()
    con.close()


def add_subscriber(chat_id: int) -> None:
    con = sqlite3.connect(DB_PATH)
    con.execute("INSERT OR IGNORE INTO subscribers (chat_id) VALUES (?)", (chat_id,))
    con.commit()
    con.close()


def remove_subscriber(chat_id: int) -> None:
    con = sqlite3.connect(DB_PATH)
    con.execute("DELETE FROM subscribers WHERE chat_id = ?", (chat_id,))
    con.commit()
    con.close()


def set_preference(chat_id: int, pref: str) -> None:
    con = sqlite3.connect(DB_PATH)
    con.execute("INSERT OR IGNORE INTO subscribers (chat_id) VALUES (?)", (chat_id,))
    con.execute(
        "UPDATE subscribers SET preference = ? WHERE chat_id = ?", (pref, chat_id)
    )
    con.commit()
    con.close()


def get_all_subscribers() -> list[tuple[int, str]]:
    con = sqlite3.connect(DB_PATH)
    rows = con.execute("SELECT chat_id, preference FROM subscribers").fetchall()
    con.close()
    return rows


# ------------------ Helpers ------------------
def today_key() -> str:
    return datetime.now(TIMEZONE).strftime("%A").lower()


def format_workout(day: str, preference: str) -> str:
    source = GYM_WORKOUTS if preference == "gym" else HOME_WORKOUTS
    workout = source.get(day)
    if not workout:
        return "Rest day! Enjoy your recovery. 🧘"

    lines = [f"*{workout['title']}*", "", workout["description"], ""]
    for i, exercise in enumerate(workout["exercises"], 1):
        lines.append(f"{i}. {exercise}")
    lines.append("")
    lines.append("Have a great workout! 💪")
    return "\n".join(lines)


# ------------------ Command Handlers ------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    add_subscriber(chat_id)
    text = (
        "👋 *Welcome to your Daily Workout Bot!*\n\n"
        "Every morning I'll send you one beginner-friendly routine.\n\n"
        "*Commands:*\n"
        "/today — today's workout\n"
        "/home — switch to home workouts 🏠\n"
        "/gym — switch to gym workouts 🏋️\n"
        "/stop — unsubscribe\n"
        "/help — show this help"
    )
    await update.message.reply_markdown(text)


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start(update, context)


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    remove_subscriber(update.effective_chat.id)
    await update.message.reply_text(
        "You've been unsubscribed. Send /start anytime to resume."
    )


async def today(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    con = sqlite3.connect(DB_PATH)
    row = con.execute(
        "SELECT preference FROM subscribers WHERE chat_id = ?", (chat_id,)
    ).fetchone()
    con.close()
    pref = row[0] if row else "home"
    text = format_workout(today_key(), pref)
    await update.message.reply_markdown(text)


async def set_home(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    set_preference(update.effective_chat.id, "home")
    await update.message.reply_text(
        "✅ You're now set to 🏠 *Home* workouts.", parse_mode="Markdown"
    )


async def set_gym(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    set_preference(update.effective_chat.id, "gym")
    await update.message.reply_text(
        "✅ You're now set to 🏋️ *Gym* workouts.", parse_mode="Markdown"
    )


# ------------------ Daily Job ------------------
async def send_daily_workout(context: ContextTypes.DEFAULT_TYPE) -> None:
    day = today_key()
    subscribers = get_all_subscribers()
    logger.info(f"Sending {day} workout to {len(subscribers)} subscriber(s).")
    for chat_id, pref in subscribers:
        try:
            await context.bot.send_message(
                chat_id=chat_id,
                text=format_workout(day, pref),
                parse_mode="Markdown",
            )
        except Exception as e:
            logger.error(f"Failed to send to {chat_id}: {e}")


# ------------------ Main ------------------
def main() -> None:
    init_db()
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_cmd))
    application.add_handler(CommandHandler("today", today))
    application.add_handler(CommandHandler("home", set_home))
    application.add_handler(CommandHandler("gym", set_gym))
    application.add_handler(CommandHandler("stop", stop))

    send_time = time(hour=SEND_HOUR, minute=SEND_MINUTE, tzinfo=TIMEZONE)
    application.job_queue.run_daily(
        send_daily_workout, time=send_time, name="daily_workout"
    )

    logger.info(
        f"Bot starting. Daily workout scheduled for {send_time.strftime('%H:%M')} "
        f"({TIMEZONE_NAME})."
    )
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
