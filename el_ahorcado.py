import random
from google.colab import drive
drive.mount('/content/gdrive')

class PalabraMagica:

  def __init__(self):
    with open("/content/gdrive/My Drive/palabras.csv", "r") as file:
      self.listado = []
      for linea in file:
        linea = linea.strip()
        self.listado.append(linea)
    self.palabra = random.choice(self.listado).lower()
    self.barras = len(self.palabra)

class Ahorcado(PalabraMagica):

   def __init__(self):
      super().__init__()
      self.letras_adivinadas = []
      self.letras_fallidas = []
      self.palabra_mostrada = ""
      self.sentenciado = 0
      self.victima = ["_____\n      |\n      |\n      |\n   ___|", " _____\n  O   |\n      |\n      |\n   ___|", " _____\n  O   |\n  I   |\n      |\n   ___|", " _____\n  O   |\n /I   |\n      |\n   ___|", " _____\n  O   |\n /I\  |\n      |\n   ___|", " _____\n  O   |\n /I\  |\n /    |\n   ___|", " _____\n  O   |\n /I\  |\n / \  |\n   ___|"]

   def juego(self):
    self.status = "muerto"
    while self.sentenciado < 6:
      if "_" not in self.palabra_mostrada:
        print(f"{self.palabra_mostrada}")
        print("\nVives para ver otro dia, has ganado!")
        self.status = "vivo"
        break
      else:
        self.pregunta = input("Diga una letra ").lower()
        if len(self.pregunta) > 1:
          print("Solo puede adivinar una letra ")
          self.juego()
        elif self.pregunta in self.letras_adivinadas:
          print("Esa letra ya fue adivinada ")
          self.juego()
        else:
          if self.secreto(self.pregunta):
            self.bien(self.pregunta)
          else:
            self.mal(self.pregunta)
    if self.status == "muerto":
        print("\nHas muerto!")
        print(f"{self.victima[self.sentenciado]}")
    print("\n")
    print("\nLa palabra era:")
    print(f"{self.palabra}")


   def inicio(self):
     if self.barras > 5:
       contador = 0
       while contador < 2:
         azar = random.choice(self.palabra)
         if azar not in self.letras_adivinadas:
           self.letras_adivinadas.append(azar)
           contador += 1
         else:
           continue
     else:
        self.letras_adivinadas.append(random.choice(self.palabra))
     for i in self.palabra:
        if i in self.letras_adivinadas:
          self.palabra_mostrada += i + " "
        else:
          self.palabra_mostrada += "_ "
     print(f"{self.victima[self.sentenciado]}")
     print("\n")
     print(f"{self.palabra_mostrada}\n")
     self.juego()

   def secreto(self, adivinanza):
    if len(adivinanza) == 0:
      return True
    else:
        if adivinanza[0] in self.palabra:
            return Ahorcado.secreto(self.palabra.replace(adivinanza[0], "", 1), adivinanza[1:])
        else:
            return False

   def bien(self, adivinanza):
        self.letras_adivinadas.append(adivinanza)
        self.palabra_mostrada = ""
        for i in self.palabra:
          if i in self.letras_adivinadas:
            self.palabra_mostrada += i + " "
          else:
            self.palabra_mostrada += "_ "
        print("\nAcertaste!")
        print(f"{self.victima[self.sentenciado]}")
        print("\n")
        print(f"{self.palabra_mostrada}\n")
        print("Has probado con las siguientes letras: ")
        print(' '.join(self.letras_fallidas))
        print(f"Puedes fallar {6 - self.sentenciado} veces")

   def mal(self, adivinanza):
       self.sentenciado += 1
       self.letras_fallidas.append(adivinanza)
       print("\nFallaste!")
       print(f"{self.victima[self.sentenciado]}")
       print("\n")
       print(f"{self.palabra_mostrada}\n")
       print("Has probado con las siguientes letras: ")
       print(' '.join(self.letras_fallidas))
       print(f"Puedes fallar {6 - self.sentenciado} veces")

iniciar = Ahorcado()
iniciar.inicio()
