def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты."""
    digits = "".join(filter(str.isdigit, card_number))
    if len(digits) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр")
    masked = f"{digits[:6]}******{digits[-4:]}"
    return " ".join(masked[i : i + 4] for i in range(0, len(masked), 4))


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета."""
    digits = "".join(filter(str.isdigit, account_number))
    if len(digits) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{digits[-4:]}"
