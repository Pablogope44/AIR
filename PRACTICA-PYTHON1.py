'EJERCICIO1'

diccionario = { "juan " : 25, "pepe" : 40, "ana" :1}
for persona, edad in diccionario.items():
    if edad > 24:
        print(f"{persona} tiene {edad}")
        print(diccionario.get("juan "))
        diccionario["juan "] = 10
' al poner diccionario.items() obtenies clave y valor pero si solo pusieras for persona, sin edad te daria una unica tupla (juan,25)'

'EJERCICIO2'

lista = [3, 1, 4, 1, 5, 9, 2, 6, 5]

lista2 = sorted(set(lista), reverse = True)
print(lista2)

'EJERCICIO3'

    
lista3 = [x for x in range(1,21) if x % 3 == 0 or x % 5 == 0 ]  
'la x antes del for es lo que se mete en la lista, un append(x)'
     
        

'EJERCICIO4'
def resumen(texto):
    palabras2= texto.split()
    palabras= len(texto.split())
    'con split cambia el string a una lista asi que ahora cuenta palabars no numero de caracteres'
    caracteres= len(texto)
    larga=max(palabras2, key=len)
    diccionario2={"palabras" : palabras, "caracteres": caracteres,"mas larga": larga}
    return diccionario2
    
    
 
print(resumen("JuanManuel corchado pelyicer")) 


'EJERCICIO5'

def funcion(*args):
    suma= sum(args)
    media = suma/len(args)
    maximo= max(args)
    
    return suma, media, maximo

print(funcion(5,6,8))
    
    
'EJERCICIO6'

def convertir(numero):
    try:
        numero=float(numero)  
        return numero
    except ValueError:
        print("no se puede transformar a float")
        return None
    

convertir("hola")
convertir(9)

'EJERCICIO7'

class cuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular= titular
        self.saldo= saldo
    def ingresar(self, cantidad):
        self.saldo +=cantidad
        
    def __str__(self):
        return f"Titular: {self.titular}, Saldo: {self.saldo}"
    def retirar(self, cantidad):
        if cantidad > self.saldo:
         print("saldo insuficiente")
        else:
         self.saldo -= cantidad
    
    
c = cuentaBancaria("Juan", 1000)
c.ingresar(500) 
c.retirar(20000)
print(c)

class Cuenta:
    @staticmethod
    def transferir(cuenta_origen, cuenta_destino, cantidad):
        if cuenta_origen.saldo >= cantidad:
            cuenta_origen.saldo -= cantidad
            cuenta_destino.saldo += cantidad
        else:
            print("Saldo insuficiente para la transferencia.")


class Animal:
    def hablar(self):
        return "..."


class Perro(Animal):
    def hablar(self):
        base = super().hablar()  # llama al hablar() de Animal
        return f"{base} y también Guau"
    
'self se usa para acceder a los metodos del ovjeto, y super() para acceder a los metodos de la clase padre'


class Animal():
    def hablar(self):
        return "....GOOOFYAU"
    
class Perro(Animal):
    def hablar(self):   
        
         return "Pitagoras itagoras tagoras agoras goras oras ras as a s"
     
     
class Gato(Animal):
    def hablar(self):
        return "Miau"

gato = Gato()
print(gato.hablar())

perro= Perro()
print(perro.hablar())


