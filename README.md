# Smart Rename

Smart Rename is a cross-platform command-line bulk file renaming tool built in Python.  
It helps users quickly rename multiple files using different renaming operations directly from the terminal.

This project works on:

- Windows
- Linux
- macOS

---

# Features

- Add prefixes to filenames
- Add suffixes to filenames
- Sequential numbering
- Find and replace text
- Convert filenames to:
  - Uppercase
  - Lowercase
  - Title Case
- Change file extensions
- Rename only specific file types
- Recursive renaming in subfolders
- Preview filename changes before applying
- Confirmation mode using `--yes`
- Undo previous rename operation
- Duplicate filename protection
- Cross-platform support using `pathlib`

---

# Technologies Used

- Python
- pathlib
- argparse
- json

---

# Project Structure

```text
Smart_Rename/
│
├── bulkrename.py
├── renamer.py
├── undo.json
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Smart_Rename.git
```

Move into the project folder:

```bash
cd Smart_Rename
```

---

# Usage

## Basic Syntax

```bash
py bulkrename.py "FOLDER_PATH" [OPTIONS]
```

---

# Examples

## Add Prefix

```bash
py bulkrename.py "E:\Photos" --prefix Vacation
```

---

## Add Prefix and Apply Changes

```bash
py bulkrename.py "E:\Photos" --prefix Vacation --yes
```

---

## Add Suffix

```bash
py bulkrename.py "E:\Photos" --suffix Edited
```

---

## Sequential Numbering

```bash
py bulkrename.py "E:\Photos" --numbering
```

---

## Find and Replace

```bash
py bulkrename.py "E:\Photos" --replace IMG Photo
```

---

## Convert Filenames to Uppercase

```bash
py bulkrename.py "E:\Photos" --upper
```

---

## Convert Filenames to Lowercase

```bash
py bulkrename.py "E:\Photos" --lower
```

---

## Convert Filenames to Title Case

```bash
py bulkrename.py "E:\Photos" --title
```

---

## Change File Extension

```bash
py bulkrename.py "E:\Photos" --extension .jpg
```

---

## Rename Specific File Types

```bash
py bulkrename.py "E:\Photos" --type .jpeg .jpg
```

---

## Recursive Rename

```bash
py bulkrename.py "E:\Photos" --prefix New --recursive
```

---

## Undo Previous Rename

```bash
py bulkrename.py "E:\Photos" --undo
```

---

# Help Menu

```bash
py bulkrename.py --help
```

---

# Preview Mode

By default, Smart Rename only shows a preview of changes.

Example:

```text
PREVIEW

photo.jpg -> Vacation_photo.jpg
image.png -> Vacation_image.png
```

To apply changes permanently, use:

```bash
--yes
```

---

# Undo System

Smart Rename stores rename history in:

```text
undo.json
```

You can restore the previous filenames using:

```bash
py bulkrename.py "FOLDER_PATH" --undo
```

---

# Error Handling

The application handles:

- Invalid folder paths
- Duplicate filenames
- Missing files
- File extension validation
- Undo conflicts
- Permission-related issues

---

# Learning Goals

This project was built to improve skills in:

- Python scripting
- File handling
- Command-line applications
- Cross-platform compatibility
- Error handling
- Modular programming
- JSON handling
- Clean code structure

---

# Future Improvements

- Regex rename support
- Multiple undo history
- Interactive CLI mode
- Colored terminal output
- Logging system
- GUI version

---

# Author

Wajid Ali

Python Developer & Learning Full Stack / AI Development
