from application import db

class Arvio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kayttaja_id = db.Column(db.String(16), nullable=True)
    sarja_id = db.Column(db.String(16), nullable=False)
    pvm_luotu = db.Column(db.DateTime, default=db.func.current_timestamp())
    pvm_muokattu = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

    arvio = db.Column(db.String(144), nullable=False)
    katsottu = db.Column(db.Boolean, nullable=False)

    def __init__(self, arvio):
        self.sarja_id = "sarjanNimi"
        self.arvio = arvio
        self.katsottu = False
