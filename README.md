# Bank Widget

Виджет для работы с банковскими операциями. Проект содержит функции для маскировки номеров карт и счетов, фильтрации и сортировки транзакций, а также инструменты для работы с большими объёмами данных через генераторы.

## Требования

- Python 3.13 или выше
- [Poetry](https://python-poetry.org/) (для управления зависимостями)

## Установка

```bash
git clone https://github.com/Jakevirtus/bank_widget.git
cd bank_widget
poetry install
```

## Использование

### Маскировка карт и счетов

Модуль `masks` содержит функции для маскировки номеров:

```python
from src.masks import get_mask_card_number, get_mask_account

print(get_mask_card_number("7000792289606361"))
# 7000 79** **** 6361

print(get_mask_account("73654108430135874305"))
# **4305
```

### Работа с типом карты/счёта и датой

Модуль `widget` распознаёт тип (карта или счёт) и преобразует даты:

```python
from src.widget import mask_account_card, get_date

print(mask_account_card("Visa Platinum 7000792289606361"))
# Visa Platinum 7000 79** **** 6361

print(mask_account_card("Счет 73654108430135874305"))
# Счет **4305

print(get_date("2024-03-11T02:26:18.671407"))
# 11.03.2024
```

### Фильтрация и сортировка транзакций

Модуль `processing` содержит функции для работы со списками транзакций:

```python
from src.processing import filter_by_state, sort_by_date

transactions = [
    {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
    {"id": 2, "state": "CANCELED", "date": "2024-03-10T12:00:00.000000"},
]

# Фильтрация по статусу (по умолчанию 'EXECUTED')
executed = filter_by_state(transactions)
print(executed)

# Сортировка по дате (по умолчанию по убыванию)
sorted_list = sort_by_date(transactions)
print(sorted_list)

# Сортировка по возрастанию
sorted_asc = sort_by_date(transactions, reverse=False)
print(sorted_asc)
```

## Модуль generators

Модуль содержит инструменты для работы с большими объёмами транзакций через генераторы.

### filter_by_currency

Возвращает итератор транзакций с заданным кодом валюты.

```python
from src.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
```

### transaction_descriptions

Поочерёдно возвращает описания транзакций.

```python
from src.generators import transaction_descriptions

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
```

### card_number_generator

Генерирует номера карт в формате `XXXX XXXX XXXX XXXX` в заданном диапазоне.

```python
from src.generators import card_number_generator

for card_number in card_number_generator(1, 5):
    print(card_number)
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003
# 0000 0000 0000 0004
# 0000 0000 0000 0005
```

## Тестирование

Проект покрыт тестами с использованием `pytest`.

### Запуск тестов

```bash
pytest
```

### Отчёт о покрытии

После запуска тестов создаётся HTML-отчёт в папке `htmlcov/`.
Откройте `htmlcov/index.html` в браузере для просмотра детального отчёта.

Текущее покрытие — **100%** по всем модулям.

## Лицензия

Проект создан в учебных целях.# Bank Widget

Виджет для работы с банковскими операциями. Проект содержит функции для маскировки номеров карт и счетов, фильтрации и сортировки транзакций, а также инструменты для работы с большими объёмами данных через генераторы.

## Требования

- Python 3.13 или выше
- [Poetry](https://python-poetry.org/) (для управления зависимостями)

## Установка

```bash
git clone https://github.com/Jakevirtus/bank_widget.git
cd bank_widget
poetry install
```

## Использование

### Маскировка карт и счетов

Модуль `masks` содержит функции для маскировки номеров:

```python
from src.masks import get_mask_card_number, get_mask_account

print(get_mask_card_number("7000792289606361"))
# 7000 79** **** 6361

print(get_mask_account("73654108430135874305"))
# **4305
```

### Работа с типом карты/счёта и датой

Модуль `widget` распознаёт тип (карта или счёт) и преобразует даты:

```python
from src.widget import mask_account_card, get_date

print(mask_account_card("Visa Platinum 7000792289606361"))
# Visa Platinum 7000 79** **** 6361

print(mask_account_card("Счет 73654108430135874305"))
# Счет **4305

print(get_date("2024-03-11T02:26:18.671407"))
# 11.03.2024
```

### Фильтрация и сортировка транзакций

Модуль `processing` содержит функции для работы со списками транзакций:

```python
from src.processing import filter_by_state, sort_by_date

transactions = [
    {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
    {"id": 2, "state": "CANCELED", "date": "2024-03-10T12:00:00.000000"},
]

# Фильтрация по статусу (по умолчанию 'EXECUTED')
executed = filter_by_state(transactions)
print(executed)

# Сортировка по дате (по умолчанию по убыванию)
sorted_list = sort_by_date(transactions)
print(sorted_list)

# Сортировка по возрастанию
sorted_asc = sort_by_date(transactions, reverse=False)
print(sorted_asc)
```

## Модуль generators

Модуль содержит инструменты для работы с большими объёмами транзакций через генераторы.

### filter_by_currency

Возвращает итератор транзакций с заданным кодом валюты.

```python
from src.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
```

### transaction_descriptions

Поочерёдно возвращает описания транзакций.

```python
from src.generators import transaction_descriptions

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))
```

### card_number_generator

Генерирует номера карт в формате `XXXX XXXX XXXX XXXX` в заданном диапазоне.

```python
from src.generators import card_number_generator

for card_number in card_number_generator(1, 5):
    print(card_number)
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003
# 0000 0000 0000 0004
# 0000 0000 0000 0005
```

## Тестирование

Проект покрыт тестами с использованием `pytest`.

### Запуск тестов

```bash
pytest
```

### Отчёт о покрытии

После запуска тестов создаётся HTML-отчёт в папке `htmlcov/`.
Откройте `htmlcov/index.html` в браузере для просмотра детального отчёта.

Текущее покрытие — **100%** по всем модулям.

## Лицензия

Проект создан в учебных целях.