"""
    ---Task 4---
2.Напишите функцию группового переименования файлов. Она должна:
* -- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
* -- принимать параметр количество цифр в порядковом номере.
* -- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
* -- принимать параметр расширение конечного файла.
* -- принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

"""
import os


def rename_files_with_numbers(desired_name, folder_path, num_digits, source_ext, target_ext, name_range=None):
    counter = 1
    files = os.listdir(folder_path)

    for filename in files:
        old_file_path = os.path.join(folder_path, filename)

        # Пропускаем папки, файлы с неправильным расширением и файлы, которые уже начинаются с желаемого имени
        if not os.path.isfile(old_file_path) or not filename.endswith(source_ext) or filename.startswith(desired_name):
            continue

        # базовое имя файла
        base_name, file_ext = os.path.splitext(filename)

        # Получаем часть имени файла из диапазона, если параметр передан
        if name_range is not None:
            start, end = name_range
            base_name = base_name[start - 1:end]

        # Создаем новое имя с добавлением желаемого конечного имени, если указано
        new_name = f"{desired_name}_{base_name}_{str(counter).zfill(num_digits)}.{target_ext}" if desired_name else f"{base_name}_{str(counter).zfill(num_digits)}.{target_ext}"
        counter += 1

        # Формируем полный путь для нового файла
        new_file_path = os.path.join(folder_path, new_name)

        # Переименовываем файл
        try:
            os.rename(old_file_path, new_file_path)
        except Exception as e:
            print(f"Error renaming {old_file_path}: {e}")


if __name__ == "__main__":
    # Параметры для функции
    desired_name = "new_file"
    folder_path = "files"
    num_digits = 3
    source_ext = ".txt"
    target_ext = "csv"
    name_range = [3, 6]
    # для генерации тестовых файлов используйте task2.py
    rename_files_with_numbers(desired_name, folder_path, num_digits, source_ext, target_ext, name_range)
