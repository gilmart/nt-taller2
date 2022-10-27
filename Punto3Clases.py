#from http import client


class Cliente:
    
    def __init__(self, nombreAsignado, apellidoAsignado, cedulaAsignado, ciudadAsignado, numeroCuentaAsignado, saldoAsignado):
        self.nombre=nombreAsignado
        self.apellido=apellidoAsignado
        self.cedula=cedulaAsignado
        self.ciudad=ciudadAsignado
        self.numeroCuenta=numeroCuentaAsignado
        self.saldo=saldoAsignado
      #  self.guardarCliente()
    
    def mostrarDatosCliente(self):
        print('El nombre del cliente es: ' + self.nombre)
        print('La edad del cliente es: ' + self.apellido)
        print('El sexo del cliente es: ' + self.cedula)
        print('La ciudad del cliente es: ' + self.ciudad)
        print('La numero de cuenta del cliente es: ' + self.numeroCuenta)
        print('La saldo del cliente es: ' +  str(self.saldo))
    
    def consultarSaldoCliente(self):
        print(f'El saldo del cliente {self.nombre} es: {self.saldo}')

    def ingresarDinero(self,saldoExtra):
        if(saldoExtra>0):
            self.saldo=self.saldo +saldoExtra
            return self.saldo

    def retirarDinero(self,saldoRetirar):
        if(saldoRetirar>0):
            if(saldoRetirar<= self.saldo):
                self.saldo=self.saldo-saldoRetirar
                return self.saldo
            