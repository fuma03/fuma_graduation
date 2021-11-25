from flask import Flask, render_template, request, redirect
import sqlite3

@app.route("/dbtest")
def dbtest():
    on = sqlite3.connect("卒業制作.db")
    c = con.cursor()
    c.execute("SELECT name, address, image, comment, parking, toilet, playset, convenience, history, vending, plaza, water, hot spring, traffic FROM parks WHERE id =1")
    parks_info = c.fetchone()
    c.close()
    print(parks_info)
    return render_template("dbtest.html",html_parks_info = parks_info)


@app.route("/add")
def add():
    return render_template("add.html")
