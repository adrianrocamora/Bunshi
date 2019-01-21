from bunshi import app
from bunshi.image import getImage
from flask import flash, render_template, session, request

recent = []
recentMax = 5

@app.route("/", methods = ["POST", "GET"])
def home():
    flash(recent)
    compound = ""
    imageSource = ""
    pageURL = ""

    try:
        if request.method == "POST":
            posts = request.form
            for post in posts.items():
                compound = post[1].lower()

            links = getImage(compound)
            imageSource = links[0]
            pageURL = links[1]

            if compound in recent:
                recent.remove(compound)
            recent.insert(0, compound)

            if len(recent) > recentMax:
                recent.pop(-1)

        return render_template("home.html",
                               error = False
                               imageSource = imageSource,
                               compound = compound,
                               pageURL = pageURL,
                               recent = recent)

    except TypeError as e:

        return render_template("home.html",
                               error = True,
                               compound = compound,
                               recent = recent)
