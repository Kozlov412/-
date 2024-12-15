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

def read_csv(file_path: str, encoding: str = "utf-8", delimiter: str = ",") -> list[list[str]] | None:
    """Читает данные из CSV файла.

    Args:
        file_path: Путь к CSV файлу.
        encoding: Кодировка файла.
        delimiter: Разделитель.

    Returns:
        Список списков со строковыми значениями из CSV файла или None, если произошла ошибка.
    """
    try:
        with open(file_path, "r", encoding=encoding, newline="") as f:
            reader = csv.reader(f, delimiter=delimiter)
            return list(reader)
    except (FileNotFoundError, csv.Error) as e: # csv.Error for other csv reading errors.
        print(f"Ошибка при чтении CSV: {e}")
        return None


def write_csv(data: list[list[str]], file_path: str, encoding: str = "utf-8", delimiter: str = ",") -> None:
    """Записывает данные в CSV файл.

    Args:
        data: Данные для записи (список списков).
        file_path: Путь к CSV файлу.
        encoding: Кодировка файла.
        delimiter: Разделитель.
    """
    try:
        with open(file_path, "w", encoding=encoding, newline="") as f:
            writer = csv.writer(f, delimiter=delimiter)
            writer.writerows(data)
    except Exception as e:
        print(f"Ошибка при записи CSV: {e}")

def append_csv(data: list[list[str]], file_path: str, encoding: str = "utf-8", delimiter: str = ",") -> None:
    """Добавляет данные в CSV файл.

    Args:
        data: Список списков со строковыми значениями для добавления в CSV.
        file_path (str): Путь к CSV файлу.
        encoding (str): Кодировка файла. По умолчанию "utf-8".
        delimiter (str): Разделитель CSV. По умолчанию ",".

    """

    try:
        with open(file_path, "a", encoding=encoding, newline="") as f:
            writer = csv.writer(f, delimiter=delimiter)
            writer.writerows(data)
    except Exception as e:
        print(f"Ошибка при добавлении в CSV: {e}")



def read_txt(file_path: str, encoding: str = "utf-8") -> str | None:
    """Читает данные из текстового файла.

    Args:
        file_path: Путь к текстовому файлу.
        encoding: Кодировка файла.

    Returns:
        Строка с данными из файла или None, если произошла ошибка.
    """
    try:
        with open(file_path, "r", encoding=encoding) as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"Ошибка при чтении TXT: {e}")
        return None


def write_txt(data: str, file_path: str, encoding: str = "utf-8") -> None:
    """Записывает данные в текстовый файл.

    Args:
        data: Данные для записи (строка).
        file_path: Путь к текстовому файлу.
        encoding: Кодировка файла.
    """
    try:
        with open(file_path, "w", encoding=encoding) as f:
            f.write(data)
    except Exception as e:
        print(f"Ошибка при записи TXT: {e}")


def append_txt(data: str, file_path: str, encoding: str = "utf-8") -> None:
    """Добавляет данные в текстовый файл.

    Args:
        data: Данные для добавления.
        file_path: Путь к текстовому файлу.
        encoding: Кодировка файла.
    """
    try:
        with open(file_path, "a", encoding=encoding) as f:
            f.write(data)
    except Exception as e:
        print(f"Ошибка при добавлении TXT: {e}")