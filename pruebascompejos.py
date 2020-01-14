import unittest
import complejos


class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        z1=(1,2)
        z2=(2,3)
        self.assertEqual(complejos.suma(z1,z2), (3, 5))
    def test_resta(self):
        z1=(1,2)
        z2=(2,3)
        self.assertEqual(complejos.resta(z1,z2), (-1, -1))
       
    def test_multiplicacion(self):
        z1=(1,2)
        z2=(2,3)
        self.assertEqual(complejos.multiplicacion(z1,z2), (-4, 7))

    def test_division(self):
        z1=(1,2)
        z2=(2,3)
        self.assertEqual(complejos.division(z1,z2), (0.6153846153846154, 0.07692307692307693))

    def test_modulo(self):
        z1=(1,2)
        
        self.assertEqual(complejos.modulo(z1), 2.23606797749979)
    def test_conujugada(self):
        z1=(1,2)
        
        self.assertEqual(complejos.conjugada(z1), (1, -2))
    def test_polares(self):
        z1=(1,2)
        
        self.assertEqual(complejos.polares(z1), (2.23606797749979, 1.1071487177940904))



if __name__ == '__main__':
    unittest.main()
   
def main():
    z1=(1,2)
    z2=(2,3)
main()
