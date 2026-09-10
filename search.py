from datetime import datetime

def search_expenses(user_df):
    print("\n========== EXPENSE SEARCH ==========")
    print("1. Search by category")
    print("2. Search by item")
    print("3. Search by month")
    print("4. Show all my expenses")
    print("5. Exit search")

    while True:
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            while True:
                search_category = input(
                    "\nSearch by category "
                    "(food/transport/clothing/education/airtime/giving): "
                ).strip().lower()

                if search_category in user_df["Category"].unique():
                    break

                print("⚠️ Category not found. Please try again.")

            filtered_expenses = user_df[
                user_df["Category"] == search_category
            ]

            print("\n----- Search Results -----")
            print(
                filtered_expenses[
                    ["Date", "Item", "Amount", "Category"]
                ]
            )

            search_total = filtered_expenses["Amount"].sum()

            print(
                f"\nTotal {search_category.title()} Spending: "
                f"₦{search_total:,.2f}"
            )

        elif choice == "2":
            search_item = input(
                "\nWhat item do you want to search for? "
            ).strip().lower()

            filtered_expenses = user_df[
                user_df["Item"].str.lower().str.contains(
                    search_item,
                    na=False
                )
            ]

            if filtered_expenses.empty:
                print("⚠️ No matching expense found.")
            else:
                print("\n----- Search Results -----")
                print(
                    filtered_expenses[
                        ["Date", "Item", "Amount", "Category"]
                    ]
                )

                search_total = filtered_expenses["Amount"].sum()

                print(
                    f"\nTotal spending for '{search_item}': "
                    f"₦{search_total:,.2f}"
                )

        elif choice == "3":
            search_month = input(
                "\nEnter month to search (MM/YYYY): "
            ).strip()

            try:
                month = datetime.strptime(
                    search_month,
                    "%m/%Y"
                ).strftime("%Y-%m")

                filtered_expenses = user_df[
                    user_df["Date"].dt.strftime("%Y-%m") == month
                ]

                if filtered_expenses.empty:
                    print("⚠️ No expenses found for that month.")
                else:
                    print("\n----- Search Results -----")
                    print(
                        filtered_expenses[
                            ["Date", "Item", "Amount", "Category"]
                        ]
                    )

                    search_total = filtered_expenses["Amount"].sum()

                    print(
                        f"\nTotal spending for {search_month}: "
                        f"₦{search_total:,.2f}"
                    )

            except ValueError:
                print(
                    "⚠️ Invalid month. Please use MM/YYYY."
                )

        elif choice == "4":
            print("\n----- All My Expenses -----")
            print(
                user_df[
                    ["Date", "Item", "Amount", "Category"]
                ]
            )

            print(
                f"\nTotal Spending: ₦"
                f"{user_df['Amount'].sum():,.2f}"
            )

        elif choice == "5":
            print("\nExiting expense search...")
            break

        else:
            print("⚠️ Invalid option. Please choose 1-5.")