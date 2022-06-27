#flask minimal app


import email
import json
from flask import Flask,render_template,request,redirect,jsonify,session
from crud import *
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
    #return "<p>Hello, World!</p>"

@app.route("/products")
def products():
    return "<p>hii this is my product page</p>"

@app.route("/register",methods=['POST'])
def register():
    email=request.json['email']
    password=request.json['password']
    name=request.json['name']
    phoneno=request.json['mobile']
    
    add_user(email,password,name)
    return jsonify("data scucessfully inserted")

@app.route("/get_user/<int:id>",methods=['POST'])
def get_user(id):
    record=getuser_fromdb(id)
    return jsonify(record)

   
       


if __name__=="__main__":
    app.run(debug= True, port=8000) # for run app ...........port don't chnage in production