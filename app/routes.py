from flask import jsonify
from app import app
from scrapper import hardmob


@app.route('/')
@app.route('/index')
def index():
    return "Hardmob API!"


@app.route('/latest')
def lastest_promo():
    raw_data = hardmob.scrap_hardmob()
    return jsonify(raw_data)
