from app import db

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=False)
