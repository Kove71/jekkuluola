from db import db

def get_jokes():
    result = db.session.execute("SELECT * FROM jokes")
    return result.fetchall()

def add_joke(content, user_id = 0):

    sql = "INSERT INTO jokes (content, created_at) VALUES (:content, NOW())"
    db.session.execute(sql, {"content": content})
    db.session.commit()