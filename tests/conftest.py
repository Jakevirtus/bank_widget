import pytest


@pytest.fixture
def sample_transactions():
    """Список словарей с транзакциями для тестов filter_by_state и sort_by_date."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
        {"id": 2, "state": "CANCELED", "date": "2024-03-10T12:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-12T08:30:00.000000"},
        {"id": 4, "state": "PENDING", "date": "2024-03-09T18:45:00.000000"},
        {"id": 5, "state": "EXECUTED", "date": "2024-03-12T08:30:00.000000"},
    ]


@pytest.fixture
def empty_transactions():
    """Пустой список — для проверки граничных случаев."""
    return []


@pytest.fixture
def card_numbers():
    """Набор валидных и невалидных номеров карт."""
    return {
        "valid": "7000792289606361",
        "valid_with_spaces": "7000 7922 8960 6361",
        "invalid_short": "123456789",
        "invalid_long": "12345678901234567",
        "empty": "",
    }


@pytest.fixture
def account_numbers():
    """Набор валидных и невалидных номеров счетов."""
    return {
        "valid": "73654108430135874305",
        "valid_short": "1234",
        "invalid_short": "123",
        "empty": "",
    }
