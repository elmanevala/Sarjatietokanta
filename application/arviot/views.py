from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.arviot.models import Arvio
from application.arviot.forms import ArvioKaavake, MuokkausKaavake

@app.route("/arviot/", methods=["GET"])
@login_required
def arviot_lista():
    return render_template("arviot/lista.html", arviot = Arvio.query.filter(Arvio.kayttaja_id == current_user.id))

@app.route("/arviot/uusi/")
@login_required
def arviot_kaavio():
    return render_template("arviot/uusi.html", form = ArvioKaavake())

@app.route("/arviot/muokkaus/")
@login_required
def arviot_muokkausnakyma():
    return render_template("arviot/muokkaus.html", form = MuokkausKaavake())


@app.route("/arviot/<arvio_id>/poisto", methods=["POST"]) 
@login_required
def arvio_katsottu(arvio_id):

    a = Arvio.query.get(arvio_id)
    a.katsottu = True
    db.session().commit()
    
    return redirect(url_for("arviot_lista"))


@app.route("/arviot/<arvio_id>/", methods=["POST"]) 
@login_required
def arvio_poisto(arvio_id):

    Arvio.query.filter(Arvio.id == arvio_id).delete()
    db.session().commit()   

    return redirect(url_for("arviot_lista"))



@app.route("/arviot/", methods=["POST"])
@login_required
def arviot_luo():

    form = ArvioKaavake(request.form)

    if not form.validate():
        return render_template("arviot/uusi.html", form = form)

    a = Arvio(form.arvio.data, form.sarja_id.data)
    a.katsottu = form.katsottu.data
    a.kayttaja_id = current_user.id

    db.session().add(a)
    db.session().commit()
    
    return redirect(url_for("arviot_lista"))



@app.route("/arviot/muokkaus", methods=["GET", "POST"])
@login_required
def arviot_muokkaus():

    return redirect(url_for("arviot_muokkausnakyma"))



