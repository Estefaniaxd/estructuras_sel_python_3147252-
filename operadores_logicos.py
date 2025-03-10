'''
Operdores Logicos Aquellos que operan unicamente 
con valores boleacos (True o False ) (V or F )
acorde a las tablas de verdad

'''
#Ejemplo 1; Operador not:y= not True 
print("el valor del resultado de operar con not es", y) # type: ignore


#ejemplo 2: operador and 
a = True
b = True
y = a and b
print("El resultado de operar con and es: ", y) # type: ignore

#ejemplo 2: operador and 
a = False
b = True
y = a and b
print("El resultado de operar con and es: ", y) # type: ignore

#ejemplo 3: operador or
a = False
b = False
y = a or b
print("El resultado de operar con or es: ", y) # type: ignore

'''
jerarquia de predencia de operadores 
(logicos inclusive)
1. ()
2. **
3. *, /, //, %
4. +, -
5. ==, !=, >, <, >=, <=
6. not
7. and
8. or
'''

#ejemplo 4  jerarquia de operadores 
y = False and not True or False
print("El resultado de operar con jerarquia de operadores es: ", y) # type: ignore 


#ejemplos 5 : relacionales y logicos

y = not 3 > 4 and 4 == 4 or 3 < 2