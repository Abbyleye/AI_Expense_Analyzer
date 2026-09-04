import matplotlib.pyplot as plt
import csv
import pandas as pd
from training_data import predict_category

print("-----------------")
print("AI Expense Analyzer")
print("-----------------")

name = input("What is your name? ")

print(f"\n Welcome, {name}!")
print("Let's start tracking your Expenses.")

# expense_name = input("What did you spend money on? ")
# amount = float(input("How much did you spend? #"))
# category = input("What is the category? ")
# date = input("Enter date: ")

# print(f"\n-------Expense Recorded-------")
# print(f"Item: {expense_name}")
# print(f"Value: #{amount}")
# print(f"Category: {category}")
# print(f"Date: {date}")

expenses = []

while True:

    expense_name = input("What did you spend on? ")
    amount = float(input("How much is it? "))

    category = predict_category(expense_name)
    print(f"🤖Suggested category: {category.title()}")
    date = input("Enter date: ")

    expense = {
        "Item": expense_name,
        "Amount": amount,
        "Category": category,
        "Date": date
    }

    expenses.append(expense)

    another = input("Add another expense? yes/no: ")

    if another.lower() == "no":
        break

# save expenses to csv
with open("expenses.csv", "w", newline = "") as file:
    writer = csv.DictWriter(
        file,
        fieldnames = ["Item", "Amount", "Category", "Date"]
    )
    writer.writeheader()
    writer.writerows(expenses)

# read using pandas
df = pd.read_csv("expenses.csv")
print("\n------DATA ANALYSIS-----")
print(df)

print(f"\n------Pandas Analysis------")
print(f"Total spending: ₦{df['Amount'].sum():,.2f}")
print(f"Average spending: ₦{df['Amount'].mean():,.2f}")
print(f"Highest spending: ₦{df['Amount'].max():,.2f}")
print(f"Number of expenses: {len(df)}")

category_summary = df.groupby("Category")["Amount"].sum()
print("\n-----Category Analysis-----")
print(category_summary)

# Your analysis starts here
total = 0
for expense in expenses:
    total = total + expense["Amount"]

categories = {}
for expense in expenses:
    category = expense["Category"]
    amount = expense["Amount"]

    if category in categories:
        categories[category] = categories[category] + amount
    else:
        categories[category] = amount
print("\n--Spending by Category--")
for category, amount in categories.items():
    print(f"{category.title()}: ₦{amount:,.2f}")

highest_expense = max(expenses, key=lambda expense: expense["Amount"])
average_expense = total / len(expenses)

print("\n---Spending Insights---")
print(f"Highest Expense: {highest_expense['Item']} - ₦{highest_expense['Amount']:,.2f}")
print(f"Average Expense: ₦{average_expense:,.2f}")

print("\n---------- Expense Summary---------")
print(f"Total Expenses: ₦{total:,.2f}")

# create spreading chart
plt.bar(category_summary.index, category_summary.values)
plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount (₦)")
plt.show()

# create piechart
plt.figure()
plt.pie(
    category_summary.values,
    labels = category_summary.index,
    autopct="%.1f%%"
)
plt.title("Spending Distribution by Category")
plt.show()