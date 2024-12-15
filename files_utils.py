import json
import csv
import os
try:
    import yaml
except ImportError:
    have_yaml_support = False
else:
    have_yaml_support = True



def read_json(file_path: str, encoding: str = "utf-8") -> dict | list | None:
    """Читает данные из JSON файла.

    Args:
        file_path: Путь к JSON файлу.
        encoding: Кодировка файла.

    Returns:
        Словарь или список с данными из JSON файла, или None, если произошла ошибка.
    """
    try:
        with open(file_path, "r", encoding=encoding) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка при чтении JSON: {e}")
        return None


def write_json(data: dict | list, file_path: str, encoding: str = "utf-8") -> None:
    """Записывает данные в JSON файл.

    Args:
        data: Данные для записи (словарь или список).
        file_path: Путь к JSON файлу.
        encoding: Кодировка файла.
    """
    try:
        with open(file_path, "w", encoding=encoding) as f:
            json.dump(data, f, indent=4) # indent для красивого форматирования
    except Exception as e:
        print(f"Ошибка при записи JSON: {e}")



