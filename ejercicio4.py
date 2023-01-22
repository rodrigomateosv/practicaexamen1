import math

def do_math(string):
    # Separar la cadena en una lista de números utilizando el espacio como separador
    num_list = string.split(" ")
    
    # Crear una lista vacía para almacenar las letras y números
    num_list_alpha = []
    
    # Extraer las letras y almacenarlas en la lista junto con los números correspondientes
    for num in num_list:
        for char in num:
            if char.isalpha():
                num_list_alpha.append((num, char))
                break
                
    # Ordenar la lista según las letras
    num_list_alpha = sorted(num_list_alpha, key=lambda x: x[1])
    
    # Realizar los cálculos especificados en el enunciado
    result = float(num_list_alpha[0][0])
    for i in range(1, len(num_list_alpha)):
        if i % 4 == 1:
            result += float(num_list_alpha[i][0])
        elif i % 4 == 2:
            result -= float(num_list_alpha[i][0])
        elif i % 4 == 3:
            result *= float(num_list_alpha[i][0])
        else:
            result /= float(num_list_alpha[i][0])
    
    # Redondear el resultado final al entero más cercano y devolverlo como resultado
    return round(result)
