"""
    ---Task 3---
    Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""

import os

FILE_TYPES = {
    'видео': ['mp4', 'avi', 'mov'],
    'изображения': ['jpg', 'png', 'gif'],
    'текст': ['txt', 'doc', 'pdf'],
}


def sort_files(directory, file_types):
    if not os.path.exists(directory):
        print(f"Папка '{directory}' не существует.")
        return

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = filename.split('.')[-1].lower()
            for file_type, extensions in file_types.items():
                if file_extension in extensions:
                    subdirectory = os.path.join(directory, file_type)
                    if not os.path.exists(subdirectory):
                        os.makedirs(subdirectory)

                    src_path = os.path.join(directory, filename)
                    dest_path = os.path.join(subdirectory, filename)
                    os.rename(src_path, dest_path)
    print("Сортировка завершена.")


if __name__ == '__main__':
    target_directory = 'files'

    sort_files(target_directory, FILE_TYPES)