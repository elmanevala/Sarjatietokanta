from flask import render_template, request, redirect, url_for

from application import app, db
from application.arviot.models import Arvio

@app.route("/arviot/", methods=["GET"])
def arviot_lista():
    return render_template("arviot/lista.html", arviot = Arvio.query.all())

@app.route("/arviot/uusi/")
def arviot_kaavio():
    return render_template("arviot/uusi.html")


@app.route("/arviot/<arvio_id>/", methods=["POST"])
def arvio_katsottu(arvio_id):

    a = Arvio.query.get(arvio_id)
    a.katsottu = True
    db.session().commit()
    
    return redirect(url_for("arviot_lista"))



@app.route("/arviot/", methods=["POST"])
def arviot_luo():
    a = Arvio(request.form.get("arvio"))

    db.session().add(a)
    db.session().commit()
    
    return redirect(url_for("arviot_lista"))