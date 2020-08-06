from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lecture.db'
db = SQLAlchemy(app)

@app.route("/")
def index(): 
    rows = db.engine.execute("SELECT * FROM registrants")
    return render_template("index.html", rows=rows)

@app.route("/register", methods = ["GET", "POST"])   
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get("name")
        if not name:
            return render_template("apology.html", message="You must provide a name.")
        email = request.form.get("email")
        if not email:
            return render_template("apology.html", message="You must provide an email address.")
        db.engine.execute("INSERT INTO registrants (name, email) VALUES (:name, :email)", name=name, email=email)    
        return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)    