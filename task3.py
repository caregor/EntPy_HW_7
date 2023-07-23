"""
    ---Task 3---
    Задание №7
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""


import os
import random
from random import randint

MIN_LEN_NAME = 6
MAX_LEN_NAME = 30
MIN_SIZE = 256
MAX_SIZE = 4096
STR_CHAR = 'qwrtpsdfghjklzxcvbnmeyuioa'
MAX_ATTEMPTS = 1000

FILE_TYPES = {
    'видео': ['mp4', 'avi', 'mov'],
    'изображения': ['jpg', 'png', 'gif'],
    'текст': ['txt', 'doc', 'pdf'],
    # Add other types and their extensions as needed
}


def create_file(directory, file_type, exp: str, min_len_name=MIN_LEN_NAME, max_len_name=MAX_LEN_NAME, min_size=MIN_SIZE,
                max_size=MAX_SIZE, count_file=1):
    if not os.path.exists(directory):
        os.makedirs(directory)

    existing_files = set(os.listdir(directory))
    subdirectory = os.path.join(directory, file_type)

    if not os.path.exists(subdirectory):
        os.makedirs(subdirectory)

    for _ in range(count_file):
        attempt = 0
        name_file = "".join(random.choices(STR_CHAR, k=random.randint(min_len_name, max_len_name))) + '.' + exp

        while name_file in existing_files and attempt < MAX_ATTEMPTS:
            name_file = "".join(random.choices(STR_CHAR, k=random.randint(min_len_name, max_len_name))) + '.' + exp
            attempt += 1

        if name_file in existing_files:
            print(f"Не удалось создать файл с уникальным именем для расширения {exp}. "
            continue

        existing_files.add(name_file)

        file_path = os.path.join(subdirectory, name_file)
        with open(file_path, 'wb') as f:
            f.write(bytes(randint(0, 255) for _ in range(randint(min_size, max_size))))


def generate_files_with_extensions(directory, file_types, num_files_per_type):
    for file_type, extensions in file_types.items():
        count_files = num_files_per_type.get(file_type, 0)
        for ext in extensions:
            create_file(directory, file_type, ext, count_file=count_files)


def sort_files(directory, file_types):
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


if __name__ == '__main__':
    target_directory = 'garbage'
    num_files_per_type = {
        'видео': 3,
        'изображения': 5,
        'текст': 2
    }

    generate_files_with_extensions(target_directory, FILE_TYPES, num_files_per_type)

    input("Файлы создвны в папке 'garbage'. Нажмите ENTER для сортировки файлов.")

    sort_files(target_directory, FILE_TYPES)

    print("Сортировка завершена.")