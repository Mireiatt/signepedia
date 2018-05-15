from src import corrector
import unittest
from src import bd

class TestCorrector(unittest.TestCase):

    ######################
    # Tests get_correcio #
    ######################

    # Comprovem que les peticions a LanguageTool es fan correctament.
    # No en fem més per evitar saturar el servidor.

    def test_obte_correccio(self):
        correccions = corrector.get_correccio("clase")
        self.assertEqual(correccions[0], "classe")
        self.assertEqual(correccions[1], "casa")

    def test_falla(self):
        self.assertEqual(corrector.get_correccio("jksdfjfqp"), None)
        self.assertEqual(corrector.get_correccio("sant jordi"), None)

    ###########################
    # Tests corregeix_paraula #
    ###########################

    # Comprovem que es retorna correctament una entrada amb la seva correcció, si la tenim registrada.
    # No en fem més per evitar saturar el servidor.

    def test_corregeix_paraula(self):
        cnx = bd.connecta()
        self.assertEqual(corrector.corregeix_paraula("master", cnx), {"paraula": "master", "correccio": "màster"})
        self.assertEqual(corrector.corregeix_paraula("miñisteri", cnx), {"paraula": "miñisteri"})
        cnx.close()

if __name__ == '__main__':
    unittest.main()
