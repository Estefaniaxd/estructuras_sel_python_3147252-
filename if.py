''' 



'''

edad = int(input("Ingrese su edad aqui :D:"))
documento = input("Tienes documento:v? (si/no): ")

# Si el usuario tiene 18 años o más
if edad >= 18 and documento == 'si': 
    numero_documento = input("Ingrese su número de documento: ")
    print(f"Tu número de documento es: {numero_documento}")
    print("Eres mayor de edad, puedes votar") 
else:
    print("Es menor de edad, no puede votar, sapa")

# Este código se ejecuta siempre
print("Fin del programa")
