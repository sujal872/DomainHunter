import os
import json
from datetime import datetime, UTC

# ================= REPORT =================

def report_generator(data):
    choice = input("\nDo you want to save report? (y/n): ").lower()

    if choice != 'y':
        return "Report not saved."

    os.makedirs("reports", exist_ok=True)

    f_name = f"reports/report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"

    with open(f_name, 'w') as f:
        json.dump(data, f, indent=4, default=str)

    return f"Report saved: {f_name}"


def report_reader():
    folder = "reports"

    if not os.path.exists(folder):
        return "No reports folder found."

    files = [f for f in os.listdir(folder) if f.endswith(".json")]

    if not files:
        return "No JSON reports found."

    print("\nAvailable Reports:\n")
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

    try:
        choice = int(input("\nEnter file number: "))

        if choice < 1 or choice > len(files):
            return "Invalid choice."

        selected_file = os.path.join(folder, files[choice - 1])

        with open(selected_file, 'r') as f:
            data = json.load(f)

        print("\nReport Content:\n")
        print(json.dumps(data, indent=4))

        return "Report opened successfully."

    except ValueError:
        return "Enter a valid number."