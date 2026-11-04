def calculate_income(transactions: list) -> float | int:
    """Функція для знаходження суми доходів
    args: транзакції
    return: сума доходів
    """
    sum_of_trans = 0
    for trans in transactions:
        if trans["type"] == "income":
            sum_of_trans += trans["amount"]
    return sum_of_trans


def calculate_expenses(transactions: list) -> float | int:
    """Функція для знаходження суми витрат
    args: транзакції
    return: сума витрат
    """
    sum_of_trans = 0
    for trans in transactions:
        if trans["type"] == "expense":
            sum_of_trans += trans["amount"]
    return sum_of_trans


