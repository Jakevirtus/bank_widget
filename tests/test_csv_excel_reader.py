from unittest.mock import Mock, patch

from src.csv_excel_reader import read_csv_transactions, read_excel_transactions


class TestReadCsvTransactions:
    """Тесты для функции read_csv_transactions."""

    @patch("src.csv_excel_reader.pd.read_csv")
    def test_read_csv_success(self, mock_read_csv):
        """Успешное чтение CSV-файла."""
        mock_df = Mock()
        mock_df.to_dict.return_value = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
        mock_read_csv.return_value = mock_df

        result = read_csv_transactions("dummy.csv")

        assert len(result) == 2
        assert result[0]["id"] == 1
        mock_read_csv.assert_called_once_with("dummy.csv")

    @patch("src.csv_excel_reader.pd.read_csv")
    def test_read_csv_error(self, mock_read_csv):
        """Ошибка при чтении CSV-файла."""
        mock_read_csv.side_effect = Exception("Ошибка файла")

        result = read_csv_transactions("bad.csv")

        assert result == []


class TestReadExcelTransactions:
    """Тесты для функции read_excel_transactions."""

    @patch("src.csv_excel_reader.pd.read_excel")
    def test_read_excel_success(self, mock_read_excel):
        """Успешное чтение Excel-файла."""
        mock_df = Mock()
        mock_df.to_dict.return_value = [{"id": 3, "amount": 300}]
        mock_read_excel.return_value = mock_df

        result = read_excel_transactions("dummy.xlsx")

        assert len(result) == 1
        assert result[0]["id"] == 3
        mock_read_excel.assert_called_once_with("dummy.xlsx")

    @patch("src.csv_excel_reader.pd.read_excel")
    def test_read_excel_error(self, mock_read_excel):
        """Ошибка при чтении Excel-файла."""
        mock_read_excel.side_effect = Exception("Ошибка файла")

        result = read_excel_transactions("bad.xlsx")

        assert result == []
