## Codificar un programa en Python utilizando funciones que permita recibir: Nombre, edad, País, Equipo y tiempo en minutos de
## múltiples ciclistas. El software estará en la capacidad de calcular y mostrar en pantalla cual fue el ciclista más rápido
     

print("*----MENU---*")
print("1. AGREGAR CICLISTA")
print("2. VER RESULTADOS")
print("*----MENU---*")


opcion=100
ciclistas=[]
while(opcion!=10):
    opcion=int(input("Digite una opcion: "))
    ciclista={}
    if(opcion==1):
        i=1
        print(f'ingresa los datos del ciclista {i}')
        ciclista['nombre']=input(f'Digite el nombre: ')
        ciclista['edad']=int(input(f'Digite la edad: '))
        ciclista['pais']=input(f'Digite el pais ')
        ciclista['tiempo']=int(input(f'Digite el tiempo en la carrera: '))
        i+1
        ciclistas.append(ciclista)

    elif(opcion==2):
        for competidor in ciclistas:
            tiempo = competidor['tiempo']
            nombre = competidor['nombre']
        if(tiempo>competidor['tiempo']):
            tiempo = competidor['tiempo']
            nombre = competidor['nombre'] 
        print(nombre, tiempo)