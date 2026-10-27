import re
from collections import Counter
from typing import Any, Dict, List, cast


def filter_by_state(
    transactions: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """Фильтрует список транзакций по значению ключа 'state'."""
    return [item for item in transactions if item.get("state") == state]


def sort_by_date(
    transactions: List[Dict[str, Any]], reverse: bool = True
) -> List[Dict[str, Any]]:
    """Сортирует список транзакций по ключу 'date'."""
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=reverse)


def process_bank_search(
    data: List[Dict[str, Any]], search: str
) -> List[Dict[str, Any]]:
    """Ищет транзакции, в описании которых есть заданная строка.

    Args:
        data: Список словарей с транзакциями.
        search: Строка для поиска в поле description.

    Returns:
        Список отфильтрованных транзакций.
    """
    pattern = re.compile(search, re.IGNORECASE)
    return [
        item
        for item in data
        if item.get("description") and pattern.search(item["description"])
    ]


def process_bank_operations(
    data: List[Dict[str, Any]], categories: List[str]
) -> Dict[str, int]:
    """Считает количество операций в каждой категории.

    Args:
        data: Список словарей с транзакциями.
        categories: Список категорий (строк) для подсчета.

    Returns:
        Словарь, где ключи — категории, значения — количество.
    """
    descriptions = [
        item["description"]
        for item in data
        if item.get("description") in categories
    ]
    # Добавляем cast, чтобы mypy понял, что внутри только строки
    return dict(Counter(cast(List[str], descriptions)))
