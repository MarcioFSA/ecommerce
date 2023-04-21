from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from mercado import routes

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)