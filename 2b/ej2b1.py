"""
Enunciado:
Utilizando las buenas prácticas de programación de Python PEP8, implementa una
función 'sum_list_numbers', el parámetro debe ser nombrado correctamente, el
mismo debe recibir una lista.

Las buenas prácticas de programación de Python PEP8 las puedes encontrar en 
el siguiente enlace:
https://peps.python.org/pep-0008/

La función debe retornar la suma de los números encontrados en la lista.

Parámetro:
El parámetro debe recibir la siguiente lista de números y debe ser nombrado
bajo las buenas prácticas de programación. Recibe la siguiente lista:
[50, 10.5, 21, 37.2, 99.9, 40.75, 80]

Ejemplo:
    Entrada:
    sum_list_numbers([50, 10.5, 21, 37.2, 99.9, 40.75, 80])

    Salida:
    339.35


Enunciat:
Utilitzant les bones pràctiques de programació de Python PEP8, implementa una
funció 'sum_list_numbers', el paràmetre ha de ser nomenat correctament i 
ha de rebre una llista.

Les bones pràctiques de programació de Python PEP8 les pots trobar a
el següent enllaç:
https://peps.python.org/pep-0008/

La funció ha de retornar la suma dels números trobats a la llista.

Paràmetre:
El paràmetre ha de rebre la següent llista de números i ha de ser nomenat
sota les bones pràctiques de programació. Rep la llista següent:
[50, 10.5, 21, 37.2, 99.9, 40.75, 80]

Exemple:
     Entrada:
     sum_list_numbers([50, 10.5, 21, 37.2, 99.9, 40.75, 80])

     Sortida:
     339.35

"""


def sum_list_numbers(list_numbers):
    total = 0
    for i in list_numbers:
        total += i
    return total


# Si quieres probar tu código, descomenta las siguientes líneas y
# ejecuta el script

# Si vols provar el teu codi, descomenta les línies següents i executa
# l'script

print(sum_list_numbers([50, 10.5, 21, 37.2, 99.9, 40.75, 80]))
