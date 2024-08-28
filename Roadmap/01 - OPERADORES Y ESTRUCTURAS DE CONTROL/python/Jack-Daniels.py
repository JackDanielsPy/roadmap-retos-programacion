# Operadores #

var1 = 1
var2 = 2

 ## Opreadores aritmeticos


Suma = var1 + var2
resta = var1 - var2
mult = var1 * var2
divi = var1 / var2
modulo = 10 % 3
exponente = 10**3
divientera = 10//3
print(Suma)

print(modulo)
print(divientera)

##Operadores de comparacíon

igualdad = 10 ==3
desigualdad = 10 != 3

mayor = 10 > 3
menor = 10 < 3
mayorque = 10 >= 3
menorque = 10<= 3 

print(mayor)
print(igualdad)
print(desigualdad)

varand = 10 > 3 and 3 < 10
varor = 10 + 3 == 13 or 10 - 1 == 9
varnot = not 10 + 3 == 14

print(varand)
print(varor)
print(varnot)

# opreadores de asignacion

variable = 10

print(variable)
variable += 2
print(variable)
variable -= 1
print(variable)
variable *= 2
print(variable)
variable /= 2
print(variable)
variable %= 2
print(variable)
variable //= 1
print(variable)
variable **= 1
print(variable)

# Operadores de identidad

nuevavariable = variable
print(f"nuevavariable es variable {nuevavariable is variable}")
print(f"nuevavariable is not variable {nuevavariable is not variable}")

# Operadores de pertenencia
print(f" 'u' in 'moure' = {'u' in 'moure'}" )
print(f" 'b' not in 'jack' = {'b' not in 'jack'} ")

# Operadores de bit

a = 10 #1010
b = 3 #0011

print(f"AND: a & b = {a & b} ") #0010
print(f"OR: a | b = {a | b} ") #1011
print(f"XOR: a ^ b = {a ^ b} ") #1001
print(f"NOT: ~10 = {~10} ")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10>>2}") #0010
print(f"Desplazamiento a la izquierda: 10 >> 2 = {10<<2}") #

"""
Estructuras de control
"""
#Condicionales

cadena = "Jack"
if cadena == "Jacky":
    print("cadena is 'Jacky'")
elif cadena == "Jack":
    print("cadena is 'Jack'")
else:
    print("cadena no es ni 'Jacky' ni 'jack'")

#iterativas

for i in range(0,11):
    print(i)

i = 0 

while i <=10:
    print(i)
    i +=1

#Manejo de excepciones

try:
    print(10 / 0)
except:
    print("Se ha producido un error")

finally:
    print("ha finalizado el manejo de excepciones")    


"""
Extra 
"""

for i in range(10,56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
