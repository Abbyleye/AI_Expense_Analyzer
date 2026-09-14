import pandas as pd
from datetime import datetime


def analyze_budget(monthly_summary):

    while True:
        budget_month = input(
            "\nWhich month do you want to analyze? (MM/YYYY): "
        ).strip()

        try:
            datetime.strptime(budget_month, "%m/%Y")
            break

        except ValueError:
            print("⚠️ Invalid month. Please use MM/YYYY.")

    while True:
        try:
            monthly_budget = float(
                input("What is your monthly budget? ₦")
            )

            if monthly_budget <= 0:
                print("⚠️ Budget must be greater than 0.")
                continue

            break

        except ValueError:
            print("⚠️ Please enter a valid budget amount.")

    # Convert user's input to a period
    budget_period = pd.Period(
        budget_month,
        freq="M"
    )

    # Get spending for the selected month
    selected_month_spending = monthly_summary.get(
        budget_period,
        0
    )

    # Calculate remaining budget
    remaining_budget = (
        monthly_budget - selected_month_spending
    )

    # Calculate percentage of budget used
    budget_used = (
        selected_month_spending / monthly_budget
    ) * 100

    print("\n----- Monthly Budget Analysis -----")

    print(
        f"Month: {budget_period.strftime('%B %Y')}"
    )

    print(
        f"Monthly Budget: ₦{monthly_budget:,.2f}"
    )

    print(
        f"Amount Spent: ₦{selected_month_spending:,.2f}"
    )

    print(
        f"Remaining Budget: ₦{remaining_budget:,.2f}"
    )

    print(
        f"Budget Used: {budget_used:.1f}%"
    )

        # Financial Health Risk Level
    print("\n--- Financial Health ---")

    if budget_used > 100:
        print("🔴 Financial Health: Over Budget")

        print(
            f"⚠️ You have exceeded your budget by "
            f"₦{abs(remaining_budget):,.2f}."
        )

        print(
            "💡 Consider reducing non-essential "
            "expenses for this month."
        )

    elif budget_used >= 80:
        print("🟠 Financial Health: High Risk")

        print(
            "⚠️ You have used 80% or more "
            "of your monthly budget."
        )

        print(
            "💡 Be careful with additional spending "
            "for the rest of the month."
        )

    elif budget_used >= 70:
        print("🟡 Financial Health: Moderate Risk")

        print(
            "⚠️ You have used 70% or more "
            "of your monthly budget."
        )

        print(
            "💡 Monitor your spending to avoid "
            "approaching your budget limit."
        )

    else:
        print("🟢 Financial Health: Healthy")

        print(
            "✅ Your spending is currently "
            "within a comfortable range."
        )