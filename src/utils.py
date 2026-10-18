import json
import os
from typing import Any, Dict, List


def load_transactions(filepath: str) -> List[Dict[str, Any]]:
    """Читает JSON-файл с транзакциями.

    Args:
        filepath: Путь к JSON-файлу.

    Returns:
        Список словарей с транзакциями.
        Пустой список, если файл не найден, пуст, или содержит не список.
    """
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

    if not isinstance(data, list):
        return []

    return data
