from typing import List, Dict, Any

def filter_by_state(transactions: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Фильтрует список транзакций по значению ключа 'state'.

    Args:
        transactions: Список словарей с данными о транзакциях.
        state: Значение для фильтрации (по умолчанию 'EXECUTED').

    Returns:
        Новый список словарей, у которых ключ 'state' равен указанному значению.
    """
    return [item for item in transactions if item.get('state') == state]

def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список транзакций по ключу 'date'.

    Args:
        transactions: Список словарей с данными о транзакциях.
        reverse: Если True, сортировка по убыванию (новые сначала).

    Returns:
        Новый отсортированный список.
    """
    return sorted(transactions, key=lambda x: x.get('date', ''), reverse=reverse)
