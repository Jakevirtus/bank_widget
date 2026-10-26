from unittest.mock import Mock, patch

import pytest

from src.external_api import convert_to_rub


class TestConvertToRub:
    """Тесты для функции convert_to_rub."""

    def test_rub_no_api_call(self):
        """Если валюта RUB, сумма возвращается без запроса к API."""
        transaction = {
            "operationAmount": {
                "amount": "1000.50",
                "currency": {"code": "RUB"},
            }
        }
        # Подменяем requests.get и проверяем, что он не был вызван
        with patch("src.external_api.requests.get") as mock_get:
            result = convert_to_rub(transaction)
            assert result == 1000.50
            mock_get.assert_not_called()

    @patch("src.external_api.requests.get")
    def test_usd_converts_to_rub(self, mock_get):
        """Если валюта USD, происходит запрос к API и возвращается результат."""
        # Создаем фейковый ответ от API
        mock_response = Mock()
        mock_response.json.return_value = {"result": 9000.00}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        transaction = {
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "USD"},
            }
        }
        result = convert_to_rub(transaction)
        assert result == 9000.00
        mock_get.assert_called_once()

    @patch("src.external_api.requests.get")
    def test_eur_converts_to_rub(self, mock_get):
        """Если валюта EUR, происходит запрос к API."""
        mock_response = Mock()
        mock_response.json.return_value = {"result": 10500.00}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        transaction = {
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "EUR"},
            }
        }
        result = convert_to_rub(transaction)
        assert result == 10500.00

    def test_missing_api_key_raises(self):
        """Если нет ключа в .env, выбрасывается ValueError."""
        transaction = {
            "operationAmount": {
                "amount": "100.00",
                "currency": {"code": "USD"},
            }
        }
        # Подменяем os.getenv так, чтобы он вернул None (ключа нет)
        with patch("src.external_api.os.getenv", return_value=None):
            with pytest.raises(ValueError):
                convert_to_rub(transaction)
