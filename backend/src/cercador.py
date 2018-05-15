# Retornem si "paraula" esta registrada al diccionari.

def tenim_entrada(paraula, cnx):
    cursor = cnx.cursor()

    query = "SELECT COUNT(paraula) FROM diccionari WHERE Hex(LOWER(paraula)) LIKE Hex(LOWER(\"" + paraula  +"\"))"
    cursor.execute(query)
    registrada = cursor.fetchall()[0][0] != 0
    cursor.close()
    return registrada

# Retornem una entrada netejant la informació:
# - Dividim el camp "alternatives".
# - Eliminem els camps buits.

def neteja_entrada(entrada):
    entrada["alternatives"] = entrada["alternatives"].split("|")
    for key in list(entrada.keys()):
        if entrada[key] == "" or entrada[key] == [""]:
            del entrada[key]
    return entrada

# Retornem l'entrada del diccionari, d'una "paraula".

def obte_entrada(paraula, cnx):
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT * FROM diccionari WHERE Hex(LOWER(paraula)) LIKE Hex(LOWER(\"" + paraula + "\"))"
    cursor.execute(query)
    resultat = cursor.fetchall()
    cursor.close()
    if resultat:
        return neteja_entrada(resultat[0])
    return None
