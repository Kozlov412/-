import unittest
import os
import json
import csv

try:
    import yaml
except ImportError:
    have_yaml_support = False
else:
    have_yaml_support = True

from files_utils import *


class TestFileUtils(unittest.TestCase):
    """ Набор тестов для функций работы с файлами."""

    def test_read_json_success(self):
        """Тест успешного чтения JSON файла."""
        data = {"name": "Vadim", "age": 34}
        file_path = "test.json"
        write_json(data, file_path)# Записываем данные 
        read_data = read_json(file_path)# Читаем данные  
        self.assertEqual(data, read_data)  # Сравниваем записанные и прочитанные данные
        os.remove(file_path)

    def test_read_json_filenotfound(self):
        """Тест чтения несуществующего JSON файла."""
        self.assertIsNone(read_json("nonexistent_file.json"))

    def test_read_json_invalid_json(self):
        """Тест чтения файла с некорректным JSON."""
        with open("invalid.json", "w", encoding="utf-8") as f:
            f.write("invalid json")  # Записываем некорректный JSON
        self.assertIsNone(read_json("invalid.json"))
        os.remove("invalid.json")

    def test_write_json_success(self):
        """Тест успешной записи JSON файла."""
        data = {"name": "Vadim", "age": 34}
        file_path = "test.json"
        write_json(data, file_path)  # Записываем данные
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)

    def test_append_json_success(self):
        """Тест добавления данных в существующий JSON файл."""
        file_path = "test.json"
        initial_data = [{"a": 1}, {"b": 2}]
        write_json(initial_data, file_path)  # Создаем файл с начальными данными

        append_data = [{"c": 3}]
        append_json(append_data, file_path)  # Добавляем данные

        expected_data = [{"a": 1}, {"b": 2}, {"c": 3}]  # Ожидаемый результат
        read_data = read_json(file_path)  # Читаем данные из файла
        self.assertEqual(read_data, expected_data)  # Сравниваем с ожидаемым результатом
        os.remove(file_path)

    def test_append_json_new_file(self):
        """Тест добавления данных в новый JSON файл."""
        file_path = "test_new.json"
        append_data = [{"c": 3}]
        append_json(append_data, file_path)
        read_data = read_json(file_path)
        self.assertEqual(read_data, append_data)  # Проверяем результат
        os.remove(file_path)

    def test_append_json_invalid_input(self):
        """Тест обработки исключения TypeError при некорректном вводе в append_json."""
        with self.assertRaises(
            TypeError
        ):  # Ожидаем TypeError, если входные данные не являются списком
            append_json({"key": "value"}, "test.json")

    def test_csv_success(self):
        """Тест успешной работы с CSV файлом (чтение и запись)."""
        data = [["Name", "Age"], ["Alice", "25"], ["Bob", "30"]]
        file_path = "test.csv"
        write_csv(data, file_path)  # Записываем данные в CSV
        read_data = read_csv(file_path)  # Читаем данные из CSV
        self.assertEqual(data, read_data)  # Сравниваем данные
        os.remove(file_path)

    def test_csv_encoding_delimiter(self):
        """Тест работы с CSV файлом с указанием кодировки и разделителя."""
        data = [
            ["Имя", "Возраст"],
            ["Аврора", "20"],
            ["Борис", "30"],
        ]  # Кириллица для теста кодировки
        file_path = "test_encoding.csv"
        write_csv(data, file_path, encoding="utf-8", delimiter=",")
        read_data = read_csv(file_path, encoding="utf-8", delimiter=",")
        self.assertEqual(
            data, read_data
        )  # Проверяем корректность чтения с заданными параметрами
        os.remove(file_path)

    def test_append_csv_success(self):
        """Тест добавления данных в CSV файл."""
        data = [["Name", "Age"], ["Alice", "25"], ["Bob", "30"]]
        append_data = [["Charlie", "35"]]
        file_path = "test.csv"
        write_csv(data, file_path)  # Записываем начальные данные
        append_csv(append_data, file_path)  # Добавляем данные
        read_appended_data = read_csv(file_path)  # Читаем все данные
        self.assertEqual(read_appended_data, data + append_data)  # Проверяем результат

        os.remove(file_path)

    def test_txt_success(self):
        """Тест успешной работы с TXT файлом (чтение и запись)."""
        data = "Test string"
        file_path = "test.txt"
        write_txt(data, file_path)  # Записываем строку в файл
        read_data = read_txt(file_path)  # Читаем строку из файла
        self.assertEqual(data, read_data)  # Сравниваем строки
        os.remove(file_path)

    def test_txt_encoding(self):
        """Тест работы с TXT файлом с указанием кодировки UTF-8."""
        data = "Тестовая строка"  # Текст с кириллицей для проверки кодировки
        file_path = "test_encoding.txt"
        write_txt(data, file_path, encoding="utf-8")  # Запись с кодировкой
        read_data = read_txt(file_path, encoding="utf-8")  # Чтение с кодировкой
        self.assertEqual(data, read_data)  # Проверка корректности
        os.remove(file_path)

    def test_append_txt_success(self):
        """Тест добавления текста в TXT файл."""
        data = "Test string"
        append_data = "\nAppended string"  # Добавляем новую строку с переносом
        file_path = "test.txt"
        write_txt(data, file_path)  # Записываем начальный текст
        append_txt(append_data, file_path)  # Добавляем текст
        read_appended_data = read_txt(file_path)  # Читаем весь текст
        self.assertEqual(read_appended_data, data + append_data)  # Проверяем результат
        os.remove(file_path)

    @unittest.skipUnless(have_yaml_support, "PyYAML не установлен")
    def test_yaml_success(self):
        """Тест успешного чтения YAML файла."""
        yaml_data = """
        location: Penza
        units: metric
        api_key: YOUR_API_KEY
        features:
            - temperature
            - wind
            - precipitation
        """
        file_path = "test.yaml"  # Путь к файлу в тестовой директории
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(yaml_data)

        expected_data = {  # Ожидаемый результат после чтения YAML файла
            "location": "Penza",
            "units": "metric",
            "api_key": "YOUR_API_KEY",
            "features": ["temperature", "wind", "precipitation"],
        }

        read_data = read_yaml(file_path)  # Читаем данные из YAML файла
        self.assertEqual(
            read_data, expected_data
        )  # Сравниваем прочитанные данные с ожидаемым результатом
        os.remove(file_path)

    @unittest.skipUnless(have_yaml_support, "PyYAML не установлен")
    def test_yaml_filenotfound(self):
        """Тест чтения несуществующего YAML файла."""
        self.assertIsNone(read_yaml("nonexistent_file.yaml"))


if __name__ == "__main__":
    unittest.main(verbosity=2)  # Запускаем тесты, если скрипт выполняется напрямую
