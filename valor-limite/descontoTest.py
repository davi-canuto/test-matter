# tests.py

import unittest
import desconto
import unittest

class TestDesconto(unittest.TestCase):
    def test_validar_forma(self):
        desconto.calcular_desconto(249, 12)  # Valor da compra abaixo do mínimo


if __name__ == '__main__':
    unittest.main()
