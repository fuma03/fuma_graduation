from sqlite3.dbapi2 import SQLITE_SELECT
from flask import Flask, render_template, request, redirect,session
import sqlite3

app = Flask(__name__, static_folder='./templates/img') 
@app.route("/add")
def add():
    return render_template("torisetu.html",)

if __name__ == "__main__":
    app.run(debug=True)









