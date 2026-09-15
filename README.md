# AI Expense Analyzer

AI Expense Analyzer is a Python-based personal finance application that helps users record, analyze, search, and visualize their expenses.

The application uses **machine learning** to automatically suggest expense categories such as Food, Transport, Clothing, Education, Airtime, and Giving.

It also uses **Pandas** for financial analysis and **Matplotlib** to visualize spending patterns.

The project is designed as a practical demonstration of how **Python, data analysis, machine learning, and financial insights** can be combined into a useful real-world application.

## Project Goal

The goal of AI Expense Analyzer is to make personal expense tracking more intelligent by moving beyond simple record keeping.

Instead of only showing how much a user has spent, the application provides insights such as:

* Total and average spending
* Highest expense
* Spending by category
* Monthly spending trends
* Most frequent spending category
* Spending concentration
* Budget usage and financial health
* Spending recommendations based on detected spending patterns
* Visual spending charts

## Features

### 🤖 AI Expense Categorization

Uses **TF-IDF vectorization and Logistic Regression** to analyze expense descriptions and suggest an appropriate spending category.

### 💰 Expense Tracking

Users can record:

* Expense name/item
* Amount
* Category
* Date

Expenses are stored locally in a CSV file.

### 📊 Financial Analysis

The application uses **Pandas** to calculate and display:

* Total spending
* Average expense
* Highest expense
* Number of transactions
* Spending by category
* Spending by date
* Monthly spending
* Highest spending month
* Spending trends
* Category percentages
* Spending frequency

### 💡 Spending Insights

The application identifies spending patterns and provides financial insights, including:

* Largest expense
* Biggest spending category
* Spending concentration
* Most frequent spending category
* Unusually high expenses
* Spending recommendations based on detected spending patterns

### 💵 Budget Analysis

Users can enter a monthly budget and analyze:

* Amount spent
* Remaining budget
* Percentage of budget used
* Financial health status

The application identifies different financial health levels, including:

* Healthy
* Moderate Risk
* High Risk
* Over Budget

### 🔎 Expense Search

Users can search their expenses by:

* Category
* Item
* Month
* All recorded expenses

### 📈 Data Visualization

Uses **Matplotlib** to generate:

* Spending by category chart
* Monthly spending trend
* Spending distribution chart

### 🛡️ Input Validation

The application validates user input to prevent common errors such as:

* Empty expense names
* Invalid amounts
* Negative amounts
* Invalid dates
* Invalid yes/no responses
* Invalid menu selections

### 🇳🇬 Nigerian Naira Support

Financial amounts are displayed in **Nigerian Naira (₦)**, making the application suitable for demonstrating personal finance tracking in a Nigerian context.

## AI/ML Component

The AI Expense Analyzer uses a supervised machine learning model to automatically classify expense descriptions into spending categories.

### Machine Learning Pipeline

The categorization process follows these steps:

1. **Training Data**

   * The model is trained using example expense descriptions.
   * Each example is associated with a spending category such as Food, Transport, Clothing, Education, Airtime, or Giving.

2. **Text Vectorization**

   * Expense descriptions are converted from text into numerical features using **TF-IDF (Term Frequency-Inverse Document Frequency)**.
   * This allows the machine learning model to work with text data.

3. **Classification**

   * A **Logistic Regression** classifier is trained on the TF-IDF features.
   * The model learns patterns that associate words and phrases with different expense categories.

4. **Prediction**

   * When a user enters a new expense, the description is passed through the same TF-IDF vectorizer.
   * The trained Logistic Regression model predicts the most likely category.

### Example

```text
User enters:
"rice"

        ↓

TF-IDF Vectorization

        ↓

Logistic Regression

        ↓

Suggested category:
Food
```

Another example:

```text
User enters:
"bike"

        ↓

Machine Learning Model

        ↓

Suggested category:
Transport
```

### Human Confirmation

The application does not blindly accept every prediction.

After the model suggests a category, the user can:

* Accept the AI suggestion
* Reject the suggestion and select the correct category manually

This allows users to correct incorrect predictions and makes the application more practical for real-world use.

### Technologies Used for Machine Learning

* **Scikit-learn**
* **TF-IDF Vectorizer**
* **Logistic Regression**

This project demonstrates a simple but practical **Natural Language Processing (NLP)** workflow for classifying short text descriptions.

## Technologies Used

| Technology       | Purpose                                     |
| ---------------- | ------------------------------------------- |
| **Python**       | Core programming language                   |
| **Pandas**       | Data processing and financial analysis      |
| **Scikit-learn** | Machine learning and expense classification |
| **Matplotlib**   | Data visualization                          |
| **CSV**          | Local expense data storage                  |
| **Git & GitHub** | Version control and project hosting         |

### Python Concepts Demonstrated

This project also demonstrates practical Python concepts including:

* Functions
* Loops
* Conditional statements
* Lists and dictionaries
* File handling
* Exception handling
* Modules and imports
* Data processing
* Object-oriented machine learning libraries
* User input validation

## How It Works

The application follows a simple workflow:

```text
Start Application
       │
       ▼
Enter User Name
       │
       ▼
Main Menu
       │
       ├── Add Expense
       │      │
       │      ▼
       │   Enter Expense
       │      │
       │      ▼
       │   AI Category Prediction
       │      │
       │      ▼
       │   Confirm Category
       │      │
       │      ├── Yes ──────► Save Expense
       │      │
       │      └── No ───────► Choose Category
       │                              │
       │                              ▼
       │                         Save Expense
       │
       ├── View Dashboard
       │
       ├── Search Expenses
       │
       ├── Analyze Budget
       │
       ├── View Charts
       │
       └── Exit
```

