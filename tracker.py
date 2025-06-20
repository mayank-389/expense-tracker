import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])

def add_expense():
    category = input("Enter category (e.g., food, travel): ").strip()
    amount = input("Enter amount (₹): ").strip()
    note = input("Add a note (optional): ").strip()

    if not amount.replace('.', '', 1).isdigit():
        print("❌ Invalid amount. Please enter a number.")
        return

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), category, amount, note])
    print(f"✅ Added ₹{amount} to {category} ({note})\n")

def show_expenses():
    print("\n📋 All Expenses:")
    print("-" * 50)
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(f"{row[0]:<12} | {row[1]:<10} | ₹{row[2]:<7} | {row[3]}")
    except FileNotFoundError:
        print("No expenses found yet.")
    print("-" * 50 + "\n")

def total_expense():
    total = 0
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                total += float(row[2])
    except:
        print("❌ Could not calculate total. Make sure the file exists and contains valid data.")
        return

    print(f"\n💰 Total Spent: ₹{total}\n")

def main_menu():
    init_file()
    while True:
        print("📌 Expense Tracker Menu")
        print("1. Add New Expense")
        print("2. Show All Expenses")
        print("3. Show Total Spent")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice. Please select a number between 1 and 4.\n")

if __name__ == "__main__":
    main_menu()
