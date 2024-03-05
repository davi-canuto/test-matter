import unittest
from fracao import Fracao

class FracaoTest(unittest.TestCase):
  def test_Fracao_ok(self):
    Fracao(1, 2)
 
  def test_Fracao_bad_type_numerador(self):
    Fracao(1, 2)

  def test_Fracao_bad_type_denominador(self):
    Fracao(1, 2)

  def test_Fracao_denominador_zero(self):
    Fracao(0, 1)

  def test_Fracao_subtrair(self):
    f1 = Fracao(2, 1)
    f2 = Fracao(2, 3)
    resultado = f1.subtracao(f2)

    self.assertEqual(4, resultado.numerador)
    self.assertEqual(3, resultado.denominador)
    
  def test_Fracao_somar(self):
    f1 = Fracao(2, 1)
    f2 = Fracao(2, 3)
    resultado = f1.soma(f2)

    self.assertEqual(8, resultado.numerador)
    self.assertEqual(3, resultado.denominador)

  def test_Fracao_multiplicar(self):
    f1 = Fracao(2, 1)
    f2 = Fracao(2, 3)
    resultado = f1.multiplicar(f2)

    self.assertEqual(4, resultado.numerador)
    self.assertEqual(3, resultado.denominador)
    
  def test_Fracao_dividir(self):
    f1 = Fracao(2, 1)
    f2 = Fracao(2, 3)
    resultado = f1.dividir(f2)

    self.assertEqual(6, resultado.numerador)
    self.assertEqual(2, resultado.denominador)
    
  def test_Fracao_simplificar(self):
    f1 = Fracao(10, 6)
    resultado_f1 = f1.reduzir()

    self.assertEqual(3, resultado_f1.denominador)
    self.assertEqual(5, resultado_f1.numerador)
    
if __name__ == '__main__':
  unittest.main()