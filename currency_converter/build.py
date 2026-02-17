import os
import py_compile
# Глобальные константы
BUILD_DIR = 'bin'  # Директория для скомпилированных файлов

files_to_compile = [
    'currency.py',
    'exchange.py',
    'converter.py',
    'main.py'
]

def build():
    """
    Выполняет процесс сборки проекта: создает целевую директорию и компилирует 
    указанные Python-файлы в байт-код (.pyc).

    Процесс включает:
    1. Проверку/создание папки 'bin'.
    2. Проверку наличия исходных файлов.
    3. Компиляцию каждого файла с помощью модуля py_compile.
    4. Обработку возможных исключений в процессе сборки.
    """
    # Создание директории для сборки, если она отсутствует
    if not os.path.exists(BUILD_DIR):
        os.makedirs(BUILD_DIR)
        print(f"Создана папка {BUILD_DIR}")

    print("Начало компиляции...")

    for filename in files_to_compile:
        if os.path.exists(filename):
            # Формирование пути назначения (например, bin/main.pyc)
            dest = os.path.join(BUILD_DIR, filename + 'c')

            try:
                # Компиляция исходного кода в байт-код
                py_compile.compile(filename, cfile=dest)
                print(f"Скомпилирован: {filename} -> {dest}")
            except Exception as e:
                print(f"Ошибка при компиляции {filename}: {e}")
        else:
            print(f"Файл {filename} не найден")

    print(f"\nСборка завершена! Файлы находятся в папке '{BUILD_DIR}'")


if __name__ == "__main__":
    """
    Точка входа в скрипт сборки. 
    Запускает функцию build() при прямом запуске файла.
    """
    build()
