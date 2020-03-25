from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class ArvioKaavake(FlaskForm):

    arvio = StringField("Arvio: ", [validators.Length(min=2)], render_kw={"placeholder": "arvio"})
    sarja_id = StringField("sarja_id", [validators.Length(min=2)], render_kw={"placeholder": "sarja"})  #kun sarjatietokanta on lisätty sovellukseen validator tarkistaa onko kyseista sarjaa olemassa
    katsottu = BooleanField("Katsottu loppuun")

    class Meta:
        csrf = False