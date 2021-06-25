def main():
  # squares = []

  # for i in range(1,101):
  #   if(i % 3 != 0 ):
  #     squares.append(i**2)
  # List comprehensions
  #        Element for element in elements if condition
  squares = [i**2 for i in range(1, 101) if(i%3 != 0)]
  print(squares)

  # Reto - Multiplos de 4, 6 y 9 en números menores a 6 digitos
  multiplos = [i for i in range (1, 100000) if(i%4 == 0 and i%6 == 0 and i%9 == 0 )]
  print(multiplos)

if __name__ == '__main__':
  main()