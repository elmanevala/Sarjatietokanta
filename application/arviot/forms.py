from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class ArvioKaavake(FlaskForm):

    arvio = StringField("Arvio: ", [validators.Length(min=2, message='Arvion oltava ainakin kaksi merkkiä.')], render_kw={"placeholder": "arvio"})
    sarja_id = StringField("sarja_id", [validators.Length(min=2, message='Sarjan oltava ainakin kaksi merkkiä.')], render_kw={"placeholder": "sarja"})  #kun sarjatietokanta on lisätty sovellukseen validator tarkistaa onko kyseista sarjaa olemassa
    katsottu = BooleanField("Katsottu loppuun")

    class Meta:
        csrf = False

class MuokkausKaavake(FlaskForm):

    arvio = StringField("Arvio: ", [validators.Length(min=2, message='Arvion oltava ainakin kaksi merkkiä.')], render_kw={"placeholder": "kirjoita uusi arvio"})
    katsottu = BooleanField("Muuta katsottu-statusta")

    class Meta:
        csrf = False