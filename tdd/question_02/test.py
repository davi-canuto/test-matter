#test.py

import unittest
import model

class TestFactorial(unittest.TestCase):
  def test_factorial_positivo(self):
    self.assertTrue(model.Factorial.calc(5) == 120)

  def test_factorial_zero(self):
    self.assertTrue(model.Factorial.calc(0) == 1)
    
  def test_factorial_negativo(self):
    with self.assertRaises(ValueError) as context:
      model.Factorial.calc(-1)
    self.assertTrue('Não existe fatorial de número negativo' in str(context.exception))

if __name__ == '__main__':
    unittest.main()