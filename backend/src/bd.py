import mysql.connector
import json

def connecta():
    with open("dades_mysql.json") as arxiu_dades:
        dades = json.load(arxiu_dades)
        connexio = mysql.connector.connect(user=dades["user"], password=dades["password"], host="54.38.240.12", database="signepedia", use_pure=False)
    return connexio
