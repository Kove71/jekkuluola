from app import app
from flask import render_template, request, redirect
from services.jokes import get_jokes, add_joke, get_user_jokes, get_jokepage_joke
from services.users import create_user, get_session_user, user_login, user_logout
from services.comments import get_comments, add_comment

@app.route("/")
def index():
    jokes = get_jokes()
    user_data = get_session_user()
    return render_template("index.html", jokes=jokes, user=user_data)

@app.route("/newjoke", methods=["GET", "POST"])
def new_joke():
    if request.method == "GET":
        return render_template("newjoke.html")
    if request.method == "POST":
        joke_content = request.form["joke"]
        add_joke(joke_content)
        return redirect("/")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        create_user(username, password)
        return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user_login(username, password):
            return redirect("/")
        else:
            return redirect("/login")

@app.route("/logout")
def logout():
    user_logout()
    return redirect("/")

@app.route("/profile/<username>")
def profile(username):
    user_jokes = get_user_jokes(username)
    return render_template("userpage.html", jokes=user_jokes)

@app.route("/joke/<int:id>", methods=["GET", "POST"])
def joke(id):
    if request.method == "GET":
        joke = get_jokepage_joke(id)
        comments = get_comments(id)
        return render_template("joke.html", joke=joke, comments=comments)
    if request.method == "POST":
        comment = request.form["comment"]
        add_comment(id, comment)
        return redirect(f"/joke/{id}")
