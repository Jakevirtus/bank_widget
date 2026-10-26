import pytest

from src.processing import (
    filter_by_state,
    process_bank_operations,
    process_bank_search,
    sort_by_date,
)


class TestFilterByState:
    """Тесты для функции filter_by_state."""

    def test_default_filter_executed(self, sample_transactions):
        """Проверяет фильтрацию по умолчанию (EXECUTED)."""
        result = filter_by_state(sample_transactions)
        assert all(item["state"] == "EXECUTED" for item in result)
        assert len(result) == 3

    @pytest.mark.parametrize(
        "state, expected_count",
        [
            ("EXECUTED", 3),
            ("CANCELED", 1),
            ("PENDING", 1),
            ("UNKNOWN", 0),
        ],
    )
    def test_filter_by_various_states(self, sample_transactions, state, expected_count):
        """Параметризованная проверка фильтрации по разным статусам."""
        result = filter_by_state(sample_transactions, state)
        assert len(result) == expected_count

    def test_filter_empty_list(self, empty_transactions):
        """Проверяет работу с пустым списком."""
        assert filter_by_state(empty_transactions) == []

    def test_no_matching_state(self, sample_transactions):
        """Проверяет случай, когда нет словарей с указанным статусом."""
        result = filter_by_state(sample_transactions, "NON_EXISTENT")
        assert result == []


class TestSortByDate:
    """Тесты для функции sort_by_date."""

    def test_default_sort_descending(self, sample_transactions):
        """Проверяет сортировку по убыванию по умолчанию."""
        result = sort_by_date(sample_transactions)
        dates = [item["date"] for item in result]
        assert dates == sorted(dates, reverse=True)

    def test_sort_ascending(self, sample_transactions):
        """Проверяет сортировку по возрастанию."""
        result = sort_by_date(sample_transactions, reverse=False)
        dates = [item["date"] for item in result]
        assert dates == sorted(dates)

    def test_sort_with_equal_dates(self, sample_transactions):
        """Проверяет корректность при одинаковых датах."""
        result = sort_by_date(sample_transactions)
        assert len(result) == len(sample_transactions)

    def test_sort_empty_list(self, empty_transactions):
        """Проверяет работу с пустым списком."""
        assert sort_by_date(empty_transactions) == []

    def test_sort_does_not_modify_original(self, sample_transactions):
        """Проверяет, что исходный список не изменяется."""
        original = [item.copy() for item in sample_transactions]
        sort_by_date(sample_transactions)
        assert sample_transactions == original


class TestProcessBankSearch:
    def test_search_found(self, sample_transactions):
        result = process_bank_search(sample_transactions, "Перевод")
        assert len(result) > 0

    def test_search_not_found(self, sample_transactions):
        result = process_bank_search(sample_transactions, "НетТакогоСлова")
        assert result == []


class TestProcessBankOperations:
    def test_count_operations(self, sample_transactions):
        categories = ["Перевод организации", "Перевод со счета на счет"]
        result = process_bank_operations(sample_transactions, categories)
        assert "Перевод организации" in result
