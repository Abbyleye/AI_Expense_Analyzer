import pandas as pd


def analyze_expenses(user_df):
    print("\n------Pandas Analysis------")

    total = user_df["Amount"].sum()
    average_expense = user_df["Amount"].mean()
    highest_expense = user_df.loc[
        user_df["Amount"].idxmax()
    ]

    print(f"Total spending: ₦{total:,.2f}")
    print(f"Average spending: ₦{average_expense:,.2f}")
    print(
        f"Highest spending: "
        f"₦{highest_expense['Amount']:,.2f}"
    )
    print(f"Number of expenses: {len(user_df)}")

    # Category Analysis
    category_summary = user_df.groupby(
        "Category"
    )["Amount"].sum()

    print("\n-----Category Analysis-----")
    print(category_summary)

    # Spending by Date
    date_summary = user_df.groupby(
        "Date"
    )["Amount"].sum()

    print("\n-----Spending by Date-----")

    for date, amount in date_summary.items():
        print(
            f"{date.strftime('%d/%m/%Y')}: "
            f"₦{amount:,.2f}"
        )

    # Monthly Spending
    user_df["Month"] = user_df["Date"].dt.to_period("M")

    monthly_summary = user_df.groupby(
        "Month"
    )["Amount"].sum()

    print("\n-----Monthly Spending-----")

    for month, amount in monthly_summary.items():
        print(
            f"{month.strftime('%B %Y')}: "
            f"₦{amount:,.2f}"
        )

    # Highest Spending Month
    highest_month = monthly_summary.idxmax()
    highest_month_amount = monthly_summary.max()

    print(
        f"\n🏆 Highest Spending Month: "
        f"{highest_month.strftime('%B %Y')} "
        f"— ₦{highest_month_amount:,.2f}"
    )

    # Spending by Category
    print("\n--Spending by Category--")

    for category, amount in category_summary.items():
        percentage = (amount / total) * 100

        print(
            f"{category.title()}: "
            f"₦{amount:,.2f} "
            f"({percentage:.1f}%)"
        )

    # Spending Insights
    highest_category = category_summary.idxmax()
    highest_category_amount = category_summary.max()

    highest_category_percentage = (
        highest_category_amount / total
    ) * 100

    print("\n---Spending Insights---")

    print(
        f"Highest Expense: "
        f"{highest_expense['Item']} - "
        f"₦{highest_expense['Amount']:,.2f}"
    )

    print(
        f"Average Expense: "
        f"₦{average_expense:,.2f}"
    )

    print(
        f"\n💡 Biggest Spending Category: "
        f"{highest_category.title()}"
    )

    print(
        f"You spent ₦{highest_category_amount:,.2f} "
        f"on {highest_category.title()}, "
        f"which is {highest_category_percentage:.1f}% "
        f"of your total spending."
    )

    # AI Recommendation
    print("\n--- AI Recommendation ---")

    if highest_category_percentage > 50:
        print(
            f"⚠️ {highest_category.title()} is taking up "
            f"more than half of your total spending."
        )

        print(
            f"Consider monitoring your "
            f"{highest_category.lower()} expenses "
            f"and setting a budget for this category."
        )

    elif highest_category_percentage > 30:
        print(
            f"💡 {highest_category.title()} is your "
            f"biggest spending category."
        )

        print(
            f"Keep an eye on your "
            f"{highest_category.lower()} expenses "
            f"to avoid overspending."
        )

    else:
        print(
            "✅ Your spending is fairly distributed "
            "across categories."
        )

    return (
        total,
        average_expense,
        highest_expense,
        category_summary,
        monthly_summary,
        highest_month,
        highest_category,
        highest_category_amount,
        highest_category_percentage
    )