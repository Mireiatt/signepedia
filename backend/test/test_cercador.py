from src import cercador
import unittest
from src import bd

class TestCercador(unittest.TestCase):

    #######################
    # Tests tenim_entrada #
    #######################

    # Comprovem que respon correctament
    def test_tenim_entrada(self):
        cnx = bd.connecta()
        self.assertTrue(cercador.tenim_entrada("zebra", cnx))
        self.assertTrue(cercador.tenim_entrada("cloïssa", cnx))
        self.assertFalse(cercador.tenim_entrada("qkañ", cnx))
        self.assertFalse(cercador.tenim_entrada("brunada", cnx))
        cnx.close()

    ########################
    # Tests neteja_entrada #
    ########################
    def test_neteja_entrada(self):
        self.assertEqual(cercador.neteja_entrada(dict(a="foo",b="",c="bar",alternatives="")),dict(a="foo",c="bar"))
        self.assertEqual(cercador.neteja_entrada(dict(paraula="Hola",alternatives="Hola què tal?|Bon dia|Hola i adéu")),dict(paraula="Hola",alternatives=["Hola què tal?","Bon dia","Hola i adéu"]))

    ######################
    # Tests obte_entrada #
    ######################

    # Comprovem que una entrada no registrada no retorna res.
    def test_obte_senseresultat(self):
        cnx = bd.connecta()
        self.assertEqual(cercador.obte_entrada("bermell", cnx), None)
        self.assertEqual(cercador.obte_entrada("", cnx), None)
        self.assertEqual(cercador.obte_entrada("¿ ?", cnx), None)
        cnx.close()

    # Comprovem que el matching de la paraula amb diferents paràmetres de l'entrada és correcte.
    def test_obte_entrada(self):
        paraules = ("adreça", "1.000", "sant just", "ajudar-me", "abans")
        paraulesReg = ("adreça", "1.000", "Sant Just", "ajudar-me", "abans")
        urls = ("videos/adreça.mp4", "https://www.youtube.com/embed/LqaR9NO8hmk", "https://www.youtube.com/embed/oawVAxU7wVA", "https://www.youtube.com/embed/XjsjQ_NUYJM", "https://www.youtube.com/embed/VMHoIzjYXt0")

        cnx = bd.connecta()
        for paraula, paraulaReg, url in zip(paraules, paraulesReg, urls):
            entrada = cercador.obte_entrada(paraula, cnx)
            self.assertEqual(entrada["paraula"], paraulaReg)
            self.assertFalse("sinonims" in entrada)
            self.assertFalse("correccio" in entrada)
            self.assertEqual(entrada["url"], url)
        cnx.close()

    def test_obte__alternatives(self):
        paraules = ("AJUDANT", "abans", "amèrica")
        alternatives_v = (["ajudant (a la feina)", "ajudant (auxiliar)"],["abans d'ahir"],["americà","Amèrica (continent)", "Amèrica central", "Amèrica del nord", "Amèrica del sud"])

        cnx = bd.connecta()
        for paraula, alternatives in zip(paraules, alternatives_v):
            self.assertEqual(cercador.obte_entrada(paraula, cnx)["alternatives"], alternatives)
        self.assertFalse("alternatives" in cercador.obte_entrada("abril", cnx))
        cnx.close()

if __name__ == '__main__':
    unittest.main()
