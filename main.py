import transactions_file
import statistics

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

while True:
    print(actions)
    num = int(input("Enter the action: "))
    match num:
        case 1 | 2:
            transaction_type = "income" if num == 1 else "expense"
            amount = int(input("Enter amount: "))
            category = input("Enter category of the transaction: ")
            description = input("Enter description to the transaction: ")
            result = transactions_file.add_transaction(
                transaction_type, amount, balance, category, description)
            if result:
                balance = result["balance"]
                print("Operation done")
        case 3:
            transactions_file.show_transactions()
        case 4:
            print(statistics.calculate_income(transactions_file.transactions))
        case 5:
            print(statistics.calculate_expenses(transactions_file.transactions))
        case 6:
            print(balance)
        case 7:
            category = input("Enter a category you want to search: ")
            statistics.filter_by_category(transactions_file.transactions, category)
        case 0:
            break
        case _:
            print("Невідома дія")