"""
Funciones
"""

def saludar():
    print("Hola, Python")

saludar()

# Funcion con retorno

def return_saludo():
    return "Hola, Python"

print(return_saludo())

#Funcion con argumento

def arg_saludo(name):
    print(f"hola, {name}")

arg_saludo("Jack")

#Funcion con Argumentos

def args_saludo(saludo, name):
    print(f"{saludo}, {name}")

args_saludo("hi, ", "jack")
args_saludo(name="jack", saludo="hola" )

#Funcion con parametros

def default_args_saludo(name="Python"):
    print(f"Hola, {name}" )

default_args_saludo("Jack")
default_args_saludo()

## Los diferentes tipos de funciones que tenemos se pueden combinar

#Funcion con retorno de varios valores

def multiple_return_saludo():
    return "hola", "Jack"

print(multiple_return_saludo())

saludo, name = multiple_return_saludo()
print(saludo)
print(name)

#Funcion con un numero variable de argumentos

def variable_args_saludo(*names):
    for name in names:
        print(f"hola, {name}!")

variable_args_saludo("jack", "Baris", "Python", "Saravena")

#Funcion con un numero variable de argumentos con palabra clave

def variable_args_saludo(**names):
    for param, name in names.items():
        print(f"hola, {name} ({param})!")

variable_args_saludo(
    name="jack", 
    tutor="Baris", 
    lenguaje="Python", 
    ciudad="Saravena", 
    edad=29)

"""
Funciones dentro de una funcion
"""

def otra_funcion():
    def dentro_funcion():
        print("Dentro de la funcion: Hola! Jack")
    dentro_funcion()
    #Hay que llamar la funcion que esta adentro para que se ejecute

otra_funcion()


"""
Funciones del sistema
"""

print(len("jack"))
print(type("jack"))
print("Jack".upper())


"""
Varibles locales y globales
"""
var_global = "Python"

print(var_global)

def hola_python():
    var_local = "hola"
    print(f"{var_local} {var_global}!")

print(var_global)
#print(var_local)No se puede acceder a esa variable desde afuera

hola_python()

"""
Extra
 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
"""
def print_numero(texto1, texto2)->int:
    cont = 0
    for numero in range(1,101):
        
        if numero % 5 == 0 and numero % 3 == 0:
            print(texto1 + texto2)
        elif numero % 3 == 0:
            print(texto1)
        elif numero % 5 == 0:
            print(texto2)
        else:
            print(numero)
            cont+=1
    print(cont)  

print_numero("Seguimos!", "Avanzando!")