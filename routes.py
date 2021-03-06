from distutils.log import error
from app import app
from flask import render_template, request, redirect, session, abort
from services.admin import give_admin_rights, ban_user, remove_joke
from services.jokes import add_joke, get_jokes_by_time, get_jokes_by_vote, get_user_jokes, get_jokepage_joke
from services.users import create_user, get_session_user, user_login, user_logout
from services.comments import get_comments, add_comment
from services.votes import get_user_votes, get_votes, vote

@app.route("/")
def index():
    jokes = get_jokes_by_time()
    user_data = get_session_user()
    return render_template("index.html", jokes=jokes, user=user_data)

@app.route("/best")
def best():
    jokes = get_jokes_by_vote()
    user_data = get_session_user()
    return render_template("index.html", jokes=jokes, user=user_data)

@app.route("/newjoke", methods=["GET", "POST"])
def new_joke():
    if request.method == "GET":
        return render_template("newjoke.html")
    if request.method == "POST":
        joke_content = request.form["joke"].strip()
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        if joke_content:
            j_id = add_joke(joke_content)
            vote(j_id, 0)
            return redirect("/")
        return render_template("newjoke.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()
        second_password = request.form["second_password"].strip()
        case = create_user(username, password, second_password)
        if case == 0:
            return redirect("/login")
        elif case == 1:
            errormessage = "Anna salasana ja käyttäjätunnus"
        elif case == 2:
            errormessage = "Salasanat eivät täsmää"
        elif case == 3:
            errormessage = "Valitsemasi käyttäjätunnus on jo käytössä"
        else:
            errormessage = "Jokin meni mönkään"
        return render_template("signup.html", errormessage=errormessage)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        case = user_login(username, password)
        if case == 0:    
            return redirect("/")
        elif case == 1:
            errormessage = "Käyttäjää ei löytynyt"
        elif case == 2:
            errormessage = "Olet bänned"
        elif case == 3:
            errormessage = "Salasana oli väärin"
        else:
            errormessage = "Jokin meni mönkään"
        return render_template("login.html", errormessage=errormessage)

@app.route("/banuser/<username>")
def banuser(username):
    ban_user(username)
    return redirect("/")

@app.route("/giveadmin/<username>")
def giveadmin(username):
    give_admin_rights(username)
    return redirect("/")


@app.route("/removejoke/<int:id>")
def removejoke(id):
    remove_joke(id)
    return redirect("/")

@app.route("/logout")
def logout():
    user_logout()
    return redirect("/")

@app.route("/profile/<username>")
def profile(username):
    user_jokes = get_user_jokes(username)
    user_votes = get_user_votes(username)
    return render_template("userpage.html", jokes=user_jokes, votes=user_votes, username=username)

@app.route("/joke/<int:id>", methods=["GET", "POST"])
def joke(id):
    if request.method == "GET":
        joke = get_jokepage_joke(id)
        comments = get_comments(id)
        votes = get_votes(id)
        return render_template("joke.html", joke=joke, comments=comments, votes=votes)
    if request.method == "POST":
        comment = request.form["comment"].strip()
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)        
        if comment:
            add_comment(id, comment)
        return redirect(f"/joke/{id}")

@app.route("/upvote/<int:id>")
def upvote(id):
    vote(id, 1)
    return redirect(f"/joke/{id}")

@app.route("/downvote/<int:id>")
def downvote(id):
    vote(id, -1)
    return redirect(f"/joke/{id}")