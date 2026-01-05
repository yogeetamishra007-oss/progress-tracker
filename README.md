# Progress Tracker (Python)

A simple command-line progress tracker built using Python.

This project helps track daily study or work tasks along with the number of hours spent. The data is stored locally and can be used to compare weekly progress to see improvement or decline over time.

## Features
- Add daily progress (task and hours)
- View all recorded progress
- Compare weekly progress totals
- File-based storage using a simple CSV format
- Menu-driven CLI interface

## How it works
Each entry is saved with:
- Date
- Task name
- Hours spent

The data is stored in a local text file (`progress.txt`).  
Weekly progress is calculated using Python’s `datetime` module and ISO week numbers.

## Project Structure
progress_tracker/ ├── tracker.py   ├── progress.txt   └── README.md       
## Tech Stack
- Python
- datetime module
- File handling (CSV-style data)

## Usage
Run the script using:

```bash
python tracker.py ```