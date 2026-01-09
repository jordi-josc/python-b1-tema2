"""
Enunciado:
Imagina que trabajas en una aplicación de gestión de inventarios. Para obtener
información sobre un producto, es necesario buscarlo en una lista. Sin embargo, 
podría generarse un error si se ingresa un índice fuera del rango de la lista.
Así que debes manejar las excepciones.

Implementa 'get_element_from_list(items_list, index)' que reciba una lista
y un índice, y retorne el elemento de la lista correspondiente al índice. Si
el índice está fuera del rango de la lista, la función debe retornar "The
specified index is out of the list's range". En caso de un error inesperado, ha
de retornar "An unexpected error has occurred: {error}".

Parámetros:
items_list (List): Lista de la que se desea obtener el elemento.
index (int): Índice del elemento que se desea obtener.

Ejemplo:
    Entrada:
    get_element_from_list(["Pencil", "Pen", "Eraser", "Notebook", "Ruler"], 3)
    get_element_from_list(["Pencil", "Pen", "Eraser", "Notebook", "Ruler"], 5)
    
    Salida:
    - En el primer caso el resultado es: "Notebook"
    - En el segundo caso el resultado es: "The specified index is out of the items_list's range"
    - En caso de un error inesperado, ha de retornar: "An unexpected error has occurred: {error}"
    

Enunciat:
Imagina't que treballes en una aplicació de gestió d'inventaris. Per obtenir
informació sobre un producte, cal cercar-lo en una llista. No obstant això,
es podria generar un error si introduïu un índex fora del rang de la llista.
Així que has de gestionar les excepcions.

Implementa 'get_element_from_list(items_list, index)' que rebi una llista
i un índex, i retorneu l'element de la llista corresponent a l'índex. Si
l'índex està fora del rang de la llista, la funció ha de retornar "The
specified index is out of the list's range". En cas d'un error inesperat, ha
de retornar "An unexpected error has passat: {error}".

Paràmetres:
items_list (List): Llista de la qual voleu obtenir l'element.
index (int): Índex de l'element que voleu obtenir.

Exemple:
     Ingrés:
     get_element_from_list(["Pencil", "Pen", "Eraser", "Notebook", "Ruler"], 3)
     get_element_from_list(["Pencil", "Pen", "Eraser", "Notebook", "Ruler"], 5)
    
     Resultat:
     - En el primer cas el resultat és: "Notebook"
     - En el segon cas, el resultat és: "L'específic index és de la llista d'articles_list"
     - En cas d'un error inesperat, ha de retornar: "An unexpected error has passat: {error}"
"""


def get_element_from_list(items_list, index) -> str:
    try:
        return items_list[index]
    except IndexError:
        return "The specified index is out of the items_list's range"
    except Exception as e:
        return f"An unexpected error has occurred: {e}"


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

print(get_element_from_list(["Pencil", "Pen", "Eraser", "Notebook", "Ruler"], 3))
print(get_element_from_list(["Pencil", "Pen", "Eraser", "Notebook", "Ruler"], 5))
