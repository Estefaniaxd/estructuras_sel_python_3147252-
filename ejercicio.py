motor_encendido = True

temperatura = int(input("cual es la temperatura del motor"))

if  temperatura > 80:
    motor_encendido = False
    print("temperatura demasiado alta, se apagara")
else:
    print("Temperatura baja y estable: :D")
    
print ("Chaooo")