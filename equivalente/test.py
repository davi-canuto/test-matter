# tests.py

import unittest
import model, datetime
import unittest

class TestTriangulo(unittest.TestCase):
    def test_validar_forma(self):
        # Classes válidas
        self.assertTrue(model.Triangulo(3, 4, 5).validarForma())  # Triângulo válido
        self.assertTrue(model.Triangulo(5, 5, 5).validarForma())  # Triângulo válido
        self.assertTrue(model.Triangulo(5, 5, 7).validarForma())  # Triângulo válido
        # Classes inválidas
        self.assertFalse(model.Triangulo(1, 2, 3).validarForma())  # Triângulo inválido
        self.assertFalse(model.Triangulo(2, 3, 6).validarForma())  # Triângulo inválido
        self.assertFalse(model.Triangulo(0, 2, 3).validarForma())  # Triângulo inválido
        self.assertFalse(model.Triangulo(-1, 2, 3).validarForma())  # Triângulo inválido

    def test_eh_equilatero(self):
        # Classes válidas
        self.assertTrue(model.Triangulo(5, 5, 5).ehEquilatero())  # Triângulo Equilátero
        # Classes inválidas
        self.assertFalse(model.Triangulo(3, 4, 5).ehEquilatero())  # Triângulo não é Equilátero

    def test_eh_isosceles(self):
        # Classes válidas
        self.assertTrue(model.Triangulo(5, 5, 7).ehIsosceles())  # Triângulo Isósceles
        # Classes inválidas
        self.assertFalse(model.Triangulo(3, 4, 5).ehIsosceles())  # Triângulo não é Isósceles

    def test_eh_escaleno(self):
        # Classes válidas
        self.assertTrue(model.Triangulo(3, 4, 5).ehEscaleno())  # Triângulo Escaleno
        # Classes inválidas
        self.assertFalse(model.Triangulo(5, 5, 5).ehEscaleno())  # Triângulo não é Escaleno


if __name__ == '__main__':
    unittest.main()
