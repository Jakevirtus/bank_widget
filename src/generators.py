from typing import Any, Dict, Iterator, List


def filter_by_currency(
    transactions: List[Dict[str, Any]], currency_code: str
) -> Iterator[Dict[str, Any]]:
    """Возвращает итератор транзакций с заданным кодом валюты."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Поочерёдно возвращает описания транзакций."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера банковских карт в заданном диапазоне."""
    for number in range(start, stop + 1):
        card = f"{number:016d}"
        yield f"{card[:4]} {card[4:8]} {card[8:12]} {card[12:]}"
