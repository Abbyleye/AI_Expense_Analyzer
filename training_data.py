from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

expenses = [
    # FOOD
    ("rice", "food"),
    ("beans", "food"),
    ("jollof rice", "food"),
    ("jollof", "food"),
    ("fufu", "food"),
    ("bread", "food"),
    ("chicken", "food"),
    ("fish", "food"),
    ("yam", "food"),
    ("spaghetti", "food"),
    ("amala", "food"),
    ("eba", "food"),
    ("garri", "food"),
    ("pasta", "food"),
    ("noodles", "food"),
    ("breakfast", "food"),
    ("lunch", "food"),
    ("dinner", "food"),
    ("snacks", "food"),
    ("restaurant", "food"),

    # TRANSPORT
    ("bus", "transport"),
    ("bike", "transport"),
    ("uber", "transport"),
    ("uber ride", "transport"),
    ("bolt", "transport"),
    ("bolt ride", "transport"),
    ("taxi", "transport"),
    ("fuel", "transport"),
    ("petrol", "transport"),
    ("transport fare", "transport"),
    ("bus fare", "transport"),
    ("motorcycle", "transport"),

    # CLOTHING
    ("shirt", "clothing"),
    ("trousers", "clothing"),
    ("dress", "clothing"),
    ("fabric", "clothing"),
    ("shoes", "clothing"),
    ("sneakers", "clothing"),
    ("skirt", "clothing"),
    ("clothes", "clothing"),
    ("clothing", "clothing"),
    ("blouse", "clothing"),
    ("top", "clothing"),
    ("jacket", "clothing"),
    ("jeans", "clothing"),
    ("shorts", "clothing"),
    ("sandal", "clothing"),

    # EDUCATION
    ("school fees", "education"),
    ("school fee", "education"),
    ("textbook", "education"),
    ("textbooks", "education"),
    ("course", "education"),
    ("exam fee", "education"),
    ("tuition", "education"),
    ("school", "education"),
    ("lecture", "education"),
    ("assignment", "education"),

    # AIRTIME / DATA
    ("mtn airtime", "airtime"),
    ("airtel airtime", "airtime"),
    ("glo airtime", "airtime"),
    ("9mobile airtime", "airtime"),
    ("airtime", "airtime"),
    ("data", "airtime"),
    ("mtn data", "airtime"),
    ("airtel data", "airtime"),
    ("internet data", "airtime"),
    ("mobile data", "airtime"),

    # GIVING
    ("offering", "giving"),
    ("donation", "giving"),
    ("giving", "giving"),
    ("charity", "giving"),
    ("church offering", "giving"),
    ("church donation", "giving"),
    ("donate", "giving"),
    ("donated", "giving"),
    ("gift", "giving"),
    ("financial gift", "giving"),
]
# Prepare training data
texts = [item[0] for item in expenses]
categories = [item[1] for item in expenses]
# Convert words into numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
# Train the machine learning model
model = LogisticRegression()
model.fit(X, categories)

# Function to predict a category
def predict_category(expense_name):
    expense_vector = vectorizer.transform([expense_name])
    prediction = model.predict(expense_vector)

    return prediction[0]


