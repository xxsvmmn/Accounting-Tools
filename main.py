from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime
from analysis_module import calculate_total_expenses
import clear_expense as clr
from chart_generator import generate_pie_chart

app = Flask(__name__)

def load_expenses():
    try:
        with open('expenses.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            print("type from  DictReader is: ", type(reader))
            # A quick way to write
            # expenses = list(reader)
            expenses  = []
            for row in reader:
                expenses.append(row)
            print(f"expense list{expenses}")
        return expenses
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open('expenses.csv', 'w', newline='') as file:
        fieldnames = ['date', 'category', 'description', 'amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        print(f"expense list for write {expenses}")
        # a quick way to write
        # writer.writerows(expenses)
        for row in expenses:
            writer.writerow(row)

@app.route('/')
def home():
    expenses = load_expenses()
    return render_template('home.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        description = request.form['description']
        amount = float(request.form['amount'])

        expense = {
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        }

        expenses = load_expenses()
        expenses.append(expense)
        save_expenses(expenses)

        return redirect(url_for('home'))

    return render_template('add_expense.html')

@app.route('/analysis')
def analysis():
    expenses = load_expenses()
    total_expenses = calculate_total_expenses(expenses)  
    categories = [expense['category'] for expense in expenses]
    amounts = [expense['amount'] for expense in expenses]

    pie_chart = generate_pie_chart(categories, amounts)

    return render_template('analysis.html', total_expenses=total_expenses, img_base64=pie_chart)

@app.route('/clear-expenses',methods=['POST','GET'])
def clear_expenses_route():
    clr.clear_expenses() 
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=8000)

