from src import sinonims
import unittest
from src import bd


class TestSinonims(unittest.TestCase):

    ######################
    # Tests get_sinonims #
    ######################

    # Comprovem que obtenim tots els sinonims sense repeticions.
    # No en fem més per evitar enlentir les proves.

    def test_get_sinonims(self):
        self.assertEqual(sinonims.get_sinonims("prova"), ["assaig", "experiment", "experimentació", "intent", "provatura", "temptativa", "tempteig", "test", "demostració", "examen"])


    ########################
    # Tests troba_sinonims #
    ########################

    # Comprovem que retornem només els sinònims registrats.
    # No en fem més per evitar enlentir les proves.

    def test_troba_sinonims(self):
        cnx = bd.connecta()
        self.assertEqual(sinonims.troba_sinonims("escola", cnx), ["col·legi","estudi","institut"])
        self.assertEqual(sinonims.troba_sinonims("llamp", cnx), None)
        cnx.close()

if __name__ == '__main__':
    unittest.main()
