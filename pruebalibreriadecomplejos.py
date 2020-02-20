import unittest
import libreriadecomplejos as lcc
import math
class TestStringMethods(unittest.TestCase):
    def testSuma(self):
        self.assertEqual(lcc.sumacomplejos([-3,2],[4,1]),[1,3])

    def testResta(self):
        self.assertEqual(lcc.restacomplejos([-3,2],[4,1]),[-7,1])

    def testMultiplicacion(self):
        self.assertEqual(lcc.multiplicacioncomplejos([-3,2],[4,1]),[-14,5])

    def testConjugado(self):
        self.assertEqual(lcc.conjugadocomplejo([-3,2]),[-3,-2])

    def testDivision(self):
        self.assertEqual(lcc.divisioncomplejos([3,-2],[5,4]),[7/41,-22/41])

    def testModulo(self):
        self.assertEqual(lcc.modulocomplejo([5,4]),math.sqrt(41))

    def testFaseNumeroComplejo(self):
        self.assertEqual(lcc.faseComplejo([5,4]),math.atan2(4,5))

    def testConversionComplejoPolar(self):
        self.assertEqual(lcc.conversionComplejoPolar([-2,2]),[2*math.sqrt(2),(3*math.pi)/4])

    def testConversionPolarComplejo(self):
        self.assertEqual(lcc.conversionPolarComplejo([math.sqrt(2)*2,(3*math.pi)/4]),[math.sqrt(2)*2*math.cos((3*math.pi)/4),math.sqrt(2)*2*math.sin((3*math.pi)/4)])


    def testMultiplicacionEscalarVector(self):
        v1 = [[[-2,5]],[[-1,-1]],[[2,-9]]]
        v2 = [-1,1]

        self.assertEqual(lcc.multiplicacionEscalarVectores(v1,v2),[[[-3,-7]],[[2,0]],[[7,11]]])

    def testAdicionMatriz(self):
        v1 = [[[-8,-3],[-6,-4],[0,-4]],
              [[-1,8],[6,-10],[8,-5]],
              [[4,0],[8,5],[-7,-9]]]

        v2 = [[[-7,-2],[-4,-2],[7,7]],
              [[5,9],[0,3],[6,-5]],
              [[1,5],[-6,-6],[5,8]]]

        self.assertEqual(lcc.adicionMatrices(v1,v2),[[[-15,-5],[-10,-6],[7,3]],[[4,17],[6,-7],[14,-10]],[[5,5],[2,-1],[-2,-1]]])

    def testInversoAditivoMatriz(self):
        v1 = [[[7,3],[-1,7]],[[-9,-4],[-7,-9]]]

        self.assertEqual(lcc.inversoAditivoMatrices(v1),[[[-7,-3],[1,-7]],[[9,4],[7,9]]])

    def testMultiplicacionEscalarMatriz(self):
        v1 = [[[3,-2],[8,-4]],[[4,-10],[-2,-8]]]
        v2 = [-2,3]

        self.assertEqual(lcc.multiplicacionEscalarMatrices(v1,v2),[[[0,13],[-4,32]],[[22,32],[28,10]]])

    def testTranspuestaMatriz(self):
        v1 = [[[5,9],[-7,-5],[-1,-4]],[[8,2],[-3,-7],[7,-8]]]

        self.assertEqual(lcc.transpuestaMatrizVector(v1),[[[5,9],[8,2]],[[-7,-5],[-3,-7]],[[-1,-4],[7,-8]]])

    def testConjugadoMatriz(self):
        v1 = [[[-6,1],[3,8]],[[2,-6],[3,0]]]

        self.assertEqual(lcc.conjugadoMatrizVector(v1),[[[-6,-1],[3,-8]],[[2,6],[3,0]]])

    def testAdjuntaMatriz(self):
        v1 = [[[7,7],[3,8],[8,4]],[[5,0],[8,-6],[-10,-1]]]

        self.assertEqual(lcc.adjuntaMatrizVector(v1),[[[7,-7],[5,0]],[[3,-8],[8,6]],[[8,-4],[-10,1]]])

    def testProductoMatriz(self):
        v1 = [[[-6,2],[0,6],[7,2]],
              [[6,9],[7,7],[-6,-6]],
              [[5,8],[-6,8],[6,9]]]

        v2 = [[[9,-6],[-3,-4],[5,-2]],
              [[3,6],[-1,-5],[0,-5]],
              [[9,9],[8,-4],[-8,-4]]]

        self.assertEqual(lcc.productoMatriz(v1,v2),[[[-33,153],[120,0],[-44,-22]],[[87,0],[-26,-117],[107,70]],[[0,165],[147,26],[69,-36]]])

    def testAccionMatrizSobreVector(self):
        v1 = [[[-1,5],[1,-7],[-6,3]],
              [[-3,-9],[2,-5],[1,-10]],
              [[-6,5],[6,-5],[3,-2]]]

        v2 = [[[1,-3]],
              [[4,3]],
              [[-3,1]]]

        self.assertEqual(lcc.accionMatrizSobreVector(v1,v2),[[[54,-32]],[[0,17]],[[41,30]]])

    def testProductoInterno(self):
        v1 = [[[2,-1]],
              [[-8,-5]],
              [[-2,-6]]]

        v2 = [[[6,-3]],
              [[5,-1]],
              [[-6,-2]]]

        self.assertEqual(lcc.productoInternoVector(v1,v2),[[[4,1]]])

    def testNorma(self):
        v1 = [[[4,5]],[[3,1]],[[0,-7]]]

        self.assertEqual(lcc.normaVector(v1),10)

    def testDistanciaVector(self):
        v1 = [[[2,7]],[[4,-1]],[[2,-4]]]
        v2 = [[[7,8]],[[2,-8]],[[1,4]]]

        self.assertEqual(lcc.distanciaVector(v1,v2),12)

    def testMatrizUnitaria(self):
        a = math.sqrt(2)

        v1 = [[[1/a,0],[0,1/a]],
              [[0,1/a],[1/a,0]]]

        v2 = [[[0,1],[1,0],[0,0]],
              [[0,0],[0,1],[1,0]],
              [[1,0],[0,0],[0,1]]]

        self.assertEqual(lcc.matrizUnitaria(v1),True)
        self.assertEqual(lcc.matrizUnitaria(v2),False)

    def testMatrizHermitiana(self):
        v1 = [[[3,0],[2,-1],[0,-3]],
              [[2,1],[0,0],[1,-1]],
              [[0,3],[1,1],[0,0]]]

        v2 = [[[1,0],[3,-1]],
              [[3,1],[0,1]]]

        self.assertEqual(lcc.matrizHermitiana(v1),True)
        self.assertEqual(lcc.matrizHermitiana(v2),False)

    def testProductoTensorial(self):
        v1 = [[[1,1],[0,0]],
              [[1,0],[0,1]]]

        v2 = [[[-1,2],[-2,-2],[0,2]],
              [[2,3],[3,1],[2,2]],
              [[-2,1],[1,-1],[2,1]]]

        v3 = [[[-3,1],[0,-4],[-2,2],[0,0],[0,0],[0,0]],
              [[-1,5],[2,4],[0,4],[0,0],[0,0],[0,0]],
              [[-3,-1],[2,0],[1,3],[0,0],[0,0],[0,0]],
              [[-1,2],[-2,-2],[0,2],[-2,-1],[2,-2],[-2,0]],
              [[2,3],[3,1],[2,2],[-3,2],[-1,3],[-2,2]],
              [[-2,1],[1,-1],[2,1],[-1,-2],[1,1],[-1,2]]]

        self.assertEqual(lcc.productoTensorialMatrizVector(v1,v2),v3)



if __name__ == '__main__':
    unittest.main()
