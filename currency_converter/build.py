import os
import py_compile

BUILD_DIR = 'bin'

files_to_compile = [
    'currency.py',
    'exchange.py',
    'converter.py',
    'main.py'
]


def build():

    if not os.path.exists(BUILD_DIR):
        os.makedirs(BUILD_DIR)
        print(f"Создана папка {BUILD_DIR}")

    print("Начало компиляции...")

    for filename in files_to_compile:
        if os.path.exists(filename):

            dest = os.path.join(BUILD_DIR, filename + 'c')

            try:
                py_compile.compile(filename, cfile=dest)
                print(f"Скомпилирован: {filename} -> {dest}")
            except Exception as e:
                print(f"Ошибка при компиляции {filename}: {e}")
        else:
            print(f"Файл {filename} не найден")

    print(f"\nСборка завершена! Файлы находятся в папке '{BUILD_DIR}'")


if __name__ == "__main__":
    build()