from src.utils import load_transactions
from src.csv_excel_reader import read_csv_transactions, read_excel_transactions
from src.processing import filter_by_state, sort_by_date, process_bank_search
from src.widget import get_date, mask_account_card


def format_transaction(t: dict) -> str:
    """Форматирует одну транзакцию для вывода в консоль."""
    date_str = get_date(t.get("date", ""))
    desc = t.get("description", "")

    from_acc = t.get("from", "")
    to_acc = t.get("to", "")

    # Маскируем счета/карты, если они есть
    if from_acc:
        from_acc = mask_account_card(from_acc)
    if to_acc:
        to_acc = mask_account_card(to_acc)

    amount_info = t.get("operationAmount", {})
    amount = amount_info.get("amount", "")
    currency = amount_info.get("currency", {}).get("name", "")

    # Формируем строку
    result = f"{date_str} {desc}\n"
    if from_acc and to_acc:
        result += f"{from_acc} -> {to_acc}\n"
    elif from_acc:
        result += f"{from_acc}\n"
    elif to_acc:
        result += f"{to_acc}\n"

    result += f"Сумма: {amount} {currency}"
    return result


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("> ")
    while choice not in ["1", "2", "3"]:
        print("Неверный ввод. Введите 1, 2 или 3.")
        choice = input("> ")

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        data = load_transactions("data/operations.json")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        data = read_csv_transactions("data/transactions.csv")
    else:
        print("Для обработки выбран XLSX-файл.")
        data = read_excel_transactions("data/transactions_excel.xlsx")

    # Фильтрация по статусу
    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
    status = input("> ").upper()  # Приводим к верхнему регистру

    while status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'Статус операции "{status}" недоступен.')
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input("> ").upper()

    print(f'Операции отфильтрованы по статусу "{status}"')
    data = filter_by_state(data, status)

    # Сортировка
    is_sort = input("Отсортировать операции по дате? Да/Нет\n> ").lower()
    if is_sort in ["да", "yes", "y", "д"]:
        sort_order = input("Отсортировать по возрастанию или по убыванию?\n> ").lower()
        reverse = sort_order in ["по убыванию", "убывание"]
        data = sort_by_date(data, reverse)

    # Фильтр по рублям
    is_rub = input("Выводить только рублевые транзакции? Да/Нет\n> ").lower()
    if is_rub in ["да", "yes", "y", "д"]:
        data = [
            t for t in data
            if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]

    # Поиск по слову
    is_search = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n> ").lower()
    if is_search in ["да", "yes", "y", "д"]:
        search_word = input("Введите слово для поиска:\n> ")
        data = process_bank_search(data, search_word)

    # Вывод результата
    print("Распечатываю итоговый список транзакций...")
    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(data)}\n")
        for t in data:
            print(format_transaction(t))
            print("-" * 30)


if __name__ == "__main__":
    main()
