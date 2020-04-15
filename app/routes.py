from flask import jsonify
from app import app
from scrapper import hardmob
from flask_jwt import jwt_required


@app.route('/')
@app.route('/index')
def index():
    return "Hardmob API!"


@app.route('/latest')
@jwt_required()
def latest_promo():
    raw_data = hardmob.scrap_hardmob()
    return jsonify(raw_data)
