# Python-File-Organizer
A modular Python file organizer that categorizes files by type, supports external category definitions, and allows reverting file moves.

# File Organizer 🗂️

Organize your files automatically into folders by type.  
Supports **custom categories** and can **revert moves** if needed.

## Features

- Categorizes files: Images, Videos, Documents, Code, Audio, Archives, etc.
- Uses an external `categories.py` file for custom categories.
- Creates folders **only when needed**.
- Keeps a log file `move_log.txt` to revert moves.
- Works on Windows, Mac, Linux.
- No extra Python packages required.

## How to Use

1. Clone the repo:-
git clone https://github.com/YOUR_USERNAME/file-organizer.git
cd file-organizer

2. Edit `categories.py` if you want custom categories (optional).

3. Run the organizer:-
python organizer.py

5. Follow the prompts:-
   - Organize files or revert previous organization.
   - Enter the directory you want to organize.
   - Choose whether to use external categories.
