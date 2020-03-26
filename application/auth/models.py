from application import db

class Kayttaja(db.Model):

    __tablename__ = "kayttaja"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    nimi = db.Column(db.String(144), nullable=False)
    kayttajanimi = db.Column(db.String(144), nullable=False)
    salasana = db.Column(db.String(144), nullable=False)

    arviot = db.relationship("Arvio", backref='kayttaja', lazy=True)

    def __init__(self, nimi, kayttajanimi, salasana):
        self.nimi = nimi
        self.kayttajanimi = kayttajanimi
        self.salasana = salasana
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True