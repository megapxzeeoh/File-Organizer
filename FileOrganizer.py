import os
import shutil
from pathlib import Path

# Словарь для определения категорий файлов
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Video": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".rb"]
}

def organize_files(directory):
    """Функция для сортировки файлов в указанной директории."""
    # Проверка существования директории
    if not os.path.exists(directory):
        print(f"Директория '{directory}' не существует.")
        return
    
    # Создание папок для каждой категории
    for category in FILE_CATEGORIES:
        category_path = Path(directory) / category
        if not category_path.exists():
            category_path.mkdir()
    
    # Перемещение файлов в соответствующие папки
    for item in os.listdir(directory):
        item_path = Path(directory) / item
        if item_path.is_file():
            file_extension = item_path.suffix.lower()
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    shutil.move(str(item_path), str(Path(directory) / category / item))
                    print(f"Файл '{item}' перемещён в папку '{category}'")
                    moved = True
                    break
            if not moved:
                # Если расширение файла не найдено в списке, перемещаем в папку "Others"
                others_path = Path(directory) / "Others"
                if not others_path.exists():
                    others_path.mkdir()
                shutil.move(str(item_path), str(others_path / item))
                print(f"Файл '{item}' перемещён в папку 'Others'")
    
    print("Сортировка завершена.")

if __name__ == "__main__":
    # Пример использования
    directory_to_organize = input("Введите путь к директории, которую нужно организовать: ")
    organize_files(directory_to_organize)

