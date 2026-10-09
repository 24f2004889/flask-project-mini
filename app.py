from flask import Flask,render_template,request

app= Flask(__name__)


students = {
    "Krishna": {"Python": 85, "DBMS": 70},
    "Rahul": {"Python": 60, "DBMS": 90},
    "Aman": {"Python": 35, "DBMS": 40}
}
@app.route("/home")
def home():
    
    return render_template('home.html',student=students)
 



@app.route("/student/<name>")
def student(name):
    name=name.capitalize()
    if name in students:
        marks = students[name]
        subject=request.args.get("student")
        return render_template("student.html",name=name,marks=marks,subject =subject) 
    else:
        return "Student not found"

if __name__ =="__main__":
    app.run(debug=True)