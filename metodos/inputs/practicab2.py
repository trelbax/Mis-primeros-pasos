# velocidad promedio es de 2 palabras por segundo
frase= input("Dime una frase y te diré cuantas palabras tiene y cuanto demoras en decirlo: ")
palabras_separadas= frase.split(" ")
palabras= len(palabras_separadas)
indice_tiempo= 1/2
Tiempo= palabras*indice_tiempo
indice_tiempo_dalto= indice_tiempo-(indice_tiempo*30/100)
tiempo_dalto= palabras*indice_tiempo_dalto
print(f"Mi amigo tardo {Tiempo} seg en decir una frase de {palabras} palabras")
print(f"Dalto tadaría {tiempo_dalto} seg en decir lo mismo")
if Tiempo>60:
    print("Para flaco no te pedí una biblia")
