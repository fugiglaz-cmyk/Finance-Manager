import random

transactions = []




def show_transactions():
    """Функція для перегляду всіх транзакцій
    args: None
    return: всі транзакції
    """
    global transactions
    for trans in transactions:
        print(trans)


