from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-","*","/"]


# Cantidad de cuentas a resolver
times = 5


# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()

#Contador de opciones correctas
correct_ans = 0

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):

    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)

    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")

    # Le pedimos al usuario el resultado
    result = int(input("resultado: "))

    #Calculo el resultado correcto para comparar
    if(operator == "+"):
        real_result = number_1 + number_2
    elif(operator == "-"):
        real_result = number_1 - number_2
    elif(operator == "*"):
        real_result = number_1 * number_2
    elif(operator == "/"):
        if (number_2 == 0):
            real_result = result + 1
            print("divicion por cero es imposible")
        else:
            real_result = number_1 // number_2 #Uso diviciones enteras para no tener conflicto con los numeros enteros

    if (result == real_result):
        #sumo las respuestas correctas e imprimo si fue correcta o no
        print("La respuesta fue correcta")
        correct_ans += 1
    else:
        print("La respuesta fue incorrecta")

# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()

# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time

print("-"*10)
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")

#informo cuantas respuestas se respondieron bien
print("has respondido correctamente {} operaciones".format(correct_ans))

#informo cuantas respuestas se respondieron  mal
print("has respondido incorrectamente {} operaciones".format(times-correct_ans))
print("-"*10)



#FALTA

#Tener en cuenta la divicion por 0 
#Se puede mejorar usando funciones