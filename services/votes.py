from flask import session
from db import db

def vote(joke_id, vote):
    user_id = session["user_id"]
    sql = "SELECT * FROM votes WHERE joke_id=:joke_id AND user_id=:user_id"
    result = db.session.execute(sql, {"joke_id":joke_id, "user_id":user_id})
    if result.fetchone() == None:
        insert_vote(joke_id, vote)
    else:
        update_vote(joke_id, vote)

def get_votes(joke_id):
    sql = "SELECT SUM(vote) FROM votes WHERE joke_id=:joke_id"
    result = db.session.execute(sql, {"joke_id":joke_id})
    votes = result.fetchone()[0]
    return votes

def get_user_votes(username):
    sql = "SELECT SUM(V.vote) \
        FROM votes V, users U, jokes J \
        WHERE V.joke_id=J.id AND J.user_id=U.id AND U.username=:username"
    result = db.session.execute(sql, {"username":username})
    votes = result.fetchone()[0]
    if votes == None:
        return 0
    return votes

def insert_vote(joke_id, vote):
    user_id=session["user_id"]
    sql = "INSERT INTO votes (user_id, joke_id, vote) \
        VALUES (:user_id, :joke_id, :vote)"
    db.session.execute(sql, {"user_id":user_id, "joke_id":joke_id, "vote":vote})
    db.session.commit()

def update_vote(joke_id, vote):
    user_id=session["user_id"]
    sql = "UPDATE votes SET vote=:vote \
        WHERE user_id=:user_id AND joke_id=:joke_id"
    db.session.execute(sql, {"vote":vote, "user_id":user_id, "joke_id":joke_id})
    db.session.commit()
