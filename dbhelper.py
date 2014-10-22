import sqlite3

conn = None
cursor = None

CREATE_TABLE_POSTS_QUERY = "CREATE TABLE IF NOT EXISTS posts (poster TEXT, title TEXT, content TEXT, date INTEGER)"
INSERT_TABLE_POSTS_QUERY = "INSERT INTO posts VALUES (?, ?, ?, ?)"
SELECT_TABLE_POSTS_WITH_TITLE = "SELECT title FROM posts WHERE title=?"
GET_TABLE_POSTS_QUERY = "SELECT * FROM posts"
GET_TABLE_POSTS_WITH_TITLE = "SELECT * FROM posts WHERE title=? LIMIT 1"
DELETE_POST_QUERY = "DELETE FROM posts WHERE poster=? AND title=? LIMIT 1"

CREATE_TABLE_COMMENTS_QUERY = "CREATE TABLE IF NOT EXISTS comments (post TEXT, commenter TEXT, content TEXT, date INTEGER)"
INSERT_TABLE_COMMENTS_QUERY = "INSERT INTO comments VALUES (?, ?, ?, ?)"
GET_TABLE_COMMENTS_QUERY = "SELECT * FROM comments WHERE post=?"
DELETE_COMMENT_QUERY = "DELETE FROM comments WHERE post=? AND commenter=? AND content=? LIMIT 1"

def connect():
    global conn, cursor
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()

def close():
    global conn
    conn.close()
    
def create_table_posts():
    cursor.execute(CREATE_TABLE_POSTS_QUERY)
    conn.commit()

def insert_post(poster, title, content, time):
    if (not has_post_with_title(title)):
        cursor.execute(INSERT_TABLE_POSTS_QUERY, (poster, title, content, time))
        conn.commit()
        return True
    else:
        return False

def has_post_with_title(title):
    return len(cursor.execute(SELECT_TABLE_POSTS_WITH_TITLE, (title,)).fetchall()) > 0
    
def get_post(title):
    return cursor.execute(GET_TABLE_POSTS_WITH_TITLE, (title,)).fetchall()

# Returns a tuple of each row of data
def get_posts():
    return cursor.execute(GET_TABLE_POSTS_QUERY).fetchall()

def delete_post(poster, title):
    cursor.execute(DELETE_POST_QUERY, (poster, title))
    conn.commit()
    
def create_table_comments():
    cursor.execute(CREATE_TABLE_COMMENTS_QUERY)
    conn.commit()

def insert_comment(post, commenter, content, time):
    cursor.execute(INSERT_TABLE_COMMENTS_QUERY, (post, commenter, content, time))
    conn.commit()

def delete_comment(post, commenter, content):
    cursor.execute(DELETE_COMMENT_QUERY, (post, commenter, content))
    conn.commit()

def get_comments(post):
    return cursor.execute(GET_TABLE_COMMENTS_QUERY, (post,)).fetchall()
'''
connect()
print get_posts()
close()
'''
