def show_dashboard(
    name,
    user_df,
    total,
    average_expense,
    highest_expense,
    highest_category,
    highest_month,
    highest_category_percentage,
    category_summary
):
    print("\n========== FINANCIAL DASHBOARD ==========")

    print(f"👤 User: {name}")

    print(f"\n💰 Total Spending: ₦{total:,.2f}")

    print(
        f"📈 Average Expense: "
        f"₦{average_expense:,.2f}"
    )

    print(
        f"🏆 Highest Expense: "
        f"{highest_expense['Item']} - "
        f"₦{highest_expense['Amount']:,.2f}"
    )

    print(
        f"🧾 Number of Expenses: "
        f"{len(user_df)}"
    )

    print(
        f"\n📂 Top Category: "
        f"{highest_category.title()}"
    )

    print(
        f"📅 Top Spending Month: "
        f"{highest_month.strftime('%B %Y')}"
    )

    print("\n💡 AI Insight:")

    print(
        f"{highest_category.title()} accounts for "
        f"{highest_category_percentage:.1f}% "
        f"of your total spending."
    )

    print("\n📊 Spending Distribution")

    for category, amount in category_summary.items():

        percentage = (amount / total) * 100

        bar_length = int(percentage / 5)

        bar = "█" * bar_length

        print(
            f"{category.title():<12} "
            f"{bar} {percentage:.1f}%"
        )

    print("=========================================")