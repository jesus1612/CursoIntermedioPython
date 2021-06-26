def divisors(num):
  assert num < 0, "ingresa un número positvo"

  divisors = [i for i in range(1, num + 1) if num % i == 0]
  return divisors


def main():
  # Solución propuesta por mi con assert statements
  # num = int(input("ingresa un número: "))
  # print(divisors(num))

  # assert ValueError, "Ingresa solo valores númericos"

  # Solución propuesta por el profesor
  num = input("ingresa un número: ")

  assert num.isnumeric(), "Debes ingresar un número"
  print(divisors(int(num)))
  print("Termino mi programa")

if __name__ == '__main__':
  main()