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
    c.execute("SELECT * FROM parks WHERE id =1")
    parks_info = c.fetchall()
    c.close()
    print(parks_info)
    return render_template("dbtest.html",html_parks_info = parks_info)


@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/add", methods = ["POST"])
def add_post():
    id  = request.form.get("id")
    name = request.form.get("name")
    address = request.form.get("address")
    image = request.form.get("image")
    parking  = request.form.get("parking")
    toilet  = request.form.get("toilet")
    playset  = request.form.get("playset")
    convenience  = request.form.get("convenience")
    history  = request.form.get("history")
    vending  = request.form.get("vending")
    plaza  = request.form.get("plaza")
    water  = request.form.get("water")
    hot_spring  = request.form.get("hot_spring")
    traffic  = request.form.get("traffic")
    comment  = request.form.get("comment")

    con = sqlite3.connect("卒業制作.db")
    c = con.cursor() 
    c.execute("INSERT INTO parks VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (id, name, address, image, comment, parking, toilet, playset, convenience, history, vending, plaza, water, hot_spring, traffic,))
    con.commit()
    con.close()
    return redirect("/")


if __name__ == "__main__":
    app.run()

app.run(debug = True)