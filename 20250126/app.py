from flask import Flask
from flask import render_template,redirect
from detabase import memo

app = Flask(__name__)

@app.route("/")
def hello_world():

    return render_template("hello.html")
@app.route("/create")
def create():
    return redirect("/")

@app.route("/detale")
def detale():
    return redirect("/")



app.run(host="0.0.0.0",debug=True)