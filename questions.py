import random

categorias={"programación":["python","variable","funcion","lista","bucle"],
            "países":["argentina","peru","colombia","chile","mexico"],
            "frutas":["manzana","banana","naranja","pera","frutilla"]}

guessed = []
attempts = 6
points=0

print("¡Bienvenido al Ahorcado!")
print()
print("Elige una categoría: ")
for cat in categorias:
   print(f"-{cat}")

cat_elegida=input("Escribe la categoría elegida: ").lower()

if cat_elegida in categorias:
        lista_elegida=categorias[cat_elegida]
else:
        print("Categoría no válida, se usará 'programación' por defecto")
        lista_elegida=categorias["programación"]
palabras_distintas=random.sample(lista_elegida,5)
word=palabras_distintas[0]

while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
 progress = ""
 for letter in word:
   if letter in guessed:
      progress += letter + " "
   else:
     progress += "_ "
 print(progress)
 # Verificar si el jugador ya adivinó la palabra completa
 if "_" not in progress:
     print("¡Ganaste!")
     points+=6
     break
 print(f"Intentos restantes: {attempts}")
 print(f"Letras usadas: {', '.join(guessed)}")
 letter = input("Ingresá una letra: ")
 if len(letter) != 1 or not (letter >="a" and letter <= "z"):
        print("Entrada no válida")
        continue
 if letter in guessed:
     print("Ya usaste esa letra.")
 elif letter in word:
     guessed.append(letter)
     print("¡Bien! Esa letra está en la palabra.")
 else:
     guessed.append(letter)
     attempts -= 1
     points-=1
     print("Esa letra no está en la palabra.")
 print()
else:
 print(f"¡Perdiste! La palabra era: {word}")
 points=0
print(f"Puntaje final: {points}")