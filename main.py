import logging
import pytz
from datetime import time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from workouts import WORKOUTS

# --- Configuration ---
# Replace with your actual bot token from @BotFather
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
# Set your desired timezone, e.g., 'America/New_York', 'Europe/London'
TIMEZONE = pytz.timezone('America/New_York') 
# Time to send the workout (24-hour format)
SEND_TIME = time(hour=7, minute=0, tzinfo=TIMEZONE) # 7:00 AM

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Helper function to format the workout message ---
def format_workout(day_key):
    workout = WORKOUTS.get(day_key)
    if not workout:
        return "No workout scheduled for today. Rest up!"

    message = f"*{workout['title']}*\n\n{workout['description']}\n\n"
    for i, exercise in enumerate(workout['exercises'], 1):
        message += f"{i}. {exercise}\n"
    message += "\nHave a great workout! 💪"
    return message

# --- Command Handlers ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message on /start."""
    user = update.effective_user
    welcome_text = (
        f"Hi {user.mention_html()}! 👋\n\n"
        "I'm your Daily Workout Bot. Every morning, I'll send you a new routine to try.\n\n"
        "Use /today to see today's workout immediately."
    )
    await update.message.reply_html(welcome_text)

async def today(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends the current day's workout on demand."""
    # Get the current day name in lowercase (e.g., 'monday')
    current_day = pytz.utc.localize(datetime.utcnow()).astimezone(TIMEZONE).strftime('%A').lower()
    message = format_workout(current_day)
    await update.message.reply_markdown(message)

# --- The Daily Job ---
async def send_daily_workout(context: ContextTypes.DEFAULT_TYPE) -> None:
    """Callback function for the daily job. Sends the workout to all subscribers."""
    # In a real bot, you would fetch a list of chat_ids from a database.
    # For this example, we'll use a placeholder list or a single chat.
    # IMPORTANT: You need a way to store user chat IDs. 
    # Here is a simple in-memory example (lost on restart):
    # subscriber_chat_ids = [123456789, 987654321] 
    
    # For demonstration, let's assume we have a list.
    # Replace this with your actual persistence logic.
    # For now, we'll just send to a test chat or log it.
    current_day = pytz.utc.localize(datetime.utcnow()).astimezone(TIMEZONE).strftime('%A').lower()
    message = format_workout(current_day)
    
    # Example: Send to a specific chat ID (replace with your own)
    # chat_id = YOUR_CHAT_ID 
    # await context.bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')
    
    logger.info(f"Daily workout sent for {current_day}: {message[:50]}...")

# --- Main Application Setup ---
def main() -> None:
    """Start the bot."""
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("today", today))

    # Schedule the daily job
    job_queue = application.job_queue
    job_queue.run_daily(send_daily_workout, time=SEND_TIME, name="daily_workout")

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
