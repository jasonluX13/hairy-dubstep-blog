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

@test.route("/<title>")
def blogpost(title=None,post=None,comments=None):
    dbhelper.connect()
    post = dbhelper.get_post(title)
    comments = dbhelper.get_comments(title)
    dbhelper.close()
    return render_template("blogpost.html",title=title,
                            post=post,
                            comments=comments)
    
if __name__ == "__main__":
    test.debug = True
    #app.run(host="0.0.0.0", port=6666)
    test.run(host="0.0.0.0",port=1212)
