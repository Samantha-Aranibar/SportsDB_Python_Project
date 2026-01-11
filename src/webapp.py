from flask import Flask, jsonify, request, render_template
from sportsdb.project import SportsDBClient

app = Flask(__name__)
client = SportsDBClient()

@app.route('/') #('/', methods=['GET'])
def home():
    return render_template('index.html')

