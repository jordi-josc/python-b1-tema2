"""
Enunciado:
Se requiere crear dos funciones que trabajen con una lista de estudiantes
y agreguen un nuevo estudiante a la lista. La diferencia es que la función
'add_student_by_value(list_students, new_student)' debe agregar al nuevo
estudiante usando paso por valor y la función
'add_student_by_reference(list_students, new_student)' usando paso por
referencia. Ambas funciones serán orquestadas desde la función
'main(list_students, new_student)' la cual ya está definida.

La función 'add_student_by_value(list_students, new_student)' debe copiar
la lista de estudiantes para no afectar la lista original y agregar al nuevo
estudiante. Esta es la solución de paso por valor.
Parámetros:
    - list_students (List): Lista de estudiantes original.
    - new_student (str): Nombre del nuevo estudiante.

La función 'add_student_by_reference(list_students, new_student)' debe agregar
al nuevo estudiante usando paso por referencia.
Parámetros:
    - list_students (List): Lista de estudiantes original.
    - new_student (str): Nombre del nuevo estudiante.

La función 'main(list_students, new_student)' es la que llamará a las 2
funciones previamente definidas para comprobar que list_students
cambie de acuerdo a la función llamada.
Parámetros:
    - list_students (List): Lista de estudiantes original.
    - new_student (str): Nombre del nuevo estudiante.

Ejemplo:
    Entrada:
    list_students = ['Alice', 'Bob', 'Juan']
    new_student_by_value = 'Maria'
    new_student_by_reference = 'Sofia'

    main(list_students, new_student_by_value, new_student_by_reference)

    Salida:
    Original student list ['Alice', 'Bob', 'Juan']
    Student list by value ['Alice', 'Bob', 'Juan', 'Maria']
    Student list by reference ['Alice', 'Bob', 'Juan', 'Sofia']
    Original student list ['Alice', 'Bob', 'Juan', 'Sofia']


Enunciat:
Cal crear dues funcions que treballin amb una llista d'estudiants
i afegeixin un nou estudiant a la llista. La diferència és que la funció
'add_student_by_value(list_students, new_student)' ha d'afegir al nou
estudiant fent servir pas per valor i la funció
'add_student_by_reference(list_students, new_student)' fent servir pas per
referència. Ambdues funcions seran orquestrades des de la funció
'main(list_students, new_student)' que ja està definida.

La funció 'add_student_by_value(list_students, new_student)' ha de copiar
la llista d'estudiants per no afectar la llista original i afegir al nou
estudiant. Aquesta és la solució de pas per valor.
Paràmetres:
     - list_students (List): Llista d'estudiants original.
     - new_student (str): Nom del nou estudiant.

La funció 'add_student_by_reference(list_students, new_student)' ha d'afegir
al nou estudiant usant pas per referència.
Paràmetres:
     - list_students (List): Llista d'estudiants original.
     - new_student (str): Nom del nou estudiant.

La funció 'main(list_students, new_student)' és la que trucarà a les 2
funcions prèviament definides per comprovar que list_students
canvieu d'acord amb la funció trucada.
Paràmetres:
     - list_students (List): Llista d'estudiants original.
     - new_student (str): Nom del nou estudiant.

Exemple:
     Entrada:
     list_students = ['Alice', 'Bob', 'Juan']
     new_student_by_value = 'Maria'
     new_student_by_reference = 'Sofia'

     main(list_students, new_student_by_value, new_student_by_reference)

     Sortida:
     Original student list ['Alice', 'Bob', 'Juan']
     Student list by value ['Alice', 'Bob', 'Juan', 'Maria']
     Student list by reference ['Alice', 'Bob', 'Juan', 'Sofia']
     Original student list ['Alice', 'Bob', 'Juan', 'Sofia']

"""


def add_student_by_value(list_students, new_student):
    return list_students + [new_student]



def add_student_by_reference(list_students, new_student):
    list_students.append(new_student)
    return list_students


def main(list_students, new_student_by_value, new_student_by_reference):
    print(f"Original student list {list_students}")
    print(f"Student list by value {add_student_by_value(list_students, new_student_by_value)}")
    print(f"Student list by reference {add_student_by_reference(list_students, new_student_by_reference)}")
    print(f"Original student list {list_students}")


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
list_students = ["Alice", "Bob", "Juan"]
new_student_by_value = "Maria"
new_student_by_reference = "Sofia"

main(list_students, new_student_by_value, new_student_by_reference)
