"""
Enunciado:
Imagina que estás trabajando en una aplicación para calcular factoriales. Crea
una función 'calculate_factorial(number)' que orquestará el proceso del cálculo
del factorial usando la función 'factorial(number)' que recibirá un número entero 
no negativo y calculará su factorial. Por lo tanto, debes manejar las excepciones 
para controlar que las funciones se utilizan correctamente.

De esta manera, 'calculate_factorial(number)' recibe un número entero y calcula su
factorial llamando a 'factorial(number)'. Si ocurre una excepción al invocar a 
'factorial(number)', debe mostrar el mensaje de error: "An unexpected error has 
occurred: {error}".

Parámetros:
number (int): El número del cual se desea calcular el factorial.

La función 'factorial(number)' calcula el factorial del número. Si el número
introducido es negativo debe lanzar una excepción con el mensaje "Factorial of
a negative number cannot be calculated".

Parámetros:
number (int): El número del cual se desea calcular el factorial.

Ejemplo:
    Entrada:
    calculate_factorial(5)
    calculate_factorial(-5)
    
    Salida:
    - En el primer caso el resultado es: 120
    - En el segundo caso se genera un error: "An unexpected error has occurred: Factorial of a
     negative number cannot be calculated"
    

Enunciat:
Imagina que treballes en una aplicació per calcular factorials. Crea
una funció 'calculate_factorial(number)' que orquestrarà el procés del càlcul
del factorial fent servir la funció 'factorial(number)' que rebrà un name enter
no negatiu i calcularà el factorial. Per tant, has de manejar les excepcions
per controlar que les funcions s'utilitzen correctament.

D'aquesta manera, 'calculate_factorial(number)' rep un name enter i calcula el
factorial cridant a 'factorial(number)'. Si passa una excepció  invocant a
'factorial(number)', ha de mostrar el missatge d'error: "An unexpected error has
occurred: {error}".

Paràmetres:
number (int): El name del qual es vol calcular el factorial.

La funció 'factorial(number)' calcula el factorial del número. Si el número
introduït és negatiu ha de llançar una excepció amb el missatge "Factorial of
a negative number cannot be calculated".

Paràmetres:
number (int): El name del qual es vol calcular el factorial.

Exemple:
     Entrada:
     calculate_factorial(5)
     calculate_factorial(-5)
    
     Sortida:
     - En el primer cas el resultat és: 120
     - En el segon cas es genera un error: "An unexpected error has occurred: Factorial of a
     negative number cannot be calculated"
"""


def factorial(number: int):
    if number < 0:
        raise ValueError("Factorial of a negative number cannot be calculated.")
    if number == 0:
        return 1
    return number * factorial(number - 1)


def calculate_factorial(number: int):
    try:
        return factorial(number)
    except Exception as e:
        return f"An unexpected error has occurred: {e}"

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

calculate_factorial(5)