
from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app.config.mysqlconnection import MySQLConnection

@app.route('/')
def index():
    return redirect("/dojos")

#dojos controller create
@app.route ("/create/dojo", methods=["POST"])
def create_dojo():
    Dojo.dojo_save(request.form)
    return redirect("/dojos")


#dojos controller read

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_dojos()
    return render_template("index.html", dojos=dojos)

@app.route("/dojo/<int:id>")
def get_a_dojo(id):
    data = {
        "id" : id
    }
    return render_template("dojo.html", the_dojos_ninjas=Dojo.get_a_dojo_with_ninjas(data))

