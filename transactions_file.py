import random

transactions = []

def delete_transaction():
    """Функція для видалення транзакції
    args: None
    return: None
    """
    delete = int(input("Enter id of transaction to delete: "))
    global transactions
    for trans in transactions:
        if trans["id"] == delete:
            transactions.remove(trans)
            break
