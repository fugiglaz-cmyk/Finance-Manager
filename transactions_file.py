import random

transactions = []


def add_transaction(transaction_type: str, amount: int | float, balance: int | float, category: str,
                    description: str) -> dict:
    """Функція для операції знімання та додавання грошей
    args: transaction_type: пишемо хочемо зняти чи покласти гроші на баланс
    amount_of_transaction: сума з якою будемо проводити маніпуляції
    balance: баланс
    category: категорія операції
    description: коментарі з метою, за що і т.д.
    return: повний чек у вигляді словника або те що баланс менше нуля та операція не проходить
    """
    ID = random.randint(1, 100000)
    global transactions
    if transaction_type == 'income':
        final_balance = amount + balance
        if final_balance >= 0:
            transaction_data = {
                "id": ID,
                "type": transaction_type,
                "balance": final_balance,
                "category": category,
                "description": description,
            }
            transactions.append(transaction_data)
            return {"id": ID, "type": transaction_type, "balance": final_balance, "category": category,
                    "description": description}
    elif transaction_type == 'expense':
        final_balance = balance - amount
        if final_balance > 0:
            transaction_data = {
                "id": ID,
                "type": transaction_type,
                "balance": final_balance,
                "category": category,
                "description": description,
            }
            transactions.append(transaction_data)
            return {"id": ID, "type": transaction_type, "balance": final_balance, "category": category,
                    "description": description}, print("Operation done")
        else:
            return f"id: {ID} Your balance is under zero: {final_balance} operation can`t be done"


def show_transactions():
    """Функція для перегляду всіх транзакцій
    args: None
    return: всі транзакції
    """
    global transactions
    for trans in transactions:
       print(trans)


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