All recorded expenses are stored locally in `expenses.csv`.

The application then uses the stored data for financial analysis, budgeting, searching, and visualization.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Abbyleye/AI_Expense_Analyzer.git
```

### 2. Navigate into the Project

```bash
cd AI_Expense_Analyzer
```

### 3. Install the Required Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** The `requirements.txt` file will be added to the project as part of the final setup.

### 4. Run the Application

```bash
python main.py
```

On Windows, if the `python` command is not available, you can use:

```bash
py main.py
```

## How to Use

After starting the application:

1. Enter your name.
2. Choose an option from the main menu.
3. Select **Add Expense** to record a new expense.
4. Enter the expense name and amount.
5. Review the AI-generated category suggestion.
6. Confirm the suggested category or select a category manually.
7. Enter the expense date using `DD/MM/YYYY`.
8. Use the dashboard, search, budget analysis, or charts to understand your spending.

### Main Menu

```text
========== AI EXPENSE ANALYZER ==========

1. Add Expense
2. View Dashboard
3. Search Expenses
4. Analyze Budget
5. View Charts
6. Exit
```

The application stores user expenses locally in `expenses.csv`.

For portfolio demonstrations, the repository also includes a fictional dataset named `demo_expenses.csv`.

## Example Output

### AI Expense Categorization

```text
Enter expense name: rice
Enter amount: ₦4000

🤖 AI Suggested Category: Food

Accept this category? (yes/no): yes

✅ Expense saved successfully!
```

### Financial Analysis

```text
------Pandas Analysis------

Total spending: ₦22,300.00
Average spending: ₦1,115.00
Highest spending: ₦5,000.00
Number of expenses: 20

-----Category Analysis-----

clothing       5000
food          13500
transport      3800

🏆 Highest Spending Month:
February 2026 — ₦14,300.00

--- Spending Insights ---

💡 Biggest Spending Category: Food

You spent ₦13,500.00 on Food,
which is 60.5% of your total spending.

⚠️ Food is both your highest spending
and most frequent category.

💡 Consider monitoring your Food expenses
and setting a budget for this category.
```

### Budget Analysis

```text
----- Monthly Budget Analysis -----

Month: February 2026
Monthly Budget: ₦10,000.00
Amount Spent: ₦7,300.00
Remaining Budget: ₦2,700.00
Budget Used: 73.0%

--- Financial Health ---

🟡 Financial Health: Moderate Risk

💡 Monitor your spending to avoid
approaching your budget limit.
```

> The example values above are included to demonstrate the application's output format. The application calculates these values dynamically from the user's recorded expenses.

## Project Structure

```text
AI-Expense-Analyzer/
│
├── main.py                 # Main application and user interface
├── training_data.py        # Machine learning model and training data
├── analysis.py             # Financial analysis and spending insights
├── dashboard.py            # Financial dashboard
├── budget.py               # Budget and financial health analysis
├── search.py               # Expense search functionality
├── charts.py               # Spending visualizations
│
├── demo_expenses.csv       # Fictional portfolio demonstration data
├── expenses.csv            # Local/private user expense data (gitignored)
├── expenses_backup.csv     # Local/private backup (gitignored)
│
├── .gitignore              # Prevents private/unnecessary files from Git
└── README.md               # Project documentation
```

### Module Responsibilities

| File                | Responsibility                                              |
| ------------------- | ----------------------------------------------------------- |
| `main.py`           | Controls the application flow and user interaction          |
| `training_data.py`  | Trains and uses the ML expense categorization model         |
| `analysis.py`       | Performs financial analysis and generates spending insights |
| `dashboard.py`      | Displays the user's financial dashboard                     |
| `budget.py`         | Calculates budget usage and financial health                |
| `search.py`         | Searches expenses by category, item, or month               |
| `charts.py`         | Generates spending charts                                   |
| `demo_expenses.csv` | Provides clean fictional data for demonstrations            |


## Future Improvements

The current project is a command-line prototype. Future versions could expand it into a full personal finance platform.

Planned improvements include:

* 🌐 Web-based user interface
* 🗄️ Database storage instead of CSV files
* 👤 User accounts and authentication
* 📱 Mobile-friendly interface
* 📥 CSV expense import
* 📊 More advanced financial dashboards
* 🔮 Spending forecasting
* 🧠 Improved machine learning categorization
* 📈 Personalized spending recommendations
* 🚨 Unusual-expense detection
* 🎯 Savings and financial goals
* 🔁 Recurring expense tracking
* 📅 Monthly and yearly financial reports
* 🔔 Budget alerts and notifications
* 💳 Income and expense tracking
* 💰 More advanced financial health scoring

The long-term goal is to evolve **AI Expense Analyzer** from a command-line learning project into a practical **AI-powered personal finance assistant**.


## Author

**Abiodun Ojo**

This project was built as part of my practical journey into:

* Python programming
* Data analysis
* Machine learning
* Artificial intelligence
* Financial technology

### Project Repository

[AI Expense Analyzer on GitHub](https://github.com/Abbyleye/AI_Expense_Analyzer.git)
