import json
from unittest.mock import mock_open, patch

from src.utils import load_transactions


class TestLoadTransactions:
    """Тесты для функции load_transactions."""

    def test_file_not_found(self):
        """Если файл не существует, возвращается пустой список."""
        # Подменяем os.path.exists так, чтобы он всегда возвращал False (файла нет)
        with patch("os.path.exists", return_value=False):
            assert load_transactions("nonexistent.json") == []

    def test_empty_file(self):
        """Если файл пустой, возвращается пустой список."""
        # Подменяем проверку существования (True) и чтение файла (пустая строка)
        with patch("os.path.exists", return_value=True), patch(
            "builtins.open", mock_open(read_data="")
        ):
            assert load_transactions("empty.json") == []

    def test_invalid_json(self):
        """Если в файле битый JSON, возвращается пустой список."""
        with patch("os.path.exists", return_value=True), patch(
            "builtins.open", mock_open(read_data="не json")
        ):
            assert load_transactions("bad.json") == []

    def test_not_a_list(self):
        """Если JSON содержит словарь, а не список, возвращается пустой список."""
        with patch("os.path.exists", return_value=True), patch(
            "builtins.open", mock_open(read_data='{"key": "value"}')
        ):
            assert load_transactions("dict.json") == []

    def test_valid_list(self):
        """Если JSON корректный и содержит список, он успешно возвращается."""
        data = [{"id": 1}, {"id": 2}]
        with patch("os.path.exists", return_value=True), patch(
            "builtins.open", mock_open(read_data=json.dumps(data))
        ):
            assert load_transactions("valid.json") == data
