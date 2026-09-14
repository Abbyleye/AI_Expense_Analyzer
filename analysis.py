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

    # Monthly Spending Trend
    if len(monthly_summary) >= 2:

        current_month = monthly_summary.index[-1]
        previous_recorded_month = monthly_summary.index[-2]

        current_amount = monthly_summary.iloc[-1]
        previous_amount = monthly_summary.iloc[-2]

        # Check whether the previous recorded month
        # is actually the calendar month before
        expected_previous_month = current_month - 1

        print("\n--- Spending Trend ---")

        if previous_recorded_month != expected_previous_month:

            print(
                f"ℹ️ There are missing months between "
                f"{previous_recorded_month.strftime('%B %Y')} "
                f"and "
                f"{current_month.strftime('%B %Y')}."
            )

            print(
                f"Comparing the latest recorded months: "
                f"{previous_recorded_month.strftime('%B %Y')} "
                f"→ "
                f"{current_month.strftime('%B %Y')}"
            )

        monthly_change = (
            (current_amount - previous_amount)
            / previous_amount
        ) * 100

        if monthly_change > 0:
            print(
                f"📈 Spending increased by "
                f"{monthly_change:.1f}%."
            )

        elif monthly_change < 0:
            print(
                f"📉 Spending decreased by "
                f"{abs(monthly_change):.1f}%."
            )

        else:
            print(
                "➡️ Spending stayed the same."
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

    # Unusually High Expense
    if highest_expense["Amount"] > average_expense * 2:
        print(
            f"⚠️ Unusually high expense detected: "
            f"{highest_expense['Item']} - "
            f"₦{highest_expense['Amount']:,.2f}"
        )

    # Largest Expense Percentage
    highest_expense_percentage = (
        highest_expense["Amount"] / total
    ) * 100

    print(
        f"💡 Your largest expense accounts for "
        f"{highest_expense_percentage:.1f}% "
        f"of your total spending."
    )

    # Biggest Spending Category
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
        # Spending Concentration Insight
    if highest_category_percentage >= 70:
        print(
            f"⚠️ Your spending is heavily concentrated "
            f"in {highest_category.title()}."
        )

        print(
            f"💡 Consider reviewing your "
            f"{highest_category.lower()} expenses "
            f"to see where you can reduce unnecessary spending."
        )

    elif highest_category_percentage >= 50:
        print(
            f"⚠️ A large portion of your spending "
            f"goes to {highest_category.title()}."
        )

        print(
            f"💡 Keep monitoring your "
            f"{highest_category.lower()} expenses."
        )

    else:
        print(
            "✅ Your spending is not heavily "
            "concentrated in one category."
        )

            # Spending Frequency Insight
    category_frequency = user_df["Category"].value_counts()

    most_frequent_category = category_frequency.idxmax()
    most_frequent_count = category_frequency.max()

    print("\n--- Spending Frequency ---")

    print(
        f"🍽️ {most_frequent_category.title()} was your "
        f"most frequent spending category with "
        f"{most_frequent_count} transactions."
    )
        # Spending Pattern Insight
    total_transactions = len(user_df)

    most_frequent_percentage = (
        most_frequent_count / total_transactions
    ) * 100

    print("\n--- Spending Pattern ---")

    if (
        most_frequent_category == highest_category
        and highest_category_percentage >= 50
    ):
        print(
            f"⚠️ {highest_category.title()} is both your "
            f"highest spending and most frequent category."
        )

        print(
            f"💡 {highest_category.title()} accounts for "
            f"{highest_category_percentage:.1f}% of your spending "
            f"and {most_frequent_percentage:.1f}% of your transactions."
        )

    elif highest_category_percentage >= 50:
        print(
            f"⚠️ {highest_category.title()} is your main "
            f"spending category."
        )

    else:
        print(
            "✅ No single category dominates your spending."
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