# Personal Journal Manager

A simple, interactive console-based Python application to manage daily journal entries. This project demonstrates core Object-Oriented Programming (OOP) concepts, robust text file handling, and proper exception handling.

## 📌 Project Overview

The **Personal Journal Manager** allows users to maintain personal daily notes in a single text file (`journal.txt`). Every entry is automatically saved along with a date and time stamp. The application provides an easy-to-use menu to add, read, search, and delete journal records safely without crashing on runtime errors.

## ✨ Features

* **Add New Entry:** Appends a new journal entry with the current date and time (`YYYY-MM-DD HH:MM:SS`).
* **View All Entries:** Displays all saved entries formatted clearly.
* **Search Entries:** Allows searching by keyword or date (case-insensitive).
* **Delete All Entries:** Permanently removes the journal file after user confirmation.
* **Safe Error Handling:** Gracefully handles missing files (`FileNotFoundError`), permission issues, and invalid menu inputs.

## 🛠️ Concepts & Technologies Used

* **Language:** Python 3.x
* **Object-Oriented Programming (OOP):** Encapsulated logic inside the `JournalManager` class.
* **File Handling Modes:**
  * `'a'` (Append Mode): Appends new entries or creates the file if it does not exist.
  * `'r'` (Read Mode): Reads entries for viewing and searching.
* **Python Modules:**
  * `datetime`: For generating accurate timestamps for each entry.
  * `os`: To check file presence (`os.path.exists`) and remove files (`os.remove`).
* **Exception Handling:** Using `try...except` blocks to prevent unexpected program crashes.

## 💻 Complete Source Code (`journal_manager.py`)

Neeche is project ka complete Python code diya gaya hai:

```python
import os
from datetime import datetime


class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    # 1. Nayi entry add karne ke liye
    def add_entry(self):
        text = input("\nEnter your journal entry:\n").strip()
        if not text:
            print("Error: Empty entry cannot be added.")
            return

        # Current timestamp format: YYYY-MM-DD HH:MM:SS
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(self.filename, "a") as f:
                f.write(f"[{timestamp}]\n")
                f.write(f"{text}\n\n")
            print("\nEntry added successfully!")
        except PermissionError:
            print("Error: Permission denied while writing to file.")
        except Exception as e:
            print(f"Error: {e}")

    # 2. Saari entries view karne ke liye
    def view_all_entries(self):
        try:
            with open(self.filename, "r") as f:
                content = f.read().strip()

            if not content:
                print("\nNo journal entries found. Start by adding a new entry!")
            else:
                print("\nYour Journal Entries:")
                print("---------------------")
                print(content)

        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("\nError: Permission denied to read file.")
        except Exception as e:
            print(f"\nError: {e}")

    # 3. Keyword ya date se search karne ke liye
    def search_entry(self):
        keyword = input("\nEnter a keyword or date to search: ").strip()
        if not keyword:
            print("Please enter something to search.")
            return

        try:
            with open(self.filename, "r") as f:
                content = f.read().strip()

            if not content:
                print(f"\nNo entries were found for the keyword: {keyword}")
                return

            blocks = content.split("\n\n")
            matched_blocks = []

            for block in blocks:
                if keyword.lower() in block.lower():
                    matched_blocks.append(block)

            if matched_blocks:
                print("\nMatching Entries:")
                print("---------------------")
                for item in matched_blocks:
                    print(item + "\n")
            else:
                print(f"\nNo entries were found for the keyword: {keyword}")

        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
        except Exception as e:
            print(f"\nError: {e}")

    # 4. Saari entries delete karne ke liye
    def delete_all_entries(self):
        if not os.path.exists(self.filename):
            print("\nNo journal entries to delete.")
            return

        confirm = input("\nAre you sure you want to delete all entries? (yes/no): ").strip().lower()
        if confirm == "yes":
            try:
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")
            except Exception as e:
                print(f"\nError while deleting: {e}")
        else:
            print("\nDelete operation cancelled.")


def main():
    manager = JournalManager()

    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("\nUser Input: ").strip()

        if choice == "1":
            manager.add_entry()
        elif choice == "2":
            manager.view_all_entries()
        elif choice == "3":
            manager.search_entry()
        elif choice == "4":
            manager.delete_all_entries()
        elif choice == "5":
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("\nInvalid option. Please select a valid option from the menu.")


if __name__ == "__main__":
    main()
```

## 📂 Project Structure

```text
├── journal_manager.py   # Main Python source code
├── journal.txt          # File where journal entries are stored (auto-generated)
└── README.md            # Project documentation and source code
```

## 🚀 How to Run the Program

1. **Clone this repository:**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Run the script:**
   ```bash
   python journal_manager.py
   ```

3. **Follow the on-screen menu:**
   * Enter `1` to write a new note.
   * Enter `2` to read all existing notes.
   * Enter `3` to search by keyword/date.
   * Enter `4` to delete all notes.
   * Enter `5` to exit the application.

## 🖥️ Example Console Output

### Adding an Entry:
```text
Welcome to Personal Journal Manager!
Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

User Input: 1

Enter your journal entry:
Today I practiced Python file handling and OOP.

Entry added successfully!
```

### Viewing Entries:
```text
User Input: 2

Your Journal Entries:
---------------------
[2026-10-12 11:30:15]
Today I practiced Python file handling and OOP.
```

## 👤 Author

* **Name:** Your Name
* **Institute:** Red & White Skill Education