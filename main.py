import csv
import pandas as pd
from datetime import datetime
from training_data import predict_category
from analysis import analyze_expenses
from dashboard import show_dashboard
from search import search_expenses
from budget import analyze_budget
from charts import (
    spending_by_category,
    monthly_spending_trend,
    spending_distribution
)

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

    while True:
        expense_name = input("What did you spend on? ").strip()

        if expense_name:
            break

        print("⚠️ Expense name cannot be empty.")

    while True:
        try:
            amount = float(input("How much is it? "))

            if amount <= 0:
                print("⚠️ Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("⚠️ Please enter a valid number.")

    category = predict_category(expense_name)
    print(f"🤖 Suggested category: {category.title()}")

    while True:
        date = input("Enter date (DD/MM/YYYY): ")

        try:
            datetime.strptime(date, "%d/%m/%Y")
            break

        except ValueError:
            print("⚠️ Invalid date. Please use DD/MM/YYYY.")

    expense = {
    "Name": name,
    "Item": expense_name,
    "Amount": amount,
    "Category": category,
    "Date": date
}

    expenses.append(expense)

    while True:
        another = input(
            "Add another expense? yes/no: "
        ).strip().lower()

        if another == "yes":
            break
        elif another == "no":
            break
        else:
            print("⚠️ Please enter yes or no.")

    if another == "no":
        break

# save expenses to csv
with open("expenses.csv", "a", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["Name", "Item", "Amount", "Category", "Date"]
    )

    if file.tell() == 0:
        writer.writeheader()

    writer.writerows(expenses)

# read using pandas
df = pd.read_csv("expenses.csv")

df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True
)

# Filter expenses for current user
user_df = df[
    df["Name"].str.lower() == name.lower()
].copy()

print("\n------DATA ANALYSIS-----")
print(user_df)

# Analyze user's expenses
(
    total,
    average_expense,
    highest_expense,
    category_summary,
    monthly_summary,
    highest_month,
    highest_category,
    highest_category_amount,
    highest_category_percentage
) = analyze_expenses(user_df)

# Financial Dashboard

show_dashboard(
    name,
    user_df,
    total,
    average_expense,
    highest_expense,
    highest_category,
    highest_month,
    highest_category_percentage,
    category_summary
)

# Expense Search

search_expenses(user_df)

# Monthly Budget Analysis
analyze_budget(monthly_summary)
    
# Spending Charts

spending_by_category(category_summary)

monthly_spending_trend(monthly_summary)

spending_distribution(category_summary)