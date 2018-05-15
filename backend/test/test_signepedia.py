from src import signepedia
import unittest
from src import bd

class TestSignepedia(unittest.TestCase):

    #########################
    # Tests retorna_entrada #
    #########################

    # Comprovem que estem retornant totes les entrades com hauríem.
    # No fem més de sinònims ni correcció per evitar enlentir els tests.
    def test_entrada_registrada(self):
        paraules = ("Màster", "sant jordi")
        entrades = (dict(paraula="màster",url="videos/màster.mp4",autor="Tània Tebé"), dict(paraula="Sant Jordi",url="https://www.youtube.com/embed/CG_5OFGV4NI",autor="generalitat"))

        cnx = bd.connecta()
        for paraula, entrada in zip(paraules, entrades):
            self.assertEqual(signepedia.retorna_entrada(paraula, cnx), entrada)
        cnx.close()

    def test_entrada_camps(self):
        paraules = ("abans", "amèrica")
        entrades = (dict(paraula="abans",url="https://www.youtube.com/embed/VMHoIzjYXt0",autor="frosinor85",alternatives=["abans d'ahir"],sinonims=["anteriorment","primer"]), dict(paraula="Amèrica",alternatives=["americà","Amèrica (continent)","Amèrica central","Amèrica del nord","Amèrica del sud"]))
        
        cnx = bd.connecta()
        for paraula, entrada in zip(paraules, entrades):
            self.assertEqual(signepedia.retorna_entrada(paraula, cnx), entrada)
        self.assertEqual(signepedia.retorna_entrada("Roig", cnx), {"paraula": "Roig", "sinonims": ["vermell"]})
        self.assertEqual(signepedia.retorna_entrada("Vlau", cnx), {"paraula": "Vlau", "correccio": "Blau"})
        cnx.close()

if __name__ == '__main__':
    unittest.main()
