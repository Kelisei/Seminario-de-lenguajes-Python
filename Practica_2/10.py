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

def generate_joint_structure(names, marks_1, marks_2):
    """The function recives a string and two list with marks and the generates a zip object which contains
    a tuple with the name alongside the two marks corresponding to each student"""
    formatted_names = names.replace("\n", "")
    formatted_names = formatted_names.split(',') 
    return tuple(zip (formatted_names, marks_1, marks_2))

def calculate_average_individual(union):
    """The function recives a lsit with tuples containing the name and the two marks of each student and calculates
    the average of the marks for each student. It then returns a dictionary where the keys are the student
    names and the values are their corresponding average marks."""
    average = dict()
    for elem in union:
        average[elem[0]] = sum([x for x in elem if isinstance(x, (int))])/2
    return average

def calculate_average_class(average):
    """This function recives a dictionary with the average marks of all the students in a class and
    calculates the overall average marks for the class."""
    total = 0
    for student in average:
        total += average[student]
    return total / len(average)

def max_student(average_per_student):
    return max(average_per_student, key=average_per_student.get)

def min_student(students):
    """This function recives a tuple of tuples, the tuple is conformed in [0] of a name, and in [1][2] of marks, 
    For key of the min function we use a lambda which returns the minimum of the [1] and [2] element of a tuple 
    (the marks), we calculate the min of all the tuples and get tuple with lowest mark then we return the name 
    of the student with [0]. 
    """
    return min(students, key=lambda x: (min(x[1], x[2])))[0] 


union = generate_joint_structure(nombres, notas_1, notas_2)
average_per_student = calculate_average_individual(union)
class_average = calculate_average_class(average_per_student)

print(f'The class average is : {class_average}')
print(f'The student with the highest average grade is {max_student(average_per_student)}')
print(f'The student with the lowest grade is {min_student(union)}')