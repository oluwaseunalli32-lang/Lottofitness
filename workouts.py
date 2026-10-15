# workouts.py
# All workout routines. Add or edit freely.

HOME_WORKOUTS = {
    "monday": {
        "title": "Monday — Full Body (Home)",
        "description": "A simple routine to start your week. No equipment needed.",
        "exercises": [
            "Bodyweight Squats — 3 sets x 10 reps",
            "Push-ups (knees allowed) — 3 sets x 5–8 reps",
            "Glute Bridges — 3 sets x 12 reps",
            "Plank — 3 sets x 20–30 seconds",
            "Jumping Jacks — 3 sets x 20 reps",
        ],
    },
    "tuesday": {
        "title": "Tuesday — Core & Cardio (Home)",
        "description": "Focus on your core and get your heart rate up.",
        "exercises": [
            "Crunches — 3 sets x 15 reps",
            "Russian Twists — 3 sets x 20 reps (10 each side)",
            "Leg Raises — 3 sets x 10 reps",
            "High Knees — 3 sets x 30 seconds",
            "Mountain Climbers — 3 sets x 20 reps",
        ],
    },
    "wednesday": {
        "title": "Wednesday — Lower Body (Home)",
        "description": "Legs and glutes with bodyweight only.",
        "exercises": [
            "Reverse Lunges — 3 sets x 10 reps per leg",
            "Wall Sit — 3 sets x 30 seconds",
            "Calf Raises — 3 sets x 20 reps",
            "Single-Leg Glute Bridge — 3 sets x 10 reps per side",
            "Squat Pulses — 3 sets x 20 reps",
        ],
    },
    "thursday": {
        "title": "Thursday — Upper Body (Home)",
        "description": "Build upper-body strength with no equipment.",
        "exercises": [
            "Incline Push-ups (hands on chair) — 3 sets x 10 reps",
            "Tricep Dips (on chair) — 3 sets x 8–10 reps",
            "Superman Hold — 3 sets x 20 seconds",
            "Pike Push-ups — 3 sets x 6–8 reps",
            "Arm Circles — 3 sets x 30 seconds each direction",
        ],
    },
    "friday": {
        "title": "Friday — Full Body Circuit (Home)",
        "description": "Complete each exercise back-to-back, rest 60s, repeat 3 times.",
        "exercises": [
            "Squats — 12 reps",
            "Push-ups — 10 reps",
            "Reverse Lunges — 10 reps per leg",
            "Plank — 30 seconds",
            "Jumping Jacks — 30 reps",
        ],
    },
    "saturday": {
        "title": "Saturday — Active Recovery (Home)",
        "description": "Light movement to help your body recover.",
        "exercises": [
            "20-minute walk (outdoors or on the spot)",
            "Cat–Cow Stretch — 10 reps",
            "Child's Pose — 60 seconds",
            "Hamstring Stretch — 30 seconds per leg",
            "Deep Breathing — 2 minutes",
        ],
    },
    "sunday": {
        "title": "Sunday — Rest Day",
        "description": "Rest and recover. You've earned it!",
        "exercises": [
            "Hydrate well — aim for 8 glasses of water",
            "Light stretching — 5–10 minutes",
            "Prep meals for the week ahead",
        ],
    },
}

GYM_WORKOUTS = {
    "monday": {
        "title": "Monday — Push Day (Gym)",
        "description": "Chest, shoulders, triceps. Warm up 5–10 minutes first.",
        "exercises": [
            "Bench Press — 4 sets x 8 reps",
            "Incline Dumbbell Press — 3 sets x 10 reps",
            "Seated Shoulder Press — 3 sets x 10 reps",
            "Cable Fly — 3 sets x 12 reps",
            "Tricep Rope Pushdown — 3 sets x 12 reps",
        ],
    },
    "tuesday": {
        "title": "Tuesday — Pull Day (Gym)",
        "description": "Back and biceps. Control the negative on every rep.",
        "exercises": [
            "Lat Pulldown — 4 sets x 10 reps",
            "Seated Cable Row — 3 sets x 10 reps",
            "Dumbbell Row — 3 sets x 10 reps per side",
            "Face Pulls — 3 sets x 15 reps",
            "Barbell Curl — 3 sets x 10 reps",
        ],
    },
    "wednesday": {
        "title": "Wednesday — Leg Day (Gym)",
        "description": "Quads, hamstrings, glutes. Don't skip the warm-up.",
        "exercises": [
            "Squat — 4 sets x 8 reps",
            "Romanian Deadlift — 3 sets x 10 reps",
            "Leg Press — 3 sets x 12 reps",
            "Leg Curl — 3 sets x 12 reps",
            "Standing Calf Raise — 4 sets x 15 reps",
        ],
    },
    "thursday": {
        "title": "Thursday — Upper Body (Gym)",
        "description": "Balanced upper-body session.",
        "exercises": [
            "Incline Bench Press — 4 sets x 8 reps",
            "Pull-ups (or assisted) — 4 sets x 6–8 reps",
            "Lateral Raises — 3 sets x 15 reps",
            "Cable Row — 3 sets x 12 reps",
            "Hammer Curls — 3 sets x 12 reps",
        ],
    },
    "friday": {
        "title": "Friday — Full Body (Gym)",
        "description": "Compound movements to finish the week strong.",
        "exercises": [
            "Deadlift — 4 sets x 5 reps",
            "Overhead Press — 3 sets x 8 reps",
            "Goblet Squat — 3 sets x 12 reps",
            "Dumbbell Row — 3 sets x 10 reps per side",
            "Plank — 3 sets x 45 seconds",
        ],
    },
    "saturday": {
        "title": "Saturday — Cardio & Core (Gym)",
        "description": "Light cardio followed by a core circuit.",
        "exercises": [
            "Treadmill / Bike — 20 minutes steady-state",
            "Hanging Leg Raises — 3 sets x 10 reps",
            "Cable Crunches — 3 sets x 15 reps",
            "Russian Twists — 3 sets x 20 reps",
            "Plank — 3 sets x 60 seconds",
        ],
    },
    "sunday": {
        "title": "Sunday — Rest Day",
        "description": "Recovery day. Sleep well and eat well.",
        "exercises": [
            "Full rest — no training",
            "Foam roll or massage tight areas",
            "8+ hours of sleep tonight",
        ],
    },
}
