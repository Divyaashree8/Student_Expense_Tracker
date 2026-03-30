print("Ganpati Bappa Morya Radhe Radhe")
expenses=[]
def addd_expense():
    amount=float(input("Enter amount:"))
    category= input("Enter category:")
    expense={"amount": amount,"category":category}
    expenses.append(expense)
    print("Added")
def view_expenses():
    for i in expenses:
        print(i)
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


    