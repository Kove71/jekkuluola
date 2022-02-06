from flask import session
from db import db

def get_comments(joke_id):
    sql = "SELECT U.username, J.id, C.comment, C.created_at FROM users U, comments C, jokes J WHERE C.joke_id=J.id AND C.user_id=U.id AND J.id=:joke_id ORDER BY C.created_at DESC"
    result = db.session.execute(sql, {"joke_id":joke_id})
    return result.fetchall()

def add_comment(joke_id, comment):
    user_id = session["user_id"]
    sql = "INSERT INTO comments (comment, user_id, joke_id, created_at) VALUES (:comment, :user_id, :joke_id, NOW())"
    db.session.execute(sql, {"comment": comment, "user_id":user_id, "joke_id":joke_id})
    db.session.commit()
