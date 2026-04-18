from flask import Flask, render_template, request
import json
app= Flask(__name__,template_folder='templates')
try:
    with open("expenses.json","r") as file:
        expenses=json.load(file)
except FileNotFoundError:    
   expenses=[]
def add_expense(category,amount,date):
    expense={"category":category,"amount":float(amount),"date":date}
    expenses.append(expense)
@app.route("/")
def home():
    return render_template('index.html',expenses=expenses)
@app.route('/add',methods=['POST'])
def add():
    category=request.form['category']
    amount= request.form['amount']
    date= request.form['date']
    add_expense(category,amount,date)
    with open("expenses.json","w") as file:
        json.dump(expenses,file)
    return render_template('index.html',expenses=expenses)
if __name__=="__main__":
    app.run(debug=True)
