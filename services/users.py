from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
from db import db


def create_user(username, password):
    hashed_pw = generate_password_hash(password)
    sql = "INSERT INTO users (username, password, admin, banned) VALUES (:username, :password, FALSE, FALSE)"
    db.session.execute(sql, {
        "username": username,
        "password": hashed_pw
    })
    db.session.commit()


def user_login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return True
        else:
            return False

def user_logout():
    del session["user_id"]

def get_session_user():
    try:
        user_id = session["user_id"]
        sql = "SELECT username, admin FROM users WHERE id=:user_id"
        result = db.session.execute(sql, {"user_id":user_id})
        return result.fetchone()
    except Exception:
        return False