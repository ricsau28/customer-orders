from flask import Flask, render_template
from . import app

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/customers")
def get_customers():
    return render_template("index.html")