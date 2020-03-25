from flask import render_template, request, redirect, url_for

from application import app, db
from application.arviot.models import Arvio
from application.arviot.forms import ArvioKaavake

@app.route("/arviot/", methods=["GET"])
def arviot_lista():
    return render_template("arviot/lista.html", arviot = Arvio.query.all())

@app.route("/arviot/uusi/")
def arviot_kaavio():
    return render_template("arviot/uusi.html", form = ArvioKaavake())


@app.route("/arviot/<arvio_id>/", methods=["POST"])     
def arvio_katsottu(arvio_id):

    a = Arvio.query.get(arvio_id)
    a.katsottu = True
    db.session().commit()
    
    return redirect(url_for("arviot_lista"))



@app.route("/arviot/", methods=["POST"])
def arviot_luo():

    form = ArvioKaavake(request.form)

    if not form.validate():
        return render_template("arviot/uusi.html", form = form)

    a = Arvio(form.arvio.data, form.sarja_id.data)
    a.katsottu = form.katsottu.data

    db.session().add(a)
    db.session().commit()
    
    return redirect(url_for("arviot_lista"))