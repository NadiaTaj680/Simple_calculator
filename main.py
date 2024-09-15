from flask import Flask ,render_template,jsonify
app=Flask(__name__)


   # Displaying dictionary of students names in jason format:
@app.route('/')
def home():
    students={"Names":["Asad","Zoraiz","Abubakar","Zayan","Abuzar","Abuzaid"]}
    return jsonify(students)

 # Displaying addition of two numbers in json format:
@app.route("/calc")
def calc():
    a = 100
    b = 200
    c= a+b

    result={"c":c}
    return jsonify(result)


 # Displaying addition of two numbers through rendering template (jinja template) :
@app.route("/homecalc")
def homecalc():
    a = 100
    b = 200
    c= a+b

    return render_template('home.html', c=c)


if __name__=="__main__":
    app.run(debug=True)