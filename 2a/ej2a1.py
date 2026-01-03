"""
Enunciado:
Una tienda tiene una promoción que aplica el descuento del 10% a los productos
cuyo valor numérico sea par. Para ello se requiere implementar funciones capaces 
de sumar una lista de valores pares y retornar dicha suma.

Implementa las funciones 'sum_even_numbers_in_list_while(list_numbers)', 
'sum_even_numbers_in_list_for(list_numbers)' y
'sum_even_numbers_in_list_do_while(list_numbers)' en donde su parámetro
sea una lista de números y utilice un bucle 'WHILE', 'FOR' y 'DO WHILE', respectivamente,
para su implementación. Todas las funciones deben retornar la suma de los números pares.

Parámetros:
    list_numbers (List): lista de precios que se desea sumar

Ejemplo:
    Entrada:
    shopping_list = [10, 449, 33, 44, 188, 640]
    sum_even_numbers_in_list_while(shopping_list)
    sum_even_numbers_in_list_for(shopping_list)
    sum_even_numbers_in_list_do_while(shopping_list)

    Salida:
    En los 3 casos el resultado es 882, que es la suma de 10, 44, 188 y 640. 


Enunciat:
Una botiga té una promoció que aplica el descompte del 10% als productes
el valor numèric del qual sigui parell. Per això es requereix implementar funcions 
per sumar una llista de valors parells i retornar aquesta suma.

Implementa les funcions 'sum_even_numbers_in_list_while(list_numbers)',
'sum_even_numbers_in_list_for(list_numbers)' i
'sum_even_numbers_in_list_do_while(list_numbers)' on el paràmetre
sigui una llista de números i utilitzi un bucle 'WHILE', 'FOR' i 'DO WHILE', respectivament,
per a la seva implementació. Totes les funcions han de retornar la suma dels números parells.

Paràmetres:
     list_numbers (List): llista de preus que es vol sumar

Exemple:
     Entrada:
     shopping_list = [10, 449, 33, 44, 188, 640]
     sum_even_numbers_in_list_while(shopping_list)
     sum_even_numbers_in_list_for(shopping_list)
     sum_even_numbers_in_list_do_while(shopping_list)

     Sortida:
     En tots tres casos el resultat és 882, que és la suma de 10, 44, 188 i 640.
"""


def sum_even_numbers_in_list_while(list_numbers):
    i = 0
    total = 0
    while i < len(list_numbers):
        if list_numbers[i] % 2 == 0:
            total += list_numbers[i]
        i += 1
    return total


def sum_even_numbers_in_list_for(list_numbers):
    total = 0
    for i in list_numbers:
        if i % 2 == 0:
            total += i
    return total


def sum_even_numbers_in_list_do_while(list_numbers):
    
    if not list_numbers:
        return 0
    
    
    i = 0
    total = 0
    
    while True:
        if list_numbers[i] % 2 == 0:
            total += list_numbers[i]
        i += 1
        if i >= len(list_numbers):
            break
    return total


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

shopping_list = [10, 449, 33, 44, 188, 640]
print(sum_even_numbers_in_list_while(shopping_list))
print(sum_even_numbers_in_list_for(shopping_list))
print(sum_even_numbers_in_list_do_while(shopping_list))
