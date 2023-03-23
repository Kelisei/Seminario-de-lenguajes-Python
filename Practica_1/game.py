from random import choice, randrange
from datetime import datetime
# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now() 
exitos = 0
fallos = 0
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    while operator == '/' and number_2 == 0:
        number_2 = randrange(10)
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = float(input("resultado: "))
    match operator:
        case("+"):
            aux = (number_1 + number_2)
        case("-"):
            aux = (number_1 - number_2)
        case("*"):
            aux = (number_1 * number_2)
        case("/"):
            aux = (number_1 / number_2)
    if aux == result:
        print('Es correcto')
        exitos += 1
    else:
        print('Es incorrecto')
        fallos += 1
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\nTardaste {total_time.seconds} segundos.")
print(f'Exitos: {exitos} Fallos:  {fallos}')
