"""
    ---Task 1 ---
    Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""
import random
from random import randint

MIN_LEN_NAME = 6
MAX_LEN_NAME = 30
MIN_SIZE = 256
MAX_SIZE = 4096
STR_CHAR = 'qwrtpsdfghjklzxcvbnmeyuioa'


def create_file(exp: str, min_len_name=MIN_LEN_NAME, max_len_name=MAX_LEN_NAME, min_size=MIN_SIZE, max_size=MAX_SIZE,
                count_file=1):
    for _ in range(count_file):
        name_file = "".join(random.choices(STR_CHAR, k=random.randint(min_len_name, max_len_name))) + '.' + exp

        with open(name_file, 'wb') as f:
            f.write(bytes(randint(0, 255) for _ in range(randint(min_size, max_size))))


def generate_files_with_extensions(extensions, num_files_per_extension):
    for extension, count_file in zip(extensions, num_files_per_extension):
        create_file(extension, count_file=count_file)


if __name__ == '__main__':
    extensions_list = ['txt', 'dat', 'csv']  # список расширений
    num_files_per_extension = [1, 2, 3]  # количество файлов для каждого расширения
    generate_files_with_extensions(extensions_list, num_files_per_extension)