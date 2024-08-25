animales = ["pez","gato","perro","loro","cocodrilo"]
numeros = [52,16,14,72]
 #recorriendo la lista animales
for animal in animales:
    print(f"El animal es un: {animal}")

#recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero*10
    print(resultado)
#para mas elementos iterables
for numero, animal in zip(animales,numeros):
    print(f"RECORRIENDO LISTA1:{numero}")
    print(f"RECORRIENDO LISTA2:{animal}")
#forma de recorrer una lista con su índice
for num in enumerate(numeros):
    print(num)