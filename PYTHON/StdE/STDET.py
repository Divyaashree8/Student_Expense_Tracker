print("Ganpati Bappa Morya Radhe Radhe")
expenses=[]
def addd_expense():
    amount=float(input("Enter amount:"))
    category= input("Enter category:")
    date= input("Enter Date (YYYY-MM-DD):")
    expense={"amount": amount,"category":category,"date":date}
    expenses.append(expense)
    print("Added")
def view_expenses():
    if not expenses:
        print("No expenses recorded")
        return
    print("All Expenses")
    print("-"*40)
    print(f"{'date':<12}{'category':<15}{'Amount':<10}")
    print("-"*40)
    for i in expenses:
        print(f"{i['date']:<12}{i['category']:<15}{i['amount']:<10}")
        print("-"*40)
def total_expenses():
    total=sum(i["amount"] for i in expenses)
    print("Total:",total)
while True:
    print("\n1. Add\n2. view\n3. Total\n4. exit")
    choice=input("choose:")
    if choice=="1":
        addd_expense()
    elif choice=="2":
        view_expenses()
    elif choice=="3":
        total_expenses()
    else:
        break


    