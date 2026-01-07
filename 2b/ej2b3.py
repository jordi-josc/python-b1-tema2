"""
Enunciado:
Implementa una función 'triangle_area_calculate', que recibe dos parámetros,
que corresponden a la altura y la base de un triángulo que deben
ser números positivos. Dichos parámetros deben ser nombrados correctamente,
considerando las buenas prácticas de programación PEP8.
La función debe retornar el cálculo del área de un triángulo mediante los
datos introducidos, adicionalmente, el código debe tener comentarios de manera
que se vaya explicando el procedimiento.

Parámetros:
Son dos parámetros, que corresponden a la altura y la base de
un triángulo y deben ser números positivos. Se deben crear correctamente
utilizando las buenas prácticas de programación PEP8.


Ejemplo:
    Entrada:
    triangle_area_calculate(33, 45)

    Salida:
    742.5


Enunciat:
Implementa una funció 'triangle_area_calculate', que rebi dos paràmetres,
que corresponen a l'alçada i la base d'un triangle i que han de
ser números positius. Aquests paràmetres han de ser nomenats correctament,
considerant les bones pràctiques de programació PEP8.
La funció ha de retornar el càlcul de l'àrea d'un triangle mitjançant les
dades introduïdes, addicionalment, el codi ha de tenir comentaris de manera
que es vagi explicant el procediment.

Paràmetres:
Són dos paràmetres, que corresponen a l'alçada i la base de
un triangle i que han de ser números positius. S'han de crear correctament
utilitzant les bones pràctiques de programació PEP8.


Exemple:
     Entrada:
     triangle_area_calculate(33, 45)

     Sortida:
     742.5

"""


def triangle_area_calculate(base, height):
    # Inicialitzem la variable àrea
    area = 0
    # Comprovem que no siguin negatius els numeros
    if base <= 0 or height <= 0:
        raise ValueError("Els numeros son negatius")
    else:
        # Calculem l'àrea del triangle
        area = (base * height) / 2
    # Retornem el valor d'àrea calculat correctament
    return area        


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta
# el script

# Si vols provar el teu codi, descomenta les línies següents i executa
# l'scrip

print(triangle_area_calculate(33, 45))
