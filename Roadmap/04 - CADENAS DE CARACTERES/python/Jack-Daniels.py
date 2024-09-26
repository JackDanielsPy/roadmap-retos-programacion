"""
Cadenas de caracteres
"""

#Oprecaiones
c1 = "Hola"
c2 = "Mundo"

print(c1 + ", " + c2 + ".")

print(c1 * 3)

#indexacion

print(c1[0] + c1[1] + c2[2] + c2[3] + c1[3])

print(len(c1+c2))

c3 = "Programacion"

print(c3[2:8])
print(c3[2:])

print("H" in c3)
print("H" in c1)

print(c3.replace("o", "ó"))
print(c3.split("m"))

print(c3.upper())
print("jack martinez".title())
print("jack martinez guerrero".capitalize())

#Eliminacion de espacios

print(" Hola a todos los programadores ".strip())

#Busqueda al principio y al final
print(c1.startswith("Ho"))
print(c1.startswith("Ha"))
print(c1.endswith("la"))
print(c2.endswith("da"))

#Busqueda por posicion
c4= "Hola a todos los programadores"

print(c4.find("Hola"))
print(c4.find("l"))
print(c4.lower().find("p"))

#Busqueda por ocurrencia
print(c4.lower().count("a"))

#Formateo

print("Saludo: {}, Gente: {}".format(c1, c3))

print(list(c2))

l1 = [c2, "", c3, "!"]
print(l1)
print(" ".join(l1))

c5 = "123654"
c5 = int(c5)
print(c5)

#Comprobaciones varias
"""
print(c5.isalnum())
print(c5.isalpha())
print(c5.isnumeric())
"""

"""
DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""



print("** Menu **")
print("1-Anagramas ")
print("2-Palindromas ")
print("3-Isogramas")
print("4-Salir")

seleccion = int(input("Selecionar del 1 al 4: "))


if seleccion == 1:
    palabra1 = input("introduce la primera palabra: ")
    palabra2 =input("introduce la segunda plabra: ")
    palabra3 = palabra1.lower()
    palabra4 = palabra2.lower()


    def anagrama(palabra3, palabra4):
    

        arreglo1 = list(palabra3)
        arreglo2 = list(palabra4)
        arreglo1.sort()
        arreglo2.sort()
        palabra1_ordenada = "".join(arreglo1)
        palabra2_ordenada = "".join(arreglo2)

        if(palabra1_ordenada == palabra2_ordenada):
            print(palabra1_ordenada == palabra2_ordenada)
            #return True
        elif(palabra1_ordenada !=palabra2_ordenada):

            #return False
            print(palabra1_ordenada == palabra2_ordenada)

    anagrama(palabra3, palabra4)

elif seleccion == 2:
    palabrapalin = input("Ingresa la palabra: ")
    a,b = "aeiou", "áéíóú" 
    trans = str.maketrans(b,a)
    def palindromo(palabrapalin):
        f = palabrapalin.lower()
        frasemis = f.replace(" ", "")
        frasemid = frasemis.replace(",","")
        frased = "".join(frasemid)
        print(frased.translate(trans))
        palabrapalin = frased[::-1]
        palabra3 = palabrapalin.lower()
        print(palabra3.translate(trans))      
        if frased.translate(trans) ==  palabra3.translate(trans):
            print("Si es un palindromo")            
        else:
            print("No es un palindromo")
    palindromo(palabrapalin)

elif seleccion == 3:
    palabraiso = input("Ingresa la palabra: ")
    lista = list(palabraiso)
    lista2 = list()
    for i in lista:
        cantletra = lista.count(i)
        lista2.append(cantletra) 
    
    promedio = sum(lista2) / len(lista2)
    isograma = True
    for i in lista2:
        if i != promedio:
            isograma = False
            print(f"La palabra es isograma?: ", isograma)
            break
        else:
            isograma = True
            print(f"La palabra es isograma?: ", isograma)
            break