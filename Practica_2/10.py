nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def generate_joint_structure(names, marks_1, marks_2): #A
    """Para esta funcion recibimos las 3 estructuras (el string, y las 2 listas de notas),
    al string lo formateamos para que quede cada nombre separado y en una lista, luego cen la 
    comprension de diccionarios con zip generamos una estructura que une los 3, que tiene de datos
    el nombre [0], y las 2 notas [1], [2], entonces usamos de clave el nombre y de valor los unimos a las notas
    en una tupla"""
    formatted_names = names.replace("\n", "").replace("'", "").replace(" ", "").split(',') 
    return {name:(mark1, mark2) for name, mark1, mark2 in zip(formatted_names, marks_1, marks_2)}
 
def calculate_average_individual(union): #B
    """Usando comprension de diccionarios, utilizamos como llaves del actual la llaves del diccionario 
    recibido, y que el valor sea la suma de los valores dentro del valor del diccionario recibido dividido 2"""
    return {name: sum(marks) / 2 for name, marks in union.items()}

def calculate_average_class(average): #C
    """Esta funcion recibe un diccionario con las notas promedio de todos los estudiantes 
    en una clase y calcula el promedio general de notas para la clase."""
    return sum(average.values()) / len(average)

def max_student(average_per_student): #D
    return max(average_per_student, key=average_per_student.get)

def min_student(students): #E
    """Recibe un diccionario creado en generate_joint_structure que posee las 2 notas como valor, y
    de clave el nombre del alumno, de entre cada valor saco cual es la nota más baja y esa es 
    mi key para el minimo en todo el diccionario"""
    return min(students, key=lambda x: min(students[x])) 

union = generate_joint_structure(nombres, notas_1, notas_2)
average_per_student = calculate_average_individual(union)
class_average = calculate_average_class(average_per_student)

# El primer print no estaba en el video, fue agregado después
print(f'Average per student: {average_per_student}')
print(f'The class average is : {round(class_average, 2)}')
print(f'The student with the highest average grade is {max_student(average_per_student)}')
print(f'The student with the lowest grade is {min_student(union)}')
