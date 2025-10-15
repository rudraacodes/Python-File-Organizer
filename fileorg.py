import os #Helps intract with the operating system
import shutil #Helps move files around
import importlib.util


# Path to the log file that will be created in the same directory being organizing
LOG_FILE_NAME = "move_log.txt"


#File categorization dictionary

# --- Load external categories safely ---
cat_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "categories.py")

if os.path.exists(cat_file):
    spec = importlib.util.spec_from_file_location("categories", cat_file)
    categories = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(categories)
    file_cat = categories.file_cat
    print("✅ Loaded categories from 'categories.py'")
else:
    print("⚠️ 'categories.py' not found. Using default minimal categories.")
    file_cat = {
    # 🖼️ Media
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],

    # 📄 Work & Text
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx", ".odp"],

    # 💻 Development
    "Code": [".py", ".cpp", ".c", ".java", ".js", ".html", ".css", ".php", ".sql"],
    "Configs": [".json", ".yaml", ".yml", ".ini", ".cfg"],

    # 📦 Archives / Executables
    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".apk", ".bat", ".sh"],

    # 🎨 Creative & Misc
    "Design": [".psd", ".ai", ".xd", ".fig"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Torrents": [".torrent"],

    # 📊 Data
    "Data": [".db", ".sqlite", ".sql", ".xml"],

    # 🚀 Fallback
    "Others": []
}


def org_files(directory):  # Organizes files in the given directory
    if not os.path.isdir(directory):
        print(f"\nError: {directory} is not a valid directory.\n")
        return

    # Log file will store "new_path|old_path" for each move
    log_path = os.path.join(directory, LOG_FILE_NAME)

    with open(log_path, "w", encoding="utf-8") as log_file:
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)

            # Skip if it's a folder or our own log file
            if os.path.isdir(file_path) or file_name == LOG_FILE_NAME:
                continue

            file_moved = False  # Flag to check if the file found a matching category

            # Loop through categories and extensions
            for cat, extensions in file_cat.items():
                # 'any()' checks if the file ends with any of the listed extensions
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    # Folder is created only when a file fits the category
                    cat_path = os.path.join(directory, cat)
                    os.makedirs(cat_path, exist_ok=True)

                    new_path = os.path.join(cat_path, file_name)
                    shutil.move(file_path, new_path)

                    # Log this move for potential reversion
                    log_file.write(f"{new_path}|{file_path}\n")
                    file_moved = True
                    break

            # If the file doesn’t match any category, move to "Others"
            if not file_moved:
                others_path = os.path.join(directory, "Others")
                os.makedirs(others_path, exist_ok=True)
                new_path = os.path.join(others_path, file_name)
                shutil.move(file_path, new_path)
                log_file.write(f"{new_path}|{file_path}\n")

    print(f"\n✅ Files organized successfully. Log saved at: {log_path}\n")


def revert_changes(directory):
    # Find the log file in the given directory
    log_path = os.path.join(directory, LOG_FILE_NAME)

    # If no log exists, there's nothing to revert
    if not os.path.exists(log_path):
        print("\nNo move log found. Cannot revert.\n")
        return

    # Open the log and go through each recorded move
    with open(log_path, "r", encoding="utf-8") as log_file:
        lines = log_file.readlines()

    # For each recorded line: move the file back to its original place
    for line in lines:
        moved_path, original_path = line.strip().split("|")

        # Move the file back only if it still exists in its new place
        if os.path.exists(moved_path):
            # Create the original directory if needed (in case it was deleted)
            os.makedirs(os.path.dirname(original_path), exist_ok=True)
            shutil.move(moved_path, original_path)

    print("\n♻️ Reverted all file moves successfully!\n")


if __name__ == "__main__":
    choice = input("Choose an action:\n1. Organize files\n2. Revert last organization\n> ")

    dir_to_org = input("Enter the directory path: ")

    if choice == "1":
        use_external = input("Use external categorization file? (y/n): ").lower().strip() == "y"
        if use_external:
            try:
                from categories import file_cat
                print("📁 Using categories from 'categories.py'")
            except ImportError:
                print("⚠️ Could not load external categories. Using default.")

            org_files(dir_to_org)
    elif choice == "2":
        revert_changes(dir_to_org)
    else:
        print("Invalid choice.")