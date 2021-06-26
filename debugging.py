def divisors(num):
  try:
    if num < 0:
      raise ValueError("ingresa un número positvo")

    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

  except ValueError as ve:
    print(ve)
    return False

def main():
  try:
    num = int(input("ingresa un número: "))
    print(divisors(num))

  except ValueError:
    print("Ingresa solo valores númericos")

if __name__ == '__main__':
  main()