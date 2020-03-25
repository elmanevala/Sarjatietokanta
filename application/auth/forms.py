from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
  
class LoginForm(FlaskForm):
    kayttajanimi = StringField("Käyttäjänimi", render_kw={"placeholder": "käyttäjänimi"})
    salasana = PasswordField("Salasana", render_kw={"placeholder": "salasana"})
  
    class Meta:
        csrf = False