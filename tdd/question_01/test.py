#test.py

import unittest
import model

class TestTemperatureConversion(unittest.TestCase):
  def test_celsius_to_fahrenheit(self):
    self.assertTrue(model.Temperature.convert_celsius_to_fahrenheit(0) == 32)
    self.assertTrue(model.Temperature.convert_celsius_to_fahrenheit(10) == 50)

  def test_farenheit_to_celsius(self):
    self.assertTrue(model.Temperature.convert_fahrenheit_to_celsius(32) == 0)
    self.assertTrue(model.Temperature.convert_fahrenheit_to_celsius(50) == 10)

if __name__ == '__main__':
    unittest.main()