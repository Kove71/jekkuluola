from flask import session
from db import db

def give_admin_rights(username):
    sql = "UPDATE users SET admin=TRUE WHERE username=:username"
    db.session.execute(sql, {"username":username})
    db.session.commit()

def ban_user(username):
    sql = "UPDATE users SET banned=TRUE WHERE username=:username AND admin=FALSE"
    db.session.execute(sql, {"username":username})
    db.session.commit()

def remove_joke(joke_id):
    sql = "UPDATE jokes SET visible=FALSE WHERE id=:joke_id"
    db.session.execute(sql, {"joke_id":joke_id})
    db.session.commit()
