import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """Конвертирует сумму транзакции в рубли.

    Если валюта RUB — возвращает сумму как есть.
    Для USD/EUR — делает запрос к API за курсом.

    Args:
        transaction: Словарь с данными о транзакции.

    Returns:
        Сумма в рублях (float).
    """
    amount_info = transaction.get("operationAmount", {})
    amount_str = amount_info.get("amount", "0")
    currency_info = amount_info.get("currency", {})
    currency = currency_info.get("code", "RUB")

    amount = float(amount_str)

    # Если рубли, то ничего конвертировать не нужно
    if currency == "RUB":
        return amount

    # Получаем ключ из переменных окружения
    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    if not api_key:
        raise ValueError("Не задан EXCHANGE_RATES_API_KEY в файле .env")

    # Делаем запрос к API
    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"to": "RUB", "from": currency, "amount": amount}
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()  # Вызовет ошибку, если API ответит 4xx или 5xx

    data = response.json()
    return float(data["result"])
