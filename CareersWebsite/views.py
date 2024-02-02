from flask import Flask
from CareersWebsite import app

@app.route("/")
@app.route("/home")

def home():
    return "Home page!"