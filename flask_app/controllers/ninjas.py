from flask import render_template, request, redirect
from flask_app import app
from flask_app.models import dojo
from flask_app.models import ninja

# create
@app.route ("/create/ninja", methods=["POST"])
def create_ninja():
    ninja.Ninja.ninja_save(request.form)
    return redirect("/")

# read 
@app.route("/ninjas")
def ninjas():
    return render_template("ninja.html", dojos=dojo.Dojo.get_dojos())