# Ejemplo 1: Operador not
y = not True
print("El valor del resultado de operar con not es:", y)  # Output: False

# Ejemplo 2: Operador and
a = True
b = True
y = a and b
print("El resultado de operar con and es:", y)  # Output: True

# Ejemplo 3: Operador and
a = False
b = True
y = a and b
print("El resultado de operar con and es:", y)  # Output: False

# Ejemplo 4: Operador or
a = False
b = False
y = a or b
print("El resultado de operar con or es:", y)  # Output: False

# Jerarquía de precedencia de operadores
y = False and not True or False
print("El resultado de operar con jerarquía de operadores es:", y)  # Output: False

# Ejemplo 5: Relacionales y lógicos
y = not (3 > 4 and 4 == 4 or 3 < 2)  # Corrected expression
print("El resultado de operar con relacionales y lógicos es:", y)  # Output: True
