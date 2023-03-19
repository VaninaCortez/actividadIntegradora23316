# Minimo Comun Multiplo

a = int(input("Ingrese el Primer Número:"))
b = int(input("Ingrese el Segundo Número:"))


i = 2 

while True:
    
    if i% a == 0 and i% b == 0:
        mcm = i
        break 
    i+=1 

print("El minimo comun multiplo es :", i)    


