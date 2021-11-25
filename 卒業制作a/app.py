from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>ありがとう</p>"
    
@app.route("/dbtest")
def dbtest():
    con = sqlite3.connect("卒業制作.db")
    c = con.cursor()
    c.execute("SELECT name, address, image, comment, parking, toilet, playset, convenience, history, vending, plaza, water, hot spring, traffic FROM parks WHERE id =1")
    parks_info = c.fetchone()
    c.close()
    print(parks_info)
    return render_template("dbtest.html",html_parks_info = parks_info)


@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/add", methods = ["POST"])
def add_post():
    task = request.form. get("name")
    task = request.form. get("address")
    task = request.form. get("image")
    con = sqlite3.connect("卒業制作.db")
    c = con.cursor()
    c.execute("INSERT INTO parks VALUES (null,?,?,?)", (task,))
    con.commit()
    con.close()
    return redirect("/")


if __name__ == "__main__":
    app.run()

app.run(debug = True)