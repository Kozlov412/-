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


def append_json(data: list[dict], file_path: str, encoding: str = "utf-8") -> None:
    """Добавляет данные в JSON файл.

    Args:
        data: Список словарей для добавления.
        file_path: Путь к JSON файлу.
        encoding: Кодировка файла.

    Raises:
        TypeError: Если data не является списком словарей.
    """
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise TypeError("Data must be a list of dictionaries")

    try:
        existing_data = read_json(file_path, encoding)
        if existing_data is None:
            existing_data = [] # Если файл не существует или пустой.

        if isinstance(existing_data, list): # Проверка existing_data
            existing_data.extend(data)

        write_json(existing_data, file_path, encoding)
    except Exception as e:
        print(f"Ошибка при добавлении JSON: {e}")

