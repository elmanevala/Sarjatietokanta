from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    kayttajanimi = StringField("Käyttäjänimi", render_kw={"placeholder": "käyttäjänimi"})
    salasana = PasswordField("Salasana", render_kw={"placeholder": "salasana"})
  
    class Meta:
        csrf = False


class RegistrationForm(FlaskForm):
    nimi = StringField("Nimi", [validators.Length(min=3, message='Nimi vähintään kolme merkkiä pitkä')], render_kw={"placeholder": "nimi"})
    kayttajanimi = StringField("Käyttäjänimi", [validators.Length(min=3, message='Käyttäjänimi vähintään kolme merkkiä pitkä')], render_kw={"placeholder": "käyttäjänimi"})
    salasana = PasswordField("Salasana",  [validators.EqualTo('tarkistus', message='Salasanat eri')], render_kw={"placeholder": "salasana"}, )
    tarkistus = PasswordField("Salasana", render_kw={"placeholder": "salasana uudestaan"})

    class Meta:
        csrf = False