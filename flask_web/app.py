# flask_web/app.py
import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
        os.environ.get('POSTGRES_USER'),
        os.environ.get('POSTGRES_PASSWORD'),
        os.environ.get('POSTGRES_HOST'),
        os.environ.get('POSTGRES_PORT'),
        os.environ.get('POSTGRES_DB')
    )

DB_URL = "postgresql://test:test@{0}:5432/test".format(
		os.environ.get('POSTGRES_HOST')
	)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
print SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app=app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username



@app.route('/')
def hello_world():
    
    return jsonify(A=os.environ.get('A'),
            B=os.environ.get('B'),
            C=os.environ.get('C'),
            sql=SQLALCHEMY_DATABASE_URI,
            db=db
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
