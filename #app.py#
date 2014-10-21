from flask import Flask, render_template, request
import dbhelper
from time import strftime

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home(titles=None):
    dbhelper.create_table_posts()
    if request.method == "POST":
        titles = dbhelper.get_posts()
        return render_template("home.html",titles=titles)
    else:
        # get stuff from form
        button = request.form["submit"]
        title = request.form["title"]
        text = request.form["textarea"]
        poster = request.form["author"]
        time = strftime("%a %d %b %Y %X")
        # add stuff from form to database
        
        dbhelper.insert_post(poster, title, text, time)
        # update home page 
        titles = dbhelper.get_posts()
        return render_template("home.html",titles=titles)


@app.route("/<title>")
def blogpost(title=None,post=None,comments=None):
    return render_template("blogpost.html",
                            title=title,
                            post=post,
                            comments=comments)

    


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=1234)
