import matplotlib.pyplot as plt


def spending_by_category(category_summary):
    plt.figure()

    plt.bar(
        category_summary.index,
        category_summary.values
    )

    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount (₦)")

    plt.show()


def monthly_spending_trend(monthly_summary):
    plt.figure()

    plt.plot(
        monthly_summary.index.astype(str),
        monthly_summary.values,
        marker="o"
    )

    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount (₦)")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()


def spending_distribution(category_summary):
    plt.figure()

    plt.pie(
        category_summary.values,
        labels=category_summary.index,
        autopct="%.1f%%"
    )

    plt.title("Spending Distribution by Category")

    plt.show()