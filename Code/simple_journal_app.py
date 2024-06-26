# simple_journal_app.py
class Journal:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def view_entries(self):
        return self.entries

if __name__ == "__main__":
    journal = Journal()
    while True:
        action = input("Choose action: add, view, or quit: ").strip().lower()
        if action == 'add':
            entry = input("Enter your journal entry: ")
            journal.add_entry(entry)
        elif action == 'view':
            entries = journal.view_entries()
            print("Journal Entries:")
            for i, entry in enumerate(entries, 1):
                print(f"{i}. {entry}")
        elif action == 'quit':
            break
