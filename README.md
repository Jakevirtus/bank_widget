# Bank Widget

Виджет для работы с банковскими операциями. Проект содержит функции для маскировки номеров карт и счетов, фильтрации и сортировки транзакций, работы с генераторами, логирования, чтения данных из различных форматов (JSON, CSV, Excel), конвертации валют и консольный интерфейс для взаимодействия с пользователем.

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

print(get_date("2024-03-11T02:26:18.671407"))
# 11.03.2024
```

### Фильтрация, сортировка и поиск
Модуль `processing` содержит функции для работы со списками транзакций:

```python
from src.processing import filter_by_state, sort_by_date, process_bank_search, process_bank_operations

transactions = [
    {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:18.671407", "description": "Перевод"},
    {"id": 2, "state": "CANCELED", "date": "2024-03-10T12:00:00.000000", "description": "Оплата"},
]

# Фильтрация по статусу
executed = filter_by_state(transactions)

# Сортировка по дате (по убыванию)
sorted_list = sort_by_date(transactions)

# Поиск по слову в описании (с помощью регулярных выражений)
found = process_bank_search(transactions, "перевод")

# Подсчет операций по категориям (использует Counter)
categories = ["Перевод", "Оплата"]
stats = process_bank_operations(transactions, categories)
```

### Модуль generators
Инструменты для работы с большими объёмами данных:

```python
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Итератор транзакций по валюте
usd_transactions = filter_by_currency(transactions, "USD")

# Генератор описаний
descriptions = transaction_descriptions(transactions)

# Генератор номеров карт
for card_number in card_number_generator(1, 5):
    print(card_number)
    # 0000 0000 0000 0001 ...
```

### Модуль decorators
Декоратор `log` для автоматического логирования вызовов функций:

```python
from src.decorators import log

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y
```

### Модуль utils и external_api
Чтение JSON и конвертация валют:

```python
from src.utils import load_transactions
from src.external_api import convert_to_rub

# Чтение JSON
transactions = load_transactions("data/operations.json")

# Конвертация в рубли (для USD/EUR используется API apilayer)
transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}
rub_amount = convert_to_rub(transaction)
```

> Для работы `external_api` создайте файл `.env` в корне проекта:
> `EXCHANGE_RATES_API_KEY=your_api_key_here`
> Шаблон находится в `.env.example`.

### Модуль csv_excel_reader
Чтение данных из табличных форматов с помощью `pandas`:

```python
from src.csv_excel_reader import read_csv_transactions, read_excel_transactions

csv_data = read_csv_transactions("data/transactions.csv")
excel_data = read_excel_transactions("data/transactions_excel.xlsx")
```

## Интерфейс командной строки (CLI)

В модуле `src/main.py` реализован консольный интерфейс для взаимодействия с пользователем.

Программа позволяет:
1. Выбрать источник данных (JSON, CSV или XLSX).
2. Отфильтровать операции по статусу (EXECUTED, CANCELED, PENDING).
3. Отсортировать по дате.
4. Отфильтровать только рублевые транзакции.
5. Найти операции по ключевому слову в описании.

Для запуска программы:

```bash
python -m src.main
```

## Логирование

В модулях настроено логирование с использованием стандартной библиотеки `logging`.
- Логи записываются в папку `logs/` в файлы `masks.log`, `utils.log`, `csv_excel_reader.log`.
- Формат записи: метка времени, имя модуля, уровень важности, сообщение.
- Файлы логов перезаписываются при каждом запуске приложения.
- Папка `logs/` и файлы `*.log` исключены из Git (добавлены в `.gitignore`).

## Тестирование

Проект покрыт тестами с использованием `pytest` и `unittest.mock`.

### Запуск тестов

```bash
pytest
```

### Отчёт о покрытии

После запуска тестов создаётся HTML-отчёт в папке `htmlcov/`.
Откройте `htmlcov/index.html` в браузере для просмотра детального отчёта.

Текущее покрытие — **100%** по всем модулям (87 тестов).

## Лицензия

Проект создан в учебных целях.