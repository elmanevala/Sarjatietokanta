from flask import render_template, request, redirect, url_for

from application import app, db
from application.auth.models import Kayttaja
from application.auth.forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user

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


    login_user(kayttaja)
    return redirect(url_for("index")) 


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/registration")
def auth_register():
    return render_template("auth/registrationform.html", form = RegistrationForm())


@app.route("/auth/", methods=["POST"])
def auth_uusiKayttaja():

    form = RegistrationForm(request.form)

    if not form.validate():
        return render_template("auth/registrationform.html", form = form)

    k = Kayttaja(form.nimi.data, form.kayttajanimi.data, form.salasana.data)

    db.session().add(k)
    db.session().commit()
    
    return redirect(url_for("auth_login"))