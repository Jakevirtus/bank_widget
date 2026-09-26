import pytest

from src.masks import get_mask_account, get_mask_card_number


class TestGetMaskCardNumber:
    """Тесты для функции get_mask_card_number."""

    @pytest.mark.parametrize(
        "card_number, expected",
        [
            ("7000792289606361", "7000 79** **** 6361"),
            ("7000 7922 8960 6361", "7000 79** **** 6361"),
            ("1234567890123456", "1234 56** **** 3456"),
            ("9999888877776666", "9999 88** **** 6666"),
        ],
    )
    def test_correct_masking(self, card_number, expected):
        """Проверяет правильность маскирования для валидных номеров."""
        assert get_mask_card_number(card_number) == expected

    @pytest.mark.parametrize(
        "invalid_number",
        [
            "123456789",
            "12345678901234567",
            "",
        ],
    )
    def test_invalid_input_raises_error(self, invalid_number):
        """Проверяет, что функция выбрасывает ValueError при некорректном вводе."""
        with pytest.raises(ValueError):
            get_mask_card_number(invalid_number)


class TestGetMaskAccount:
    """Тесты для функции get_mask_account."""

    @pytest.mark.parametrize(
        "account_number, expected",
        [
            ("73654108430135874305", "**4305"),
            ("1234", "**1234"),
            ("12345678901234567890", "**7890"),
            ("9999888877776666", "**6666"),
        ],
    )
    def test_correct_masking(self, account_number, expected):
        """Проверяет правильность маскирования для валидных счетов."""
        assert get_mask_account(account_number) == expected

    @pytest.mark.parametrize(
        "invalid_number",
        [
            "123",
            "",
        ],
    )
    def test_invalid_input_raises_error(self, invalid_number):
        """Проверяет, что функция выбрасывает ValueError при некорректном вводе."""
        with pytest.raises(ValueError):
            get_mask_account(invalid_number)

