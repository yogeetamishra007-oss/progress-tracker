## Progress Tracker (Python)

This is a terminal-based progress tracker built using Python.  
It helps track daily tasks and study hours, stores progress locally, and provides useful summaries to analyze consistency over time.

The project is intentionally kept simple and beginner-friendly, with a focus on clean logic and gradual feature improvements.

## Features
- Add daily progress (date, task, hours)
- View all recorded progress
- Weekly progress summary
- Total hours worked
- Streak tracking
- Calculates current streak based on consecutive active days
- Tracks longest streak achieved
- Indicates whether progress was logged today
- Data stored locally in a text file (CSV-style format)
- Menu-driven CLI interface

## Streak Tracking

The streak feature analyzes the dates on which progress was logged.

- A streak increases when progress is logged on consecutive days.
- If a day is missed, the current streak resets.
- Duplicate entries for the same day are ignored.
- The tracker displays:
  - Current streak
  - Longest streak
  - Whether progress has been logged today
## How to Run

1. Clone the repository or download the ZIP
2. Make sure Python is installed
3. Open a terminal in the project folder
4. Run the program using:

   python tracker.py


### Project Structure

```text
Progress_tracker
├── tracker.py
├── progress.txt
└── README.md
```    
## Tech Stack
- Python
- datetime module
- File handling (CSV-style data)

## Planned Improvements

- Daily goal tracking (e.g., target study hours per day)
- Weekly comparison (current week vs previous week)
- Improved error handling and input validation
- Refactoring logic to make it reusable for a web interface
- Optional Flask-based web dashboard with a clean UI
- Visual progress representation (graphs or progress indicators)
These features will be added gradually as the project evolves.

## Notes

This project is part of my learning journey with Python.
The focus is on building features step by step, improving code structure, and gradually enhancing usability rather than rushing complexity.