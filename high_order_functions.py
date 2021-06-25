from functools import reduce

def main():
  # FILTER
  # Filter lleva en primer argumento la iteración o condición ( En este caso una función lambda)
  # Y como segundo parametro lleva el rango bajo el cual se va a iterar
  # Nos regresa una nueva lista con los elementos que cumplen la condicionante
  # **Debe ir dentro de list()**
  # pairs_nums = list(filter(lambda i: i % 2 == 0, range(1,1000)))
  # print(pairs_nums)

  #MAP
  # Ejemplo de lists comprehensions
  # squares = [i**2 for i in range(1,6)]
  # print(squares)

  # Ahora lo aplicamos con map
  # Mismos parametros pero incluyendo todos los elementos, transformados bajo una función lambda

  # squares = list(map(lambda x: x**2, range(1,6)))
  # print(squares)

  # Filter
  # El primer parametro es una función lambda que transformará nuestro input
  # Recibe una lista como segundo parametro y une todas según se necesite
  all_multiplied = reduce(lambda a,b: a * b, [2, 2, 2, 2, 2])
  print(all_multiplied)

if __name__ == '__main__':
  main()