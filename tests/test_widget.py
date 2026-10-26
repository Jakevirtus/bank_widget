import pytest

from src.widget import get_date, mask_account_card


class TestMaskAccountCard:
    """Тесты для функции mask_account_card."""

    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
            ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
            ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
            ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
            ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
            ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
            ("Счет 73654108430135874305", "Счет **4305"),
            ("Счет 64686473678894779589", "Счет **9589"),
            ("Счет 35383033474447895560", "Счет **5560"),
        ],
    )
    def test_correct_masking_card_and_account(self, input_str, expected):
        """Проверяет распознавание типа и правильную маскировку."""
        assert mask_account_card(input_str) == expected

    @pytest.mark.parametrize(
        "invalid_input",
        [
            "",
            "Visa Platinum",
            "Visa Platinum 123",
            "Счет 123",
        ],
    )
    def test_invalid_input_raises_error(self, invalid_input):
        """Проверяет защиту от некорректного ввода."""
        with pytest.raises(ValueError):
            mask_account_card(invalid_input)


class TestGetDate:
    """Тесты для функции get_date."""

    @pytest.mark.parametrize(
        "iso_string, expected",
        [
            ("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("2024-12-31T23:59:59.999999", "31.12.2024"),
            ("2023-01-01T00:00:00.000000", "01.01.2023"),
            ("2024-03-11T02:26:18", "11.03.2024"),
            ("2024-03-11", "11.03.2024"),
            ("2025-06-15T10:00:00.000000", "15.06.2025"),
        ],
    )
    def test_correct_date_conversion(self, iso_string, expected):
        """Проверяет правильность преобразования ISO-даты."""
        assert get_date(iso_string) == expected

    def test_invalid_date_raises_error(self):
        """Проверяет, что при некорректной дате выбрасывается ValueError."""
        with pytest.raises(ValueError):
            get_date("не дата")
