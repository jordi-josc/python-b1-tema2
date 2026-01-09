"""
Enunciado:
Implementa la función 'convert_to_integer(string)' que reciba como parámetro una
cadena y retorne un número entero si es posible. En caso contrario, debe retornar
un mensaje indicando que la cadena no puede ser convertida a un número entero o
un mensaje de error inesperado. Para el error 'ValueError' debe retornar "The 
string cannot be converted to an integer"; si es cualquier otra excepción, debe 
mostrar "An unexpected error has occurred:" seguido del error.

Parámetros:
string (str): cadena que se desea convertir a un número entero.

Ejemplo:
    Entrada:
    convert_to_integer("123")
    convert_to_integer("foo")
    convert_to_integer(["3.14"])
    

    Salida:
    - En el primer caso el resultado es: 123
    - En el segundo caso el resultado es: The string cannot be converted to an integer
    - En el tercer caso el resultado es: An unexpected error has occurred: int() argument
    must be a string, a bytes-like object or a number, not 'list'    
    
Enunciat:
Implementa la funció 'convert_to_integer(string)' que rebi com a paràmetre una
cadena i retorneu un name enter si és possible. En cas contrari, heu de retornar
un missatge indicant que la cadena no pot ser convertida a un name enter o
un missatge d'error inesperat. Per a l'error 'ValueError' heu de retornar "The
string cannot be converted to an integer"; si és qualsevol altra excepció, ha de
mostrar "An unexpected error has occurred:" seguit de l'error.

Paràmetres:
string (str): cadena que voleu convertir a un name enter.

Exemple:
     Entrada:
     convert_to_integer("123")
     convert_to_integer("foo")
     convert_to_integer(["3.14"])
     

     Sortida:
     - En el primer cas el resultat és: 123
     - En el segon cas el resultat és: The string cannot be converted to an integer
     - En el tercer cas el resultat és: An unexpected has occurred: int() argument
     must be a string, a bytes-like object or a number, not 'list'
"""


def convert_to_integer(string):
    try:
        return int(string)
    except ValueError:
        return "The string cannot be converted to an integer"
    # TO CAPTURE THE WHOLE ERROR
    except Exception as e:
        return f"An unexpected error has occurred: {e}"


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(convert_to_integer("123"))
print(convert_to_integer(["3.14"]))
print(convert_to_integer("foo"))
