CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN,
    banned BOOLEAN
);

CREATE TABLE IF NOT EXISTS jokes (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INT REFERENCES users,
    created_at TIMESTAMP,
    visible BOOLEAN
);

CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users,
    joke_id INT REFERENCES jokes,
    comment TEXT,
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS votes (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users,
    joke_id INT REFERENCES jokes,
    vote INT
);

CREATE TABLE IF NOT EXISTS joke_tags (
    id SERIAL PRIMARY KEY,
    tag TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS tag_members (
    id SERIAL PRIMARY KEY,
    joke_id INT REFERENCES jokes,
    tag_id INT REFERENCES joke_tags
);

CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    sender_user_id INT REFERENCES users,
    receiver_user_id INT REFERENCES users,
    message TEXT,
    created_at TIMESTAMP
);