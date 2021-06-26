# Función para abrir archivos con permisos de lectura
def read():
  numbers = []
  # Ruta, parametro de permisos y codificador
  with open('./archivos/numbers.txt', 'r', encoding="utf-8") as f:
    for line in f:
      numbers.append(int(line))
  print(numbers)

# Función para abrir archivos con permisos de escritura

def write():
  names = ["facundo", "Miguel", "Pepe", "Christian", "rocío", "Genaro", "Abril"]
  #  El parametro "w" sobreescribe o crea el archivo de nuevo, poner "a" como segundo parametro no sobreescribe, solo agrega los nuevos elementos
  with open("./archivos/names.txt", "a", encoding="utf-8") as f:
    for name in names:
      f.write(name)
      f.write("\n")

def main():
  write()

if __name__ == '__main__':
  main()