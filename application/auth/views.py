from flask import render_template, request, redirect, url_for

from application import app
from application.auth.models import Kayttaja
from application.auth.forms import LoginForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    kayttaja = Kayttaja.query.filter_by(kayttajanimi=form.kayttajanimi.data, salasana=form.salasana.data).first()
    if not kayttaja:
        return render_template("auth/loginform.html", form = form,
                               error = "Ei käyttäjänimeä tai salasanaa")


    print("Käyttäjä " + kayttaja.nimi + " tunnistettiin")
    return redirect(url_for("index")) 