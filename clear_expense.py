import os
def clear_expenses():
    try:
        os.remove('expenses.csv')
        return True
    except FileNotFoundError:
        return False