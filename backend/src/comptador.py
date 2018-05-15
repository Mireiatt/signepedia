import pandas as pd

# Compta els elements diferents que hi ha en un csv

def compta_unics(ruta_dades, camp):
    df = pd.read_csv(ruta_dades, na_values="")
    unics = len(df[camp].unique())
    for x in df[camp].values:
        if x != x: #Comprovem si és NaN
            return unics - 1
    return unics
