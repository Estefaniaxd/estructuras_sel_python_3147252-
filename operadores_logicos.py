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