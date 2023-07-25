"""
    ---Task 2---
    Задание №6
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
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


def create_file(directory, exp: str, min_len_name=MIN_LEN_NAME, max_len_name=MAX_LEN_NAME, min_size=MIN_SIZE,
                max_size=MAX_SIZE, count_file=1):
    if not os.path.exists(directory):
        os.makedirs(directory)

    existing_files = set(os.listdir(directory))
    for _ in range(count_file):
        attempt = 0
        name_file = "".join(random.choices(STR_CHAR, k=random.randint(min_len_name, max_len_name))) + '.' + exp

        while name_file in existing_files and attempt < MAX_ATTEMPTS:
            name_file = "".join(random.choices(STR_CHAR, k=random.randint(min_len_name, max_len_name))) + '.' + exp
            attempt += 1

        if name_file in existing_files:
            print(f"Не удалось создать файл с уникальным именем для расширения {exp}. ")
            continue

        existing_files.add(name_file)

        file_path = os.path.join(directory, name_file)
        with open(file_path, 'wb') as f:
            f.write(bytes(randint(0, 255) for _ in range(randint(min_size, max_size))))


def generate_files_with_extensions(directory, extensions, num_files_per_extension):
    for extension, count_file in zip(extensions, num_files_per_extension):
        create_file(directory, extension, count_file=count_file)


if __name__ == '__main__':
    target_directory = 'files'
    extensions_list = ['txt', 'mp4', 'jpg']
    num_files_per_extension = [3, 5, 2]
    generate_files_with_extensions(target_directory, extensions_list, num_files_per_extension)