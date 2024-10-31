import json
import matplotlib.pyplot as plt

class BudgetTracker:
    def __init__(self, filename="budget.json"):
        self.filename = filename
        self.budget_data = {"budget": {}, "expenses": []}
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                self.budget_data = json.load(file)
        except FileNotFoundError:
            self.save_data()

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.budget_data, file, indent=4)

    def set_budget(self, category, amount):
        self.budget_data["budget"][category] = amount
        self.save_data()

    def add_expense(self, category, amount, description):
        self.budget_data["expenses"].append({
            "category": category,
            "amount": amount,
            "description": description
        })
        self.save_data()

    def view_expenses(self):
        for expense in self.budget_data["expenses"]:
            print(f"{expense['category']}: ${expense['amount']} - {expense['description']}")

    def generate_report(self):
        categories = list(self.budget_data["budget"].keys())
        budgeted_amounts = [self.budget_data["budget"].get(category, 0) for category in categories]
        spent_amounts = [sum(expense["amount"] for expense in self.budget_data["expenses"] if expense["category"] == category) for category in categories]

        x = range(len(categories))
        plt.bar(x, budgeted_amounts, width=0.4, label="Budgeted", align="center")
        plt.bar(x, spent_amounts, width=0.4, label="Spent", align="edge")
        plt.xlabel("Categories")
        plt.ylabel("Amount")
        plt.title("Budget vs. Spending")
        plt.xticks(x, categories, rotation=45)
        plt.legend()
        plt.show()

tracker = BudgetTracker()
tracker.set_budget("Food", 200)
tracker.set_budget("Entertainment", 100)
tracker.add_expense("Food", 15, "Lunch")
tracker.add_expense("Entertainment", 30, "Movies")
tracker.generate_report()
