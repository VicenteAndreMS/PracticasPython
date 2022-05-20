class Persona():
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance 
    def __str__(self):
        return f"Nombre y Apellido de cliente: {self.nombre} {self.apellido}\n Número de cuenta: {self.numero_cuenta}\n Balance: {self.balance}"
    def depositar(self,cantidad_depositar):
        self.cantidad = cantidad_depositar
        self.balance = self.balance + cantidad_depositar
    def retirar(self,cantidad_retirar):
        self.cantidad_retirar = cantidad_retirar
        self.balance = self.balance - cantidad_retirar

def crear_usuario():
    print("-------BIENVENIDO A BANCO PILAR-------")
    usuario_nombre = input("Ingrese su nombre: ")
    usuario_apellido = input("Ingrese su apellido: ")
    usuario_numero_cuenta = input("Ingrese su número de cuenta: ")
    usuario_final = Cliente(usuario_nombre,usuario_apellido,usuario_numero_cuenta,15000)
    control_acciones(usuario_final)

def control_acciones(usuario_final):
    control_numero = 0
    while control_numero != 3:
        print("***Su balance es de: {} ***".format(usuario_final.balance))
        print("¿Qué acción desea realizar?")
        print("->Presione 1 para depositar")
        print("->Presione 2 para retirar")
        print("->Presione 3 para salir")
        eleccion_usuario = input()
        eleccion_usuario_int = int(eleccion_usuario)
        if eleccion_usuario_int == 1:
            eleccion_uno(usuario_final)
        elif eleccion_usuario_int == 2:
            eleccion_dos(usuario_final)
        elif eleccion_usuario_int == 3:
            print("Finalizando Programa...")
            break
        elif eleccion_usuario_int != 1 or eleccion_usuario_int != 2 or eleccion_usuario_int != 3:
            print("Ingrese alguno de los índices mostrados (1 ,2 o 3)")
        
def eleccion_uno(usuario_final):
    depositar_cantidad = input("Ingrese la cantidad a depositar a su cuenta: ")
    depositar_cantidad_int = int(depositar_cantidad)
    usuario_final.depositar(depositar_cantidad_int)
    print("*******Deposito Exitoso******")

def eleccion_dos(usuario_final):
    retirar_cantidad = input("Ingrese la cantidad a retirar de su cuenta: ")
    retirar_cantidad_int = int(retirar_cantidad)
    if usuario_final.balance < retirar_cantidad_int:
        print("No cuenta con el balanceo suficiente, ingrese una cantidad menor")
    elif usuario_final.balance >= retirar_cantidad_int:
        usuario_final.retirar(retirar_cantidad_int)
        print("*******Retiro Exitoso******")

crear_usuario()