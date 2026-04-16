from flask import Flask, render_template, request
app= Flask(__name__,template_folder='templates')
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
    return render_template('index.html',expenses=expenses)
if __name__=="__main__":
    app.run(debug=True)
