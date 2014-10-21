from flask import Flask, render_template, request
import dbhelper
from time import strftime

test = Flask(__name__)

@test.route("/",methods=["GET"])
def main(titles=None):
    titles = ["Hello","bye"]
    return render_template("home.html",titles=titles)

if __name__ == "__main__":
    test.debug = True
    #app.run(host="0.0.0.0", port=1234)
    test.run()
