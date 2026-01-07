"""
Enunciado:
Utilizando las buenas prácticas de programación de Python PEP8, implementa una
función 'check_leap_year', el parámetro debe ser nombrado correctamente y
recibe como dato un año y mediante la función se debe retornar si este año es
bisiesto o no.

Para comprobar el año bisiesto fácilmente se puede utilizar la
operación mod '%', el resultado de la operación del año a consultar mod 4
debe ser igual a '0' y además el año a consultar mod 100 debe ser distinto de
'0'.

En el caso de obtener un resultado de '0' al realizar la operación del año
mod 100 se debe comprobar si el mismo año mod 400 es igual a '0'.

Parámetros:
El parámetro debe ser nombrado correctamente recibe como dato un valor de tipo
int.

Ejemplo:
El año a comprobar será '2000', por lo que:

2000 % 4 = 0        - Cumple un parámetro para ser considerado año bisiesto.

2000 % 100 = 0      - Como se obtuvo '0' se debe comprobar adicionalmente, que
                      el resultado del año a comprobar mod 400 sea '0' para
                      considerar que sea un año bisiesto.
2000 % 400 = 0      - El año '2000' si es un año bisiesto.


Enunciat:

Utilitzant les bones pràctiques de programació de Python PEP8, implementa una
funció 'check_leap_year', el paràmetre ha de ser nomenat correctament i
rep com a dada un any i mitjançant la funció s'ha de retornar si aquest any és
de traspàs o no.

Per comprovar l'any de traspàs fàcilment es pot utilitzar la
operació mod '%', el resultat de l'operació de l'any a consultar mod 4
ha de ser igual a '0' i a més l'any a consultar mod 100 ha de ser diferent de
'0'.

En cas d'obtenir un resultat de '0' en fer l'operació de l'any
mod 100 cal comprovar si el mateix any mod 400 és igual a '0'.

Paràmetres:
El paràmetre ha de ser nomenat correctament i rep com a dada un valor de tipus
int.

Exemple:
L'any a comprovar serà '2000', de manera que:

2000 % 4 = 0 - Compleix un paràmetre per ser considerat any de traspàs.

2000 % 100 = 0 - Com es va obtenir '0' s'ha de comprovar addicionalment, que
                       el resultat de l'any a comprovar mod 400 sigui '0' per
                       considerar que sigui un any de traspàs.
2000 % 400 = 0 - L'any '2000' si és un any de traspàs.

"""


def check_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
    


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el
# script

# Si vols provar el teu codi, descomenta les línies següents i executa
# l'script

print(check_leap_year(2025))
