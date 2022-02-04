from flask import session
from db import db

def get_jokes():
    result = db.session.execute("SELECT U.username, J.content, J.created_at FROM jokes J, users U WHERE U.id=J.user_id ORDER BY J.created_at DESC")
    return result.fetchall()

def add_joke(content):
    user_id = session["user_id"]
    sql = "INSERT INTO jokes (content, user_id, created_at) VALUES (:content, :user_id, NOW())"
    db.session.execute(sql, {"content": content, "user_id":user_id})
    db.session.commit()

def get_user_jokes(username):
    sql = "SELECT U.username, J.content, J.created_at FROM jokes J, users U WHERE U.id=J.user_id AND U.username=:username ORDER BY J.created_at DESC"
    result = db.session.execute(sql, {"username":username})
    return result.fetchall()
