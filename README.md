# Bank Widget

Виджет для работы с банковскими операциями. Проект содержит функции для маскировки номеров карт и счетов, а также для фильтрации и сортировки транзакций.

## Установка

```bash
git clone https://github.com/Jakevirtus/bank_widget.git
cd bank_widget
poetry install   # если используется poetry

## Использование

### Фильтрация по состоянию

```python
from src.processing import filter_by_state

transactions = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2024-03-11'},
    {'id': 2, 'state': 'CANCELED', 'date': '2024-03-10'},
]
executed = filter_by_state(transactions)
print(executed)
# [{'id': 1, 'state': 'EXECUTED', 'date': '2024-03-11'}]
```

### Сортировка по дате

```python
from src.processing import sort_by_date

sorted_list = sort_by_date(transactions)  # по убыванию (новые сначала)
print(sorted_list)

sorted_asc = sort_by_date(transactions, reverse=False)  # по возрастанию


