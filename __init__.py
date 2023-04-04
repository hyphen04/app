from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:passwd@localhost/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from posts.routes import posts_bp
from weather.routes import weather_bp

app.register_blueprint(posts_bp, url_prefix='/api')
app.register_blueprint(weather_bp, url_prefix='/api')
