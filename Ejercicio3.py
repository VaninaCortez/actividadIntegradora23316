#Frecuencia

"""Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
       cada palabra que contiene y la cantidad de veces que aparece (frecuencia)
    """

dict = {}
frase = input("Ingrese la Frase:")
lista_palabras=frase.split(" ")
for palabra in lista_palabras:
	if palabra in dict:
		dict[palabra]+=1
	else:
		dict[palabra]=1	

for campo,valor in dict.items():
	print (campo,"->",valor)

