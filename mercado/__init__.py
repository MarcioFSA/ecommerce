from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
app.config["SECRET_KEY"] = '0a7bfef6c00cdd67f65edfe0'
db.init_app(app)

from mercado import routes

# if __name__ == '__main__':
#     app.run(debug=True)
