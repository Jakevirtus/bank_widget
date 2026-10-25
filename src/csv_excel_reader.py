import logging
import os
from typing import Any, Dict, List, cast  # <--- Добавили cast сюда

import pandas as pd

# Настраиваем логирование
os.makedirs("logs", exist_ok=True)
logger = logging.getLogger("csv_excel_reader")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/csv_excel_reader.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_csv_transactions(filepath: str) -> List[Dict[str, Any]]:
    """Читает финансовые операции из CSV-файла.

    Args:
        filepath: Путь к файлу CSV.

    Returns:
        Список словарей с транзакциями.
    """
    logger.debug(f"Вызвана функция read_csv_transactions с путем: {filepath}")
    try:
        df = pd.read_csv(filepath)
        # Оборачиваем в cast (строка 32)
        result = cast(List[Dict[str, Any]], df.to_dict(orient="records"))
        logger.info(f"Успешно прочитан CSV-файл. Количество транзакций: {len(result)}")
        return result
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV-файла {filepath}: {e}")
        return []


def read_excel_transactions(filepath: str) -> List[Dict[str, Any]]:
    """Читает финансовые операции из Excel-файла.

    Args:
        filepath: Путь к файлу Excel (.xlsx).

    Returns:
        Список словарей с транзакциями.
    """
    logger.debug(f"Вызвана функция read_excel_transactions с путем: {filepath}")
    try:
        df = pd.read_excel(filepath)
        # Оборачиваем в cast (строка 52)
        result = cast(List[Dict[str, Any]], df.to_dict(orient="records"))
        logger.info(f"Успешно прочитан Excel-файл. Количество транзакций: {len(result)}")
        return result
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel-файла {filepath}: {e}")
        return []
