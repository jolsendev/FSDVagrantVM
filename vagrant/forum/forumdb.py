# "Database code" for the DB Forum.

import datetime

import psycopg2 as psycopg2


def get_posts():
    """Return all posts from the 'database', most recent first."""
    posts = [("This is the first post.", datetime.datetime.now())]
    conn = psycopg2.connect("dbname=forum")
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts;")
    all_posts = cur.fetchall()

    for post in all_posts:
        content = post[0]
        time = post[1]
        post_tuple = (content, time)
        posts.append(post_tuple)

    conn.commit()
    cur.close()
    conn.close()
    return reversed(posts)


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    conn = psycopg2.connect("dbname=forum")
    cur = conn.cursor()
    cur.execute('INSERT INTO posts (content, time) VALUES (%s, %s)', (content, datetime.datetime.now()))
    conn.commit()
    cur.close()
    conn.close()
