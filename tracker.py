import datetime

# progress wali file
FILE_NAME = "progress.txt"


def add_progress():
    task = input("What did you work on today? ")
    hours = float(input("How many hours did you study/work? "))

    date = datetime.date.today()
    entry = f"{date},{task},{hours}\n"

    with open(FILE_NAME, "a") as file:
        file.write(entry)

    print("Progress saved successfully!\n")


def view_progress():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.read()

            if data.strip() == "":
                print("No progress recorded yet.\n")
            else:
                print("\nYour Progress:")
                print("--------------------")
                for line in data.splitlines():
                    date, task, hours = line.split(",")
                    print(f"Date: {date} | Task: {task} | Hours: {hours}")
                print()

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
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_progress()
        elif choice == "2":
            view_progress()
        elif choice == "3":
            weekly_comparison()
        elif choice == "4":
            print("Bai bai Keep going.")
            break
        else:
            print("Invalid choice. Try again.\n")


main()