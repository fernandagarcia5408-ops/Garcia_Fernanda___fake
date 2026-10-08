# Archivo: practica_2_2_garcia_fernanda.py

# Ejercicio 1 — ¿Es par o impar?
# Declara una variable numero y calcula en una variable booleana es_par si el número es par
numero = 4
es_par = (numero % 2 == 0)
print("--- Ejercicio 1: ¿Es par o impar? ---")
print(f"El número {numero} es par: {es_par}")

# Ejercicio 2 — Concatenar vs. sumar
# Declara dos variables de texto con dígitos y muestra la suma de texto vs. numérica.
texto_1 = "5"
texto_2 = "3"

suma_texto = texto_1 + texto_2
suma_numerica = int(texto_1) + int(texto_2)

print("\n--- Ejercicio 2: Concatenar vs. sumar ---")
print(f"Suma como texto (concatenación): {suma_texto}")
print(f"Suma como número (tras int()): {suma_numerica}")
# Diferencia: El operador '+' con cadenas une los textos ("5" + "3" = "53"), 
# mientras que al convertirlos a int() se realiza una operación aritmética (5 + 3 = 8).

# Ejercicio 3 — Mini reporte de un perfil
# Variables para nombre, edad, estatura y es_estudiante.
nombre = "Fernanda"
edad = 20
estatura = 1.68
es_estudiante = True

print("\n--- Ejercicio 3: Mini reporte de un perfil ---")
print(f"Valor: {nombre} | Tipo: {type(nombre)}")
print(f"Valor: {edad} | Tipo: {type(edad)}")
print(f"Valor: {estatura} | Tipo: {type(estatura)}")
print(f"Valor: {es_estudiante} | Tipo: {type(es_estudiante)}")

# Extra: Combinar datos en un mensaje de texto usando str()
mensaje_extra = "Hola, me llamo " + nombre + " y tengo " + str(edad) + " años."
print(f"Mensaje extra: {mensaje_extra}")

# Ejercicio 4 — Operadores aritméticos básicos
num_a = 10
num_b = 4

print("\n--- Ejercicio 4: Operadores aritméticos básicos ---")
print(f"Suma (+): {num_a + num_b}")
print(f"Resta (-): {num_a - num_b}")
print(f"Multiplicación (*): {num_a * num_b}")
print(f"División (/): {num_a / num_b}")

# Ejercicio 5 — División entera y módulo

print("\n--- Ejercicio 5: División entera y módulo ---")
print(f"División entera (17 // 5): {17 // 5}")
print(f"Módulo (17 % 5): {17 % 5}")
# Explicación: La división normal (/) devuelve un resultado con decimales (flotante), 
# mientras que la división entera (//) descarta la parte fraccionaria quedándose solo con el cociente entero.
# El operador módulo (%) devuelve el residuo sobrante de esa división entera.

# Ejercicio 6 — Operadores relacionales
val1 = 8
val2 = 8

mayor = (val1 > val2)
menor = (val1 < val2)
igual = (val1 == val2)
diferente = (val1 != val2)

print("\n--- Ejercicio 6: Operadores relacionales ---")
print(f"Comparando {val1} y {val2}:")
print(f"Mayor (>): {mayor}")
print(f"Menor (<): {menor}")
print(f"Igual (==): {igual}")
print(f"Diferente (!=): {diferente}")

# Ejercicio 7 — Operadores lógicos
condicion_1 = (10 > 5)   # True
condicion_2 = (3 == 7)   # False

res_and = condicion_1 and condicion_2
res_or = condicion_1 or condicion_2
res_not = not condicion_1

print("\n--- Ejercicio 7: Operadores lógicos ---")
print(f"Condición 1 (10 > 5): {condicion_1}")
print(f"Condición 2 (3 == 7): {condicion_2}")
print(f"AND: {res_and}")
print(f"OR: {res_or}")
print(f"NOT Condición 1: {res_not}")

# Ejercicio 8 — Promedio y aprobación
cal1 = 8.5
cal2 = 7.0
cal3 = 9.0

promedio = (cal1 + cal2 + cal3) / 3
aprobado = (promedio >= 6)

print("\n--- Ejercicio 8: Promedio y aprobación ---")
print(f"Calificaciones: {cal1}, {cal2}, {cal3}")
print(f"Promedio: {promedio:.2f}")
print(f"¿Aprobado?: {aprobado}")

# Ejercicio 9 — Validación de elegibilidad
edad_persona = 20
nacionalidad = "mexicana"

es_elegible = (edad_persona > 17) and (nacionalidad == "mexicana")
es_elegible_or = (edad_persona > 17) or (nacionalidad == "mexicana")

print("\n--- Ejercicio 9: Validación de elegibilidad ---")
print(f"Edad: {edad_persona}, Nacionalidad: {nacionalidad}")
print(f"Es elegible (con and): {es_elegible}")
print(f"Es elegible (con or): {es_elegible_or}")


# Nota extra: 'and' requiere que ambas condiciones sean verdaderas para dar True, 
# mientras que 'or' arroja True si al menos una de las dos condiciones se cumple.