class Factorial:
  def calc(num):
    if num == 1 or num == 0:
      return 1
    elif num < 0:
      raise ValueError("Não existe fatorial de número negativo")
    else:
      fact = 1

      for i in range(1, num+1):
          fact = fact * i
      return fact