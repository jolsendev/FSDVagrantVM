# "Database code" for the DB Forum.

import datetime

import psycopg2 as psycopg2

POSTS = [("This is the first post.", datetime.datetime.now())]


def get_posts():
    """Return all posts from the 'database', most recent first."""
    return reversed(POSTS)


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    conn = psycopg2.connect("dbname=forum")
    cur = conn.cursor()
    cur.execute('INSERT INTO posts (text, time, id) VALUES (%s, %s)', (content, datetime.datetime.now()))
    conn.commit()
    cur.close()
    conn.close()