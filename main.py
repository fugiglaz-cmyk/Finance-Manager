import transactions_file
import statistics

transactions = []
num = 1
actions = """========== FINANCE MANAGER ==========

1. Додати дохід
2. Додати витрату
3. Переглянути всі транзакції
4. Показати загальний дохід
5. Показати загальні витрати
6. Показати поточний баланс
7. Фільтрація за категорією
0. Вихід
"""
balance = int(input("Enter your balance: "))
print(actions)
while num != 0:
    num = int(input("Enter the action: "))
    match num:
        case 1:
            transaction_type = "income"
            amount = int(input("Enter amount you to  income: "))
            category = input("Enter category of the transaction: ")
            description = input("Enter description to the transaction: ")
            transactions_file.add_transaction(transaction_type, amount, balance, category, description)
            print("Operation done what do you want next?")
            print(actions)
            num = int(input("Enter the action: "))
        case 2:
            transaction_type = "income"
            amount = int(input("Enter amount you to  income: "))
            category = input("Enter category of the transaction: ")
            description = input("Enter description to the transaction: ")
            transactions_file.add_transaction(transaction_type, amount, balance, category, description)
            print("What do you want next?")
            print(actions)
            num = int(input("Enter the action: "))
        case 3:
            transactions_file.show_transactions()
            print("What do you want next?")
            print(actions)
            num = int(input("Enter the action: "))
        case 4:
            statistics.calculate_income(transactions)
            print("What do you want next?")
            print(actions)
            num = int(input("Enter the action: "))
        case 5:
            statistics.calculate_expenses(transactions)
            print("What do you want next?")
            print(actions)
            num = int(input("Enter the action: "))
        case 6:
            print(balance)
            print("What do you want next?")
            print(actions)
            num = int(input("Enter the action: "))
        case 7:
            category = input("Enter a category you want to search: ")
            statistics.filter_by_category(transactions, category)
            print("What do you want next?")
            print(actions)
            num = int(input("Enter the action: "))
        case 8:
            num = 0
            break
