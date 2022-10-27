#El banco de hierro de la isla de Braavos necesita de sus servicios para programar un software que permita:
#Almacenar información de un cliente (nombre, apellido, cedula, ciudad)
#Almacenar información de la cuenta (numeroCuenta, saldo)
#Se debe permitir consultar saldo en cualquier momento
#Se debe permitir ingresar o retirar dinero cuando se desee 

from unittest.mock import seal
from Punto3Clases import Cliente

print("****---MENU---****")
print("1. Almacenar información del cliente")
print("2. Mostrar informacion")
print("3. Consultar saldo")
print("4. Ingresar dinero")
print("5. Retirar dinero")

opcion=100
#objetoCliente=Cliente()

while(opcion!=0):
    opcion=int(input('Digite una opcion: '))
  #  objetoCliente={}
    if(opcion==1):
        objetoCliente=Cliente(
        nombreAsignado=input(f'Digite nombre: '),
        apellidoAsignado=input(f'Digite apellido: '),
        cedulaAsignado=input(f'Digite cedula: '),
        ciudadAsignado=input(f'digite ciudad: '),
        numeroCuentaAsignado=input(f'digite numero de cuenta: '),
        saldoAsignado=int(input(f'digite saldo: '))
        )
        
        print("Registrado")
        #print(objetoCliente.nombre, objetoCliente.apellido, objetoCliente.cedula, objetoCliente.ciudad)
        
    elif(opcion==2):
        objetoCliente.mostrarDatosCliente()
    
    elif(opcion==3):
        objetoCliente.consultarSaldoCliente()
    
    elif(opcion==4):
        saldoExtra=int(input(f'Digite la cantidad que desea ingresar: '))
        print("Contando...")
        print(objetoCliente.ingresarDinero(saldoExtra))
    
    elif(opcion==5):
        saldoRetirar=int(input("Ingrese la cantidad que desee retirar: "))
        print(objetoCliente.retirarDinero(saldoRetirar))


