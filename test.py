from flask import Flask, render_template, request
import dbhelper
from time import strftime

test = Flask(__name__)

@test.route("/",methods=["GET","POST"])
def main(titles=None):
    if request.method == "GET":
        dbhelper.connect()
        #dbhelper.create_table_posts();
        titles = dbhelper.get_posts()
        dbhelper.close()
        return render_template("home.html",titles=titles)
    else:
        button = request.form["submit"]
        title = request.form["title"]
        text = request.form["textarea"]
        poster = request.form["author"]
        time = strftime("%a %d %b %Y %X")
        dbhelper.connect()
        dbhelper.insert_post(poster, title, text, time)
        titles = dbhelper.get_posts()
        dbhelper.close()
        return render_template("home.html",titles=titles)

@test.route("/<title>",methods=["GET","POST"])
def blogpost(title=None,post=None,comments=None):
    if request.method=="GET":
        dbhelper.connect()
        post = dbhelper.get_post(title)
        comments = dbhelper.get_comments(title)
        titles = dbhelper.get_posts()
        author=""
        for item in titles: 
            if item[1] == title: 
                author = item[0] 
                break
        dbhelper.close()
        return render_template("blogpost.html",title=title,author=author,
                            post=post,
                            comments=comments)
    else:
        button = request.form["submit"]
        poster = request.form["author"]
        text = request.form["textarea"]
        time = strftime("%a %d %b %Y %X")
        dbhelper.connect()
        dbhelper.insert_comment(title, poster, text, time)
        post = dbhelper.get_post(title)
        comments = dbhelper.get_comments(title)
        titles = dbhelper.get_posts()
        author=""
        for item in titles: 
            if item[1] == title: 
                author = item[0] 
                break
        dbhelper.close()
        return render_template("blogpost.html",title=title,author=author,
                               post=post,comments=comments)
    
if __name__ == "__main__":
    test.debug = True
    #app.run(host="0.0.0.0", port=6666)
    test.run(host="127.0.0.1",port=8080)
