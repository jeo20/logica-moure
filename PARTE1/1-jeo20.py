"""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""
# OPERADORES
# Operadores aritméticos
print("Suma: ", 2 + 2)
print("Resta: ", 2 - 2)
print("Multiplicación: ", 2 * 2)
print("División: ", 2 / 2)
print("División entera: ", 2 // 2)
print("Módulo: ", 2 % 2)
print("Potencia: ", 2 ** 2)


# Operadores lógicos
print("Operadores lógicos")
print("AND: ", True and True)
print("OR: ", True or False)
print("NOT: ", not True)


# Operadores de comparación
print("Operadores de comparación")
print("Igualdad: ", 2 == 2)
print("Diferencia: ", 2 != 2)
print("Menor que: ", 2 < 2)
print("Mayor que: ", 2 > 2)
print("Menor o igual que: ", 2 <= 2)
print("Mayor o igual que: ", 2 >= 2)


# Operadores de asignación
print("Operadores de asignación")
a = 2
print(f"Asignación: ", a)
a += 2
print(f"Asignación aditiva: ", a)
a *= 2
print(f"Asignación multiplicativa: ", a)
a /= 2
print(f"Asignación divida: ", a)
a %= 2
print(f"Asignación módulo: ", a)
a **= 2
print(f"Asignación potencia: ", a)


# Operadores de identidad
a = 3
numero = a
print("Operadores de identidad")
print("Es igual: ", numero is a)
print("Es distinto: ", numero is not a)

# Operadores de pertenencia
print("Operadores de pertenencia")
print("Pertenencia: ", 2 in [1, 2, 3])
print("No pertenencia: ", 2 not in [1, 2, 3])


#Operadores de bit
print("Operadores de bit")
print("AND: ", 2 & 3)
print("OR: ", 2 | 3)
print("XOR: ", 2 ^ 3)
print("NOT: ", ~2)
print("Left Shift: ", 2 << 1)
print("Right Shift: ", 2 >> 1)


# ESTRUCTURAS DE CONTROL
name = "Jorge"
print("Estructura de control condicional")
if name == "Jorge":
    print("Hola Jorge")
elif name == "JeO":
    print("Hola JeO")
else:
    print("No eres Jorge")
    
# For
print("Ciclo For")
for i in range(10):
    print(i)
    
# While
print("Ciclo While")
i = 0
while i < 10:
    print(i)
    i += 1

# Excepciones
print("Excepciones")
try:
    print(10/0)
except:
    print("No se puede dividir por cero")
finally:
    print("Se ha ejecutado el bloque try")

    
"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""
for numero in range(10,55):
    if numero % 2 == 0 and numero != 16 and numero % 3 != 0:
        print(numero)
        