import json
import logging
import os
from typing import Any, Dict, List

# Создаем папку logs, если её нет
os.makedirs("logs", exist_ok=True)

# Создаем логгер для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Настраиваем file_handler
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(filepath: str) -> List[Dict[str, Any]]:
    """Читает JSON-файл с транзакциями."""
    logger.debug(f"Вызвана функция load_transactions с путем: {filepath}")

    if not os.path.exists(filepath):
        logger.error(f"Файл не найден по пути: {filepath}")
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError) as e:
        logger.error(f"Ошибка при чтении файла {filepath}: {e}")
        return []

    if not isinstance(data, list):
        logger.error(f"Ошибка: JSON-файл {filepath} содержит не список")
        return []

    logger.info(f"Успешно прочитан файл {filepath}. Количество транзакций: {len(data)}")
    return data
