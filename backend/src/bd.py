import mysql.connector
import json
import os

def connecta():
    try:
        with open("dades_mysql.json") as arxiu_dades:
            dades = json.load(arxiu_dades)
    except "FileNotFoundError":
        dades = dict(user=os.environ["SIGNEPEDIA_MYSQL_USER"], password=os.environ["SIGNEPEDIA_MYSQL_PASSWORD"])
    connexio = mysql.connector.connect(user=dades["user"], password=dades["password"], host="54.38.240.12", database="signepedia", use_pure=False)
    return connexio
