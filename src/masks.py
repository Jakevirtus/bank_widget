import logging
import os

# Создаем папку logs, если её нет
os.makedirs("logs", exist_ok=True)

# Создаем логгер для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Настраиваем file_handler (mode="w" означает перезапись при каждом запуске)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты."""
    logger.debug(f"Вызвана функция get_mask_card_number с аргументом: {card_number}")

    digits = "".join(filter(str.isdigit, card_number))
    if len(digits) != 16:
        logger.error(f"Ошибка: неверная длина номера карты ({len(digits)} цифр)")
        raise ValueError("Номер карты должен содержать ровно 16 цифр")

    masked = f"{digits[:6]}******{digits[-4:]}"
    result = " ".join(masked[i: i + 4] for i in range(0, len(masked), 4))

    logger.info(f"Успешно замаскирован номер карты. Результат: {result}")
    return result


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета."""
    logger.debug(f"Вызвана функция get_mask_account с аргументом: {account_number}")

    digits = "".join(filter(str.isdigit, account_number))
    if len(digits) < 4:
        logger.error(f"Ошибка: номер счета слишком короткий ({len(digits)} цифр)")
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    result = f"**{digits[-4:]}"
    logger.info(f"Успешно замаскирован номер счета. Результат: {result}")
    return result
