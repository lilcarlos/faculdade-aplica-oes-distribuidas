import unittest


# Código

def contador(palavra):

    lista = palavra.split()
    dicionario = {}

    for x in lista:
        if x in dicionario:
            dicionario[x] += 1
        else:
            dicionario[x] = 1
    return dicionario



# Funçoes para testar o codigo

class TestStringMethods(unittest.TestCase):

     def test_01_contador_retorna_dic(self):
         d=contador('o doce mais doce')
         self.assertEqual(type(d),type({'dicionario':'exemplo'}))

     def test_02_contador(self):
        d2=contador('esse exercício é um exercício fácil ou difícil')
        self.assertEqual(d2,{'é': 1, 'difícil': 1,
                            'esse': 1, 'ou': 1, 'um': 1, 'fácil': 1, 'exercício': 2})
        d3=contador('o doce perguntou ao doce qual é o doce mais doce '+
                    'e o doce respondeu ao doce que o doce mais doce é '+
                    'o doce de batata doce')
        self.assertEqual(d3['doce'],10)
        self.assertTrue('gato' not in d3)
        self.assertTrue('respondeu' in d3)
     
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

try:
    from gabarito_contador import *
    runTests()
except:
    pass


runTests()