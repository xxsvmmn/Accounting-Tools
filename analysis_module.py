def calculate_total_expenses(expenses):
    total_expenses = 0
    for expense in expenses:
        total_expenses += float(expense['amount'])  # Convert from string
    return total_expenses