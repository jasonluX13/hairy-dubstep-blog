from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home(titles=None):
    if request.method == "POST":
        return render_template("home.html",titles=titles)
    else:
        # get stuff from form
        # add stuff from form to database
        # update home page 
        


@app.route("/<title>")
def blogpost(title=None,post=None,comments=None):
    return render_template("blogpost.html",title=title,post=post,comments=comments)

    


if __name__ == "__main__":
app.debug = True
app.run(host="0.0.0.0", port=1234)
