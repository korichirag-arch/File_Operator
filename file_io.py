import os # OS File operations mate Import karayu, Direct file new create and instantly delete karva mate.
from datetime import datetime # kyare file create thayi eni mate datetime import karayu


class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    # 1. Navi Entry Add karava Mate 
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

    # 2. Badhhii entries view karva Mate
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

    # 3. Keyword ya date thi search karva Mate
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

            # Entries double newline thii split thai, ane keyword match karva mate case-insensitive search kariye
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

    # 4. Badhhi entries delete karne ke liye
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