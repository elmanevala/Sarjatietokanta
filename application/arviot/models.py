from application import db

class Arvio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kayttaja_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'),
                           nullable=False)
    sarja_id = db.Column(db.String(16), nullable=False)
    pvm_luotu = db.Column(db.DateTime, default=db.func.current_timestamp())
    pvm_muokattu = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

    arvio = db.Column(db.String(144), nullable=False)
    katsottu = db.Column(db.Boolean, nullable=False)

    def __init__(self, arvio, sarja_id):
        self.sarja_id = sarja_id
        self.arvio = arvio
        self.katsottu = False
