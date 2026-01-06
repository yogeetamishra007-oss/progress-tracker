from datetime import datetime,timedelta
# progress wali file
FILE_NAME = "progress.txt"


def add_progress():
    task = input("What did you work on today? ").strip()
    if not task:
        print("Error: Task cant be empty.")
        return
    if not any(char.isalpha() for char in task):
        print("Error.Task must contain letters(not just numbers or symbols.)")
        return
    try:
        hours = float(input("How many hours did you study/work? "))
        if hours<=0:
            print("Error. Hours must be greater than 0")
            return
    except ValueError:
        print("Error.Please enter valid no. for hours")

    date = datetime.today().date()
    entry = f"{date},{task},{hours}\n"

    with open(FILE_NAME, "a") as file:
        file.write(entry)
    print("Progress saved successfully\n")


def view_progress():
    try:
        with open(FILE_NAME, "r") as file:
            lines=file.readlines()
        if not lines:
            print("No progress recorded yet.\n")
            return
        print("\n______________________________________")
        print("PROGRESS LOG")
        print("________________________________________")
        for line in lines:
            date, task, hours = line.strip().split(",", 2)
            print(f"Date: {date} | Task: {task} | Hours: {hours}")
        print("________________________________________\n")
    except FileNotFoundError:
        print("No progress file found yet.\n")


def weekly_comparison():
    weekly_hours = {}

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                date_str, task, hours = line.strip().split(",")

                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                week = date.isocalendar()[1]

                weekly_hours[week] = weekly_hours.get(week, 0) + float(hours)

        if len(weekly_hours) < 2:
            print("Not enough data to compare weeks.\n")
            return

        weeks = sorted(weekly_hours.keys())
        last_week = weeks[-2]
        current_week = weeks[-1]

        last_hours = weekly_hours[last_week]
        current_hours = weekly_hours[current_week]
        diff = current_hours - last_hours

        print("\nWeekly Comparison:")
        print(f"Last week ({last_week}): {last_hours} hrs")
        print(f"This week ({current_week}): {current_hours} hrs")

        if diff > 0:
            print(f" Improved by {diff} hours\n")
        elif diff < 0:
            print(f" Worsened by {abs(diff)} hours.\n")
        else:
            print(" No change from last week.\n")

    except FileNotFoundError:
        print("No data found yet.\n")


def main():
    while True:
        print("Progress Tracker")
        print("1. Add today's progress")
        print("2. View all progress")
        print("3. Compare weekly progress")
        print("4. View streak summary")
        print("5. Delete a progress entry")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice== "1":
            add_progress()
        elif choice == "2":
            view_progress()
        elif choice == "3":
            weekly_comparison()
        elif choice== "4":
            calculate_streak()
        elif choice== "5":
            delete_progress()
        elif choice=="6":
            print("Bai bai Keep going.")
            break
        else:
            print("Invalid choice. Try again.\n")

def calculate_streak():
    dates = []

    try:
        with open("progress.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                date_str = line.split(",")[0]
                date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
                dates.append(date_obj)

    except FileNotFoundError:
        print("Progress file not found.")
        return

    if not dates:
        print("No progress recorded yet.")
        return

    dates = sorted(set(dates))  # remove duplicates + sort

    current_streak = 1
    longest_streak = 1

    for i in range(1, len(dates)):
        if dates[i] == dates[i - 1] + timedelta(days=1):
            current_streak += 1
        else:
            current_streak = 1

        longest_streak = max(longest_streak, current_streak)

    today = datetime.today().date()
    logged_today = dates[-1] == today

    print("\n______________________________________")
    print("STREAK SUMMARY")
    print("________________________________________")
    print(f"Current streak : {current_streak} days")
    print(f"Longest streak : {longest_streak} days")
    print(f"Logged today   : {'Yes' if logged_today else 'No'}")
    print("________________________________________\n")
    
def delete_progress():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No progress to delete.\n")
            return

        print("\nSaved Progress:")
        for i, line in enumerate(lines, start=1):
            date, task, hours = line.strip().split(",", 2)
            print(f"{i}. Date: {date} | Task: {task} | Hours: {hours}")

        choice = input("\nEnter the number of the entry to delete (or press Enter to cancel): ").strip()

        if choice == "":
            print("Delete cancelled.\n")
            return

        if not choice.isdigit():
            print("Invalid choice.\n")
            return

        index = int(choice) - 1

        if index < 0 or index >= len(lines):
            print("Invalid entry number.\n")
            return

        deleted = lines.pop(index)

        with open(FILE_NAME, "w") as file:
            file.writelines(lines)

        date, task, hours = deleted.strip().split(",", 2)

        print("Deleted entry:")
        print(f"Date: {date} | Task: {task} | Hours: {hours}")

    except FileNotFoundError:
        print("No progress file found.\n")

main()