from flask import session
from db import db

def get_jokes_by_time():
    result = db.session.execute("SELECT U.username, J.content, J.created_at, J.id, SUM(V.vote) AS votesum \
        FROM jokes J, users U, votes V \
        WHERE U.id=J.user_id AND V.joke_id=J.id \
        GROUP BY J.id, J.content, J.created_at, U.username \
        ORDER BY J.created_at DESC")
    return result.fetchall()

def get_jokes_by_vote():
    result = db.session.execute("SELECT U.username, J.content, J.created_at, J.id, SUM(V.vote) AS votesum \
        FROM jokes J, users U, votes V \
        WHERE U.id=J.user_id AND V.joke_id=J.id \
        GROUP BY J.id, J.content, J.created_at, U.username \
        ORDER BY votesum DESC")
    return result.fetchall()

def add_joke(content):
    user_id = session["user_id"]
    sql = "INSERT INTO jokes (content, user_id, created_at) \
        VALUES (:content, :user_id, NOW()) RETURNING id"
    result = db.session.execute(sql, {"content": content, "user_id":user_id})
    db.session.commit()
    return result.fetchone()[0]

def get_user_jokes(username):
    sql = "SELECT U.username, J.id, J.content, J.created_at \
        FROM jokes J, users U \
        WHERE U.id=J.user_id AND U.username=:username \
        ORDER BY J.created_at DESC"
    result = db.session.execute(sql, {"username":username})
    return result.fetchall()

def get_jokepage_joke(joke_id):
    sql = "SELECT U.username, J.id, J.content, J.created_at \
        FROM users U, jokes J \
        WHERE J.user_id=U.id AND J.id=:joke_id"
    result = db.session.execute(sql, {"joke_id":joke_id})
    return result.fetchone()
