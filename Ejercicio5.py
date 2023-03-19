
#valueError

def get_int(a):
    
    while True: 
       try:
          num = int(input("Ingrese un número entero: "))  
          break 
        
    
       except ValueError:
    
           print("Error: Ingrese un valor numérico válido.")   
    
        
a=input("Ingrese un numero entero:") 
print(get_int(a))          
            
