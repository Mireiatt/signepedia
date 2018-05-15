from src import signepedia 
from flask import Flask
from flask import jsonify
from flask_cors import CORS
import requests
from src import bd
app = Flask(__name__)
CORS(app)

@app.route('/diccionari/<string:paraula>', methods=["GET"])
def consulta_paraula(paraula):
    entrada = signepedia.retorna_entrada(paraula, bd.connecta())
    return jsonify(entrada)
