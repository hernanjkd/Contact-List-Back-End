from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True)
    address = db.Column(db.String(120))
    gender = db.Column(db.String(1))
    image_url = db.Column(db.String(120))

    def __repr__(self):
        return '<Person %r>' % self.fullname

    def serialize(self):
        return {
            "id": self.id,
            "fullname": self.fullname,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "gender": self.gender,
            "image_url": self.image_url
        }