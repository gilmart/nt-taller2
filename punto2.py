# Codificar un programa en Python utilizando funciones lamba que permita: recibir 2 números y devolver
# 1 → si el primer número es mayor que el segundo
# -1→ si el primer número es menor que el segundo
# Después una segunda función debe recibir el 1 o el -1 retornado por
# la función 1 y mostrar un mensaje
# Si recibe 1 → Debe indicar que el primer número es mayor
# Si recibe -1 → Debe indicar que el segundo número es mayor

funcion1= lambda n1,n2: 1 if n1 > n2 else -1 
funcion2= lambda funcion1:print(f'el 1er numero es mayor {n1}') if funcion1 == 1 else print(f"el 2do numero es mayor {n2}")


i=1
print('**** --- MENU --- ****')    
print(' --- Ingrese 2 numeros ---')     

n1=int(input(f' -Ingrese numero {i}: '))
n2=int(input(f' -Ingrese numero {i+1}: '))

print(funcion1(n1,n2)) 
print(funcion2(funcion1(n1,n2)))


