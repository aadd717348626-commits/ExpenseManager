# Expense Manager Project
# This program allows you to add, view, and save expenses in a text file.

# Function to add a new expense
def add_expense():
    amount = input("Enter the amount: ")
    category = input("Enter the category (e.g., food, transport, bills): ")
    description = input("Enter a description: ")

    with open("data.txt", "a") as file:
        file.write(f"{amount}, {category}, {description}\n")

    print("Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    try:
        with open("data.txt", "r") as file:
            expenses = file.readlines()

        if not expenses:
            print("No expenses found.\n")
        else:
            print("\n--- Expenses ---")
            for expense in expenses:
                print(expense.strip())
            print()
    except FileNotFoundError:
        print("No expenses found. Add one first!\n")

# Main program
def main():
    while True:
        print("Expense Manager")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
