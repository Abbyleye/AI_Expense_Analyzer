import csv
import os
import pandas as pd
from datetime import datetime

from training_data import predict_category
from analysis import analyze_expenses
from dashboard import show_dashboard
from search import search_expenses
from budget import analyze_budget
from charts import show_all_charts


DATA_FILE = "expenses.csv"


# Create CSV file if it does not exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Name",
                "Item",
                "Amount",
                "Category",
                "Date"
            ]
        )
        writer.writeheader()


print("-----------------")
print("AI Expense Analyzer")
print("-----------------")


name = input("What is your name? ")

print(f"\nWelcome, {name}!")
print("Let's start tracking your Expenses.")


expenses = []


while True:

    print("\n========== MAIN MENU ==========")
    print("1. Add Expense")
    print("2. View Dashboard")
    print("3. Search Expenses")
    print("4. Analyze Budget")
    print("5. View Charts")
    print("6. Exit")

    choice = input("\nChoose an option: ").strip()


    # ==============================
    # 1. ADD EXPENSE
    # ==============================

    if choice == "1":

        while True:

            # Get expense name
            while True:

                expense_name = input(
                    "What did you spend on? "
                ).strip()

                if expense_name:
                    break

                print(
                    "⚠️ Expense name cannot be empty."
                )


            # Get amount
            while True:

                try:

                    amount = float(
                        input("How much is it? ")
                    )

                    if amount <= 0:

                        print(
                            "⚠️ Amount must be greater than 0."
                        )

                        continue

                    break

                except ValueError:

                    print(
                        "⚠️ Please enter a valid number."
                    )


            # Predict category using AI
            category = predict_category(
                expense_name
            )

            print(
                f"🤖 Suggested category: "
                f"{category.title()}"
            )


            # Confirm AI category
            while True:

                confirm_category = input(
                    "Is this category correct? yes/no: "
                ).strip().lower()


                if confirm_category == "yes":

                    break


                elif confirm_category == "no":

                    print(
                        "\nChoose the correct category:"
                    )

                    print("1. Food")
                    print("2. Transport")
                    print("3. Clothing")
                    print("4. Education")
                    print("5. Airtime")
                    print("6. Giving")


                    while True:

                        category_choice = input(
                            "Enter your choice (1-6): "
                        ).strip()


                        category_map = {
                            "1": "food",
                            "2": "transport",
                            "3": "clothing",
                            "4": "education",
                            "5": "airtime",
                            "6": "giving"
                        }


                        if category_choice in category_map:

                            category = category_map[
                                category_choice
                            ]

                            break


                        print(
                            "⚠️ Invalid choice. "
                            "Please choose a number from 1-6."
                        )


                    break


                else:

                    print(
                        "⚠️ Please enter yes or no."
                    )


            # Get date
            while True:

                date = input(
                    "Enter date (DD/MM/YYYY): "
                ).strip()


                try:

                    datetime.strptime(
                        date,
                        "%d/%m/%Y"
                    )

                    break


                except ValueError:

                    print(
                        "⚠️ Invalid date. "
                        "Please use DD/MM/YYYY."
                    )


            # Create expense record
            expense = {
                "Name": name,
                "Item": expense_name,
                "Amount": amount,
                "Category": category,
                "Date": date
            }


            expenses.append(expense)


            # Save expense immediately
            with open(
                DATA_FILE,
                "a",
                newline=""
            ) as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=[
                        "Name",
                        "Item",
                        "Amount",
                        "Category",
                        "Date"
                    ]
                )


                if file.tell() == 0:

                    writer.writeheader()


                writer.writerow(expense)


            # Ask whether to add another expense
            while True:

                another = input(
                    "Add another expense? yes/no: "
                ).strip().lower()


                if another == "yes":

                    break


                if another == "no":

                    break


                print(
                    "⚠️ Please enter yes or no."
                )


            if another == "no":

                break


    # ==============================
    # 2. VIEW DASHBOARD
    # ==============================

    elif choice == "2":

        print(
            "\nLoading your financial dashboard..."
        )


        df = pd.read_csv(DATA_FILE)


        df["Date"] = pd.to_datetime(
            df["Date"],
            dayfirst=True
        )


        user_df = df[
            df["Name"].str.lower() == name.lower()
        ].copy()


        if user_df.empty:

            print(
                f"\nℹ️ No expenses found for {name}."
            )

            print(
                "Add your first expense to see "
                "your financial dashboard."
            )

            continue


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


    # ==============================
    # 3. SEARCH EXPENSES
    # ==============================

    elif choice == "3":

        print(
            "\nLoading your expenses..."
        )


        df = pd.read_csv(DATA_FILE)


        df["Date"] = pd.to_datetime(
            df["Date"],
            dayfirst=True
        )


        user_df = df[
            df["Name"].str.lower() == name.lower()
        ].copy()


        if user_df.empty:

            print(
                f"\nℹ️ No expenses found for {name}."
            )

            print(
                "Add your first expense before "
                "using expense search."
            )

            continue


        search_expenses(user_df)


    # ==============================
    # 4. ANALYZE BUDGET
    # ==============================

    elif choice == "4":

        print(
            "\nLoading your budget analysis..."
        )


        df = pd.read_csv(DATA_FILE)


        df["Date"] = pd.to_datetime(
            df["Date"],
            dayfirst=True
        )


        user_df = df[
            df["Name"].str.lower() == name.lower()
        ].copy()


        if user_df.empty:

            print(
                f"\nℹ️ No expenses found for {name}."
            )

            print(
                "Add your first expense before "
                "using budget analysis."
            )

            continue


        user_df["Month"] = (
            user_df["Date"].dt.to_period("M")
        )


        monthly_summary = user_df.groupby(
            "Month"
        )["Amount"].sum()


        analyze_budget(monthly_summary)


    # ==============================
    # 5. VIEW CHARTS
    # ==============================

    elif choice == "5":

        print(
            "\nLoading your spending charts..."
        )


        df = pd.read_csv(DATA_FILE)


        df["Date"] = pd.to_datetime(
            df["Date"],
            dayfirst=True
        )


        user_df = df[
            df["Name"].str.lower() == name.lower()
        ].copy()


        if user_df.empty:

            print(
                f"\nℹ️ No expenses found for {name}."
            )

            print(
                "Add your first expense before "
                "viewing spending charts."
            )

            continue


        category_summary = user_df.groupby(
            "Category"
        )["Amount"].sum()


        user_df["Month"] = (
            user_df["Date"].dt.to_period("M")
        )


        monthly_summary = user_df.groupby(
            "Month"
        )["Amount"].sum()


        print(
            "\nOpening spending charts..."
        )


        show_all_charts(
            category_summary,
            monthly_summary
        )


    # ==============================
    # 6. EXIT
    # ==============================

    elif choice == "6":

        print(
            "\nThank you for using AI Expense Analyzer!"
        )

        exit()


    # ==============================
    # INVALID OPTION
    # ==============================

    else:

        print(
            "⚠️ Invalid option. Please choose 1-6."
        )