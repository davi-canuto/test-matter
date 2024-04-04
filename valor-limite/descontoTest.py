# tests.py

import unittest
import desconto
import unittest

class TestDesconto(unittest.TestCase):
    def test_idade_dependente_invalida(self):
        # Casos de teste para idade do dependente inválida
        self.assertEqual(desconto.calcular_desconto(300, -1), "Idade do dependente inválida")  # Abaixo do mínimo
        self.assertEqual(desconto.calcular_desconto(300, 25), "Idade do dependente inválida")  # Acima do máximo

    def test_valor_compra_abaixo_minimo(self):
        # Casos de teste para valor da compra abaixo do mínimo
        self.assertEqual(desconto.calcular_desconto(249, 10), "Valor da compra abaixo do mínimo")  # Abaixo do mínimo

    def test_desconto(self):
        # Casos de teste para desconto baseado na idade do dependente
        self.assertEqual(desconto.calcular_desconto(300, 10), 45.0)  # 15% de desconto para idade <= 12
        self.assertEqual(desconto.calcular_desconto(400, 15), 48.0)  # 12% de desconto para 12 < idade <= 18
        self.assertEqual(desconto.calcular_desconto(500, 20), 25.0)  # 5% de desconto para 18 < idade <= 21
        self.assertEqual(desconto.calcular_desconto(600, 24), 18.0)  # 3% de desconto para 21 < idade <= 24

    def test_valores_limites(self):
        # Casos de teste para valores limites
        self.assertEqual(desconto.calcular_desconto(250, 0), 37.5)  # Mínimo valor de compra e idade
        self.assertEqual(desconto.calcular_desconto(250, 12), 37.5)  # Mínimo valor de compra e idade
        self.assertEqual(desconto.calcular_desconto(250, 24), 7.5)   # Mínimo valor de compra e máxima idade para desconto

        self.assertEqual(desconto.calcular_desconto(1000, 0), 150.0)  # Máximo valor de compra e idade
        self.assertEqual(desconto.calcular_desconto(1000, 24), 30.0)  # Máximo valor de compra e idade



if __name__ == '__main__':
    unittest.main()
