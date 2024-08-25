
# 📂 File Organizer

A simple yet effective Python script to organize files in a specified directory by categorizing them into folders based on their file types. It's perfect for cleaning up your Downloads folder or any other directory that's gotten out of hand!

## 🚀 Features

- 📁 Automatically creates folders for each file type (e.g., Images, Documents, Audio).
- 🔄 Moves files into their corresponding folders based on their extensions.
- 🗂️ Unrecognized file types are moved into an "Others" folder.

## 🛠️ Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/megapxzeeoh/FileOrganizer.git
    cd FileOrganizer
    ```

2. Make sure you have Python 3 installed. You can check your Python version by running:
    ```bash
    python --version
    ```

3. No additional dependencies are required for this script.

## 📝 Usage

1. Run the script by using the following command in your terminal:
    ```bash
    python organizer.py
    ```

2. Enter the path to the directory you want to organize when prompted.

3. The script will create folders based on the following categories and move the files accordingly:
    - Images: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
    - Documents: `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
    - Audio: `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`
    - Video: `.mp4`, `.mov`, `.avi`, `.mkv`
    - Archives: `.zip`, `.rar`, `.tar`, `.gz`, `.7z`
    - Scripts: `.py`, `.js`, `.sh`, `.bat`, `.rb`
    - Others: Any file type not listed above

4. Enjoy your newly organized folder!

## 💡 Example

Before:
```
Downloads/
│
├── photo.jpg
├── resume.pdf
├── song.mp3
├── script.py
└── archive.zip
```

After running the script:
```
Downloads/
│
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Audio/
│   └── song.mp3
├── Scripts/
│   └── script.py
├── Archives/
│   └── archive.zip
└── Others/
```

## 🐛 Issues and Contributions

If you have any ideas or encounter any bugs, feel free to reach out in the Telegram channel: [@bleckatool](https://t.me/bleckatool).

## 🌟 Support

If you find this tool useful, consider giving it a ⭐ on GitHub!
```
