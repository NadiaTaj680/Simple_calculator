from flask import Flask ,render_template, request
app=Flask(__name__)


    # Making a simple calculator URl for adding ,subtratcting ,dividing and multiplying two numbers:
@app.route('/', methods=["GET","POST"])
def calc():
    if request.method== "POST":
        num1 = float(request.form['n1'])
        num2 = float(request.form['n2'])


        operator = request.form['operation']
        if (operator == '+'):
            res = num1+num2
        elif (operator == '-'):
            res = num1-num2
        elif (operator == '*'):
           res = num1*num2
        elif (operator == '/'):
           if num2!=0:
               res = num1/num2
           else:
               res= "Error: Division by zero"
        else:
            res = "Invalid Operater"
        return render_template('calc.html', result=res)

    return render_template('calc.html')




if __name__=="__main__":
    app.run(debug=True)