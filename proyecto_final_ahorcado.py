from random import randrange
import os

# Posibles palabras para el ahorcado
words = ["computadora", "libro", "Cielo", "espejo", "automovil"]

# Parte gráfica de como se vería la bienvenida al juego
def intructions():
  print("""
  BIENVENIDO AL JUEGO DEL AHOCARDO

  LAS INSTRUCCIONES SON LAS SIGUIENTES:
  * Tienes 5 oportunidades para adivinar la palabra
  * Te mostraremos las letras que adivines
  * si no adivinas podrás volver a jugar con una palabra aleatoría
  """)

def winGame(word):
  print("LA PALABRA ES "+ word)
  print("HAZ GANADO EL JUEGO!!")
# Función principal
def main():
  lifes = 5
  intructions()
  # Obtenemos la palabra
  word = words[randrange(len(words))]
  word = word.upper()

  secretWord = ["_" for i in range(0, len(word))]

  while lifes > 0:
    print("Tienes {} vidas\n".format(lifes))
    print("La palabra a adivinar es la siguiente: ")
    print(secretWord)

    letter = input("\nIngresa una letra y presiona enter: ")
    letter = letter.upper()

    # Variables temporales dentro del ciclo
    removeLife = True

    for i in range(0, len(word)):
      if word[i] == letter:
        secretWord[i] = letter;
        removeLife = False;

    if removeLife:
        lifes-=1

    if secretWord.count("_") == 0:
        winGame(word)
        break
    os.system("clear")
# Flayer
if __name__ == '__main__':
  main()