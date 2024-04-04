# tests.py

import unittest
import triangulo
import unittest

class TestTriangulo(unittest.TestCase):
    def test_validar_forma(self):
        # Classes válidas
        self.assertTrue(triangulo.Triangulo(3, 4, 5).validarForma())  # Triângulo válido
        self.assertTrue(triangulo.Triangulo(5, 5, 5).validarForma())  # Triângulo válido
        self.assertTrue(triangulo.Triangulo(5, 5, 7).validarForma())  # Triângulo válido
        # Classes inválidas
        self.assertFalse(triangulo.Triangulo(1, 2, 3).validarForma())  # Triângulo inválido
        self.assertFalse(triangulo.Triangulo(2, 3, 6).validarForma())  # Triângulo inválido
        self.assertFalse(triangulo.Triangulo(0, 2, 3).validarForma())  # Triângulo inválido
        self.assertFalse(triangulo.Triangulo(-1, 2, 3).validarForma())  # Triângulo inválido

    def test_eh_equilatero(self):
        # Classes válidas
        self.assertTrue(triangulo.Triangulo(5, 5, 5).ehEquilatero())  # Triângulo Equilátero
        # Classes inválidas
        self.assertFalse(triangulo.Triangulo(3, 4, 5).ehEquilatero())  # Triângulo não é Equilátero

    def test_eh_isosceles(self):
        # Classes válidas
        self.assertTrue(triangulo.Triangulo(5, 5, 7).ehIsosceles())  # Triângulo Isósceles
        # Classes inválidas
        self.assertFalse(triangulo.Triangulo(3, 4, 5).ehIsosceles())  # Triângulo não é Isósceles

    def test_eh_escaleno(self):
        # Classes válidas
        self.assertTrue(triangulo.Triangulo(3, 4, 5).ehEscaleno())  # Triângulo Escaleno
        # Classes inválidas
        self.assertFalse(triangulo.Triangulo(5, 5, 5).ehEscaleno())  # Triângulo não é Escaleno

    def test_valores_limites(self):
        # Casos de teste para valores mínimos
        self.assertTrue(triangulo.Triangulo(1, 1, 1).validarForma())  # Mínimos
        self.assertTrue(triangulo.Triangulo(1, 1, 1).ehEquilatero())  # Mínimos
        self.assertTrue(triangulo.Triangulo(1, 2, 2).ehIsosceles())  # Mínimos
        self.assertTrue(triangulo.Triangulo(2, 3, 4).ehEscaleno())  # Mínimos

        # Casos de teste para valores máximos
        self.assertTrue(triangulo.Triangulo(100, 100, 100).validarForma())  # Máximos
        self.assertTrue(triangulo.Triangulo(100, 100, 100).ehEquilatero())  # Máximos
        self.assertFalse(triangulo.Triangulo(100, 100, 100).ehIsosceles())  # Máximos
        self.assertFalse(triangulo.Triangulo(100, 100, 100).ehEscaleno())  # Máximos

        # Casos de teste para valores extremos
        self.assertTrue(triangulo.Triangulo(50, 51, 51).validarForma())  # Extremos
        self.assertFalse(triangulo.Triangulo(50, 51, 51).ehEquilatero())  # Extremos
        self.assertTrue(triangulo.Triangulo(50, 51, 51).ehIsosceles())  # Extremos
        self.assertFalse(triangulo.Triangulo(50, 51, 51).ehEscaleno())  # Extremos

        # Casos de teste para valores nulos ou negativos
        self.assertFalse(triangulo.Triangulo(0, 1, 1).validarForma())  # Nulos ou negativos
        self.assertFalse(triangulo.Triangulo(0, 1, 1).ehEquilatero())  # Nulos ou negativos
        self.assertFalse(triangulo.Triangulo(0, 1, 1).ehIsosceles())  # Nulos ou negativos
        self.assertFalse(triangulo.Triangulo(0, 1, 1).ehEscaleno())  # Nulos ou negativos

        self.assertFalse(triangulo.Triangulo(-1, 1, 1).validarForma())  # Nulos ou negativos
        self.assertFalse(triangulo.Triangulo(-1, 1, 1).ehEquilatero())  # Nulos ou negativos
        self.assertFalse(triangulo.Triangulo(-1, 1, 1).ehIsosceles())  # Nulos ou negativos
        self.assertFalse(triangulo.Triangulo(-1, 1, 1).ehEscaleno())  # Nulos ou negativos
        self.assertFalse(triangulo.Triangulo(1, 0, 1).validarForma())  # Nulos ou negativos

if __name__ == '__main__':
    unittest.main()
