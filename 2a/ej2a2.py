"""
Enunciado:
Implementa la función 'tax_calculation_global(value)' que calcula los impuestos
a pagar de un valor numérico dado.
Implementa también la función 'tax_calculation_group_1(value)', que calcula los
impuestos para un grupo de productos diferente que tiene un porcentaje menor.

La función 'tax_calculation_global(value)' calcula el valor de impuestos usando
el valor de porcentaje ('tax_percent') de 24. De esta manera, calcularía los impuestos 
mediante la siguiente fórmula: ('tax_percent' * 'value')/100
Parámetros:
    - value: un número entero, que representa el valor al cual se le calcularán
    los impuestos.

La función tax_calculation_group_1(value) calcula los impuestos para el grupo 1 de 
productos, que tiene un valor de porcentaje ('tax_percent') de 19. 
Parámetros:
    - value: un número entero, que representa el valor al cual se le calcularán
    los impuestos.

Por ejemplo, si se llama a las funciones con un valor de 500, la función
tax_calculation_global(500) calcula el valor del impuesto global que tiene un porcentaje 
del 24%, y la función tax_calculation_group_1(500) calcula el valor del impuesto para el 
grupo 1, que son el 19% del valor.

Entrada:
tax_calculation_global(500)
tax_calculation_group_1(500)

Salida:
120.0
95.0

Enunciat:
Implementa la funció 'tax_calculation_global(value)' que calcula els impostos
a pagar un valor numèric donat.
Implementa també la funció 'tax_calculation_group_1(value)', que calcula els
impostos per a un grup de productes diferent que té un percentatge menor.

La funció 'tax_calculation_global(value)' calcula el valor d'impostos usant
el valor de percentatge ('tax_percent') de 24. D'aquesta manera calcularia els impostos
mitjançant la fórmula següent: ('tax_percent' * 'value')/100
Paràmetres:
     - value: un name enter, que representa el valor al qual es calcularan
     els impostos.

La funció tax_calculation_group_1(value) calcula els impostos per al grup 1 de
productes, que tenen un valor de percentatge ('tax_percent') de 19.
Paràmetres:
     - value: un name enter, que representa el valor al qual es calcularan
     els impostos.

Per exemple, si es crida a les funcions amb un valor de 500, la funció
tax_calculation_global(500) calcula el valor de l'impost global que té un percentatge
del 24%, i la funció tax_calculation_group_1(500) calcula el valor de l'impost per al
grup 1, que són el 19% del valor.

Entrada:
tax_calculation_global(500)
tax_calculation_group_1(500)

Sortida:
120.0
95.0
"""


def tax_calculation_group_1(value: int):
    total = (19 * value) / 100
    return total


def tax_calculation_global(value: int):
    total = (24 * value) / 100
    return total

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(f"The taxes for group global: {tax_calculation_global(500)}")
print(f"The taxes for group 1: {tax_calculation_group_1(500)}")
