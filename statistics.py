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


def calculate_balance(transactions: list) -> float | int:
    """Функція для знаходження різниці між доходами та витратами
    args: транзакції
    return: різниця між доходами та витратами
    """
    sum_of_in = 0
    for trans in transactions:
        if trans["type"] == "income":
            sum_of_in += trans["amount"]
    sum_of_ex = 0
    for trans in transactions:
        if trans["type"] == "expense":
            sum_of_ex += trans["amount"]
    bal = sum_of_in - sum_of_ex
    return bal


def filter_by_category(transactions: list, category: str) -> list:
    """Функція для фільтрації та подальшого виводу транзакцій за категоріями
    args: transactions: список транзакцій
    category: категорія транзакцій
    return: фільтровані транзакції
    """
    for trans in transactions:
        if trans["category"] == category:
            print(trans)
