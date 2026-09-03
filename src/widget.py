from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_info: str) -> str:
    """
    Принимает строку с типом и номером карты или счета,
    возвращает строку с замаскированным номером.
    """
    parts = account_info.split()
    if len(parts) < 2:
        raise ValueError("Недостаточно данных: укажите тип и номер")

    number = parts[-1]
    name = " ".join(parts[:-1])

    if not number.isdigit():
        raise ValueError("Номер должен содержать только цифры")

    # Определяем, счёт это или карта
    if "Счет" in name or "счёт" in name:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Принимает строку с датой в формате ISO 8601,
    возвращает дату в формате ДД.ММ.ГГГГ.
    """
    from datetime import datetime
    date_obj = datetime.fromisoformat(date_string)
    return date_obj.strftime("%d.%m.%Y")
