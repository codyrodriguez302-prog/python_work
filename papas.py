import pandas as pd
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        # Initialize an empty DataFrame to store expenses
        self.expenses = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])

    def add_expense(self, category: str, amount: float, description: str = ""):
        """Add a new expense record."""
        pense = pd.DataFrame([{
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Category": category.title(),
            "Amount": float(amount),
            "Description": description
        }])
        self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)
        print(f"Added expense: ${amount:.2f} for '{description}' under [{category}]")

    def category_summary(self):
        """Display total spent per category."""
        if self.expenses.empty:
            print("No expenses recorded yet.")
            return None
        
        summary = self.expenses.groupby("Category")["Amount"].sum().reset_index()
        summary = summary.sort_values(by="Amount", ascending=False)
        return summary

    def save_to_csv(self, filename: str = "expenses.csv"):
        """Export data to CSV."""
        self.expenses.to_csv(filename, index=False)
        print(f"Data saved successfully to {filename}")


# --- Example Usage ---
if __name__ == "__main__":
    tracker = ExpenseTracker()
    
    # Adding sample data
    tracker.add_expense("Food", 15.50, "Lunch at cafe")
    tracker.add_expense("Transport", 22.00, "Gasoline")
    tracker.add_expense("Food", 45.10, "Weekly groceries")
    tracker.add_expense("Entertainment", 12.99, "Streaming subscription")

    print("\n--- Spending Summary by Category ---")
    print(tracker.category_summary().to_string(index=False))

    # Save output
    tracker.save_to_csv()
    