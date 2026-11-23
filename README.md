# 📁 Python File Organiser

## 📌 Project Description

Python File Organiser is a simple file management automation project developed using Python. It automatically organizes files in a selected directory into separate folders based on their file extensions.

The program reduces the effort of manually sorting files and helps maintain a clean and व्यवस्थित folder structure.

## ✨ Features

- Takes the folder path as input from the user.
- Automatically creates folders if they do not exist.
- Identifies files based on their extensions.
- Moves files into their respective folders.
- Skips directories while organizing files.
- Supports multiple file formats.
- Uses Python's built-in modules.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Modules Used:**
  - `os` – For file and directory operations.
  - `shutil` – For moving files from one folder to another.

## 📂 Project Structure

```text
FileOrganiser/
│
├── file_organiser.py
└── README.md
```

After execution, the selected folder will be organized as follows:

```text
Selected_Folder/
│
├── PDFs/
│   └── example.pdf
│
├── Word_Files/
│   └── document.docx
│
├── Images/
│   └── photo.jpg
│
├── Videos/
│   └── movie.mp4
│
└── Text_Files/
    └── notes.txt
```

## 📑 Supported File Types

| Folder Name | File Extensions |
|---|---|
| PDFs | `.pdf` |
| Word_Files | `.docx`, `.doc` |
| Images | `.jpg`, `.jpeg`, `.png` |
| Videos | `.mp4`, `.mkv` |
| Text_Files | `.txt` |

## ⚙️ Requirements

- Python 3.x
- VS Code or any Python-supported IDE

**Note:** The `os` and `shutil` modules are built into Python. No additional library installation is required.

## 🚀 How to Run the Project

**Step 1:** Install Python on your computer.

**Step 2:** Download or clone this project.

**Step 3:** Open the project in VS Code.

**Step 4:** Run the following command in the terminal:

```bash
python file_organiser.py
```

**Step 5:** Enter the path of the folder you want to organize.

Example:

```text
Enter the path of the folder to organize:
C:\Users\Jay\Downloads
```

The program will automatically create the required folders and move the matching files.

## 💻 Sample Output

```text
Enter the path of the folder to organize:
C:\Users\Jay\Downloads

Files have been organized into folders based on their types ✓.
```

## 🔍 Working of the Project

1. The program imports the `os` and `shutil` modules.
2. It asks the user to enter the directory path.
3. A dictionary named `FILE_TYPES` stores folder names and their supported extensions.
4. The program checks whether the required folders exist.
5. If a folder does not exist, it creates one using `os.mkdir()`.
6. It scans all items in the selected directory using `os.listdir()`.
7. It skips directories using `os.path.isdir()`.
8. It extracts file extensions using `os.path.splitext()`.
9. It matches each extension with the dictionary.
10. It moves matching files using `shutil.move()`.

## 🎯 Objective

The main objective of this project is to learn Python file handling and directory management while developing a practical automation tool that organizes files efficiently.

## 📚 Concepts Used

- Python Dictionaries
- For Loops
- Conditional Statements
- User Input
- File Handling
- Directory Management
- Modules and Functions

## 👨‍💻 Author

**Jay**

## 📜 License

This project is developed for educational and personal use.
