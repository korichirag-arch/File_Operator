# 📓 Personal Journal Manager

A lightweight, terminal-based Python application to record, manage, and search personal daily notes and journal entries with automated timestamps and persistent file storage.

---

## 🌟 Features

- **Automated Timestamping:** Every entry is automatically tagged with the current date and time (`YYYY-MM-DD HH:MM:SS`).
- **Persistent File Storage:** Keeps all journal logs safely stored in a local text file (`journal.txt`).
- **View All Logs:** Read through past thoughts and entries formatted in chronological blocks.
- **Keyword & Date Search:** Case-insensitive search to quickly find entries by specific keywords, terms, or dates.
- **Safe Reset & Deletion:** Option to wipe all journal entries with a confirmation check (`yes/no`) to prevent accidental data loss.
- **Robust Error Handling:** Built-in exceptions for `FileNotFoundError`, `PermissionError`, and invalid user prompts.

---

## 🛠️ Tech Stack & Concepts Covered

| Module / Concept | Purpose |
| :--- | :--- |
| **Object-Oriented Programming (OOP)** | Modular design using the `JournalManager` class |
| **File I/O (`open()`)** | Reading (`r`) and appending (`a`) text logs persistently |
| **`os` Module** | File existence checks (`os.path.exists`) and file deletion (`os.remove`) |
| **`datetime` Module** | Dynamic timestamp creation (`datetime.now().strftime`) |
| **String Manipulation** | Chunking logs with `.split("\n\n")` and case-insensitive matching (`.lower()`) |

---

## 📂 Project Structure

```text
.
├── journal_manager.py     # Main application script
├── journal.txt            # Auto-generated text file storing your entries
└── README.md              # Project documentation

👤 Author
GitHub: @korichirag-archr
