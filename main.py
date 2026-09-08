from src.widget import mask_account_card, get_date

if __name__ == "__main__":
    # Примеры для карт
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("MasterCard 7158300734726758"))

    # Примеры для счетов
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Счет 64686473678894779589"))

    # Пример даты
    print(get_date("2024-03-11T02:26:18.671407"))
