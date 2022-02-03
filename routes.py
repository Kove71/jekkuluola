from app import app
from flask import render_template, request, redirect
from services.jokes import get_jokes, add_joke

@app.route("/")
def index():
    jokes = get_jokes()
    return render_template("index.html", jokes=jokes)

@app.route("/newjoke", methods=["GET", "POST"])
def new_joke():
    if request.method == "GET":
        return render_template("newjoke.html")
    if request.method == "POST":
        joke_content = request.form["joke"]
        add_joke(joke_content)
        return redirect("/")