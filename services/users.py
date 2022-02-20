from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
from db import db
from sqlalchemy import exc

def create_user(username, password, second_password):
    if not username or not password or not second_password:
        return 1
    if password != second_password:
        return 2
    hashed_pw = generate_password_hash(password)
    sql = "INSERT INTO users (username, password, admin, banned) VALUES (:username, :password, FALSE, FALSE)"
    try:
        db.session.execute(sql, {
            "username": username,
            "password": hashed_pw
        })
        db.session.commit()
        return 0
    except exc.IntegrityError:
        return 3

def user_login(username, password):
    sql = "SELECT id, password, banned FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return 1
    elif user.banned:
        return 2
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            return 0
        else:
            return 3

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

def give_admin_rights(username):
    sql = "UPDATE users SET admin=TRUE WHERE username=:username"
    db.session.execute(sql, {"username":username})
    db.session.commit()

def ban_user(username):
    sql = "UPDATE users SET banned=TRUE WHERE username=:username"
    db.session.execute(sql, {"username":username})
    db.session.commit()