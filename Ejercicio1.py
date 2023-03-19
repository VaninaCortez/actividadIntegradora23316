
comprobar = True

while comprobar: 

    a = int(input("Ingrese el Primer Número:"))
    b = int(input("Ingrese el Segundo Número:"))

    MCD = False

    if a > 0 and b > 0 and a != b:
    
        comprobar = False
        
        if b < a :
        
            aux = a 
            a = b
            b = aux
       
        i = a 
       
        while not MCD and i >= 1:
           
                if a % i == 0 and  b % i == 0:
               
                    print ("El Maximo Comun Divisor es",i)
                    MCD = True
        
                else:
            
                     i -= 1
            
         
    else: 
    
        if a == b:
            print ("Los Nùmeros son iguales, intente de nuevo")
    
        else:
            print ("Los Numeros no son correctos. Intente nuevamente")



