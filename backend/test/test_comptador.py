from src import comptador
import unittest

class TestComptador(unittest.TestCase):

    ######################
    # Tests compta_unics #
    ######################

    # Comprovem que comptem degudament els casos diferents.

    def test_compta_unics(self):
        diccionaris = ("test/dicc/dicc1.csv", "test/dicc/dicc2.csv", "test/dicc/dicc3.csv")
        nEntrades = (2, 5, 3)
        camps = ("url", "on", "lletra")

        for dicc, n, camp in zip(diccionaris, nEntrades, camps):
            self.assertEqual(comptador.compta_unics(dicc, camp), n)
