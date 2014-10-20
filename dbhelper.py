import sqlite3

conn = sqlite3.connect("blog.db")
cursor = conn.cursor()

CREATE_TABLE_POSTS_QUERY = "CREATE TABLE IF NOT EXISTS posts (poster TEXT, title TEXT, content TEXT, date INTEGER)"
INSERT_TABLE_POSTS_QUERY = "INSERT INTO posts VALUES (%s, %s, %s, %d)"
SELECT_TABLE_POSTS_WITH_TITLE = "SELECT title FROM posts WITH title=%s"
GET_TABLE_POSTS_QUERY = "SELECT * FROM posts"
DELETE_POST_QUERY = "DELETE FROM posts WHERE poster=%s AND title=%s LIMIT 1"

CREATE_TABLE_COMMENTS_QUERY = "CREATE TABLE IF NOT EXISTS comments (commenter TEXT, content TEXT, date INTEGER)"
INSERT_TABLE_COMMENTS_QUERY = "INSERT INTO comments VALUES (%s, %s, %s)"
GET_TABLE_COMMENTS_QUERY = "SELECT * FROM comments"
DELETE_COMMENT_QUERY = "DELETE FROM comments WHERE commenter=%s AND content=%s LIMIT 1"

def create_table_posts():
    cursor.execute(CREATE_TABLE_POSTS_QUERY)
    conn.commit()

def insert_post(poster, title, content, time):
    if (not has_post_with_title(title)):
        cursor.execute(INSERT_TABLE_POSTS_QUERY % (poster, title, content, time))
        conn.commit()
        return True
    else:
        return False

def has_post_with_title(title):
    return len(cursor.execute(SELECT_TABLE_POSTS_WITH_TITLE % title)) > 0
    
def get_posts():
    return cursor.execute(GET_TABLE_POSTS_QUERY)

def delete_post(poster, title):
    cursor.execute(DELETE_POST_QUERY % (poster, title))
    conn.commit()
    
def create_table_comments():
    cursor.execute(CREATE_TABLE_COMMENTS_QUERY)
    conn.commit()

def insert_comment(commenter, content, time):
    cursor.execute(INSERT_TABLE_COMMENTS_QUERY % (commenter, content, time))
    conn.commit()

def delete_comment(commenter, content):
    cursor.execute(DELETE_COMMENT_QUERY %s (commenter, content))
    conn.commit()
