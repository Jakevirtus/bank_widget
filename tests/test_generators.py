import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


class TestFilterByCurrency:
    """Тесты для функции filter_by_currency."""

    def test_filter_usd_transactions(self, transactions_with_currencies):
        """Проверяет фильтрацию транзакций по коду USD."""
        result = list(filter_by_currency(transactions_with_currencies, "USD"))
        assert len(result) == 3
        assert all(
            t["operationAmount"]["currency"]["code"] == "USD" for t in result
        )

    def test_filter_rub_transactions(self, transactions_with_currencies):
        """Проверяет фильтрацию транзакций по коду RUB."""
        result = list(filter_by_currency(transactions_with_currencies, "RUB"))
        assert len(result) == 2
        assert all(
            t["operationAmount"]["currency"]["code"] == "RUB" for t in result
        )

    def test_unknown_currency_returns_empty(self, transactions_with_currencies):
        """Если валюты нет в списке — итератор пустой."""
        result = list(filter_by_currency(transactions_with_currencies, "EUR"))
        assert result == []

    def test_empty_list(self):
        """Пустой список → пустой итератор."""
        assert list(filter_by_currency([], "USD")) == []

    def test_returns_iterator(self, transactions_with_currencies):
        """Проверяет, что функция возвращает итератор (можно вызвать next)."""
        result = filter_by_currency(transactions_with_currencies, "USD")
        first = next(result)
        assert first["operationAmount"]["currency"]["code"] == "USD"


class TestTransactionDescriptions:
    """Тесты для функции-генератора transaction_descriptions."""

    def test_all_descriptions(self, transactions_with_currencies):
        """Проверяет описания всех транзакций."""
        result = list(transaction_descriptions(transactions_with_currencies))
        expected = [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ]
        assert result == expected

    @pytest.mark.parametrize("count", [1, 3, 5])
    def test_first_n_descriptions(self, transactions_with_currencies, count):
        """Проверяет, что можно получить первые N описаний."""
        generator = transaction_descriptions(transactions_with_currencies)
        result = [next(generator) for _ in range(count)]
        assert len(result) == count

    def test_empty_list(self):
        """Пустой список → пустой генератор."""
        assert list(transaction_descriptions([])) == []


class TestCardNumberGenerator:
    """Тесты для генератора card_number_generator."""

    @pytest.mark.parametrize(
        "start, stop, expected",
        [
            (
                1,
                3,
                [
                    "0000 0000 0000 0001",
                    "0000 0000 0000 0002",
                    "0000 0000 0000 0003",
                ],
            ),
            (1, 1, ["0000 0000 0000 0001"]),
            (
                9999,
                10001,
                [
                    "0000 0000 0000 9999",
                    "0000 0000 0001 0000",
                    "0000 0000 0001 0001",
                ],
            ),
        ],
    )
    def test_generate_range(self, start, stop, expected):
        """Проверяет генерацию в заданном диапазоне."""
        assert list(card_number_generator(start, stop)) == expected

    def test_format(self):
        """Проверяет формат номера карты: 4 группы по 4 цифры."""
        card = next(card_number_generator(1, 1))
        assert len(card) == 19  # 16 цифр + 3 пробела
        parts = card.split(" ")
        assert len(parts) == 4
        assert all(len(part) == 4 and part.isdigit() for part in parts)

    def test_max_value(self):
        """Проверяет последнее значение диапазона."""
        card = next(card_number_generator(9999999999999999, 9999999999999999))
        assert card == "9999 9999 9999 9999"
