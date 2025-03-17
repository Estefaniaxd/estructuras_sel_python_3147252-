
estado_civil = input("Ingresa tu estado civil (soltero/casado/comprometido): ").strip().lower()
edad = int(input("Ingresa tu edad: "))
temperamento = input("Ingresa tu temperamento (buena persona/mala persona): ")
fisico = input("Ingresa tu físico (lindo/feo): ")
salario = int(input("Ingresa tu salario mensual en dólares: "))



if estado_civil == "casado" or estado_civil == "comprometido":
    print("No puedes casarte con esa persona, ya tienes un compromiso.")
elif edad < 18:
    print("No puedes casarte con esa persona, eres menor de edad.")
elif temperamento == "mala persona":
    print("No puedes acercarte a esa persona, su temperamento no es bueno.")
elif fisico == "feo":
    print("No puedes acercarte a esa persona por su físico.")  
elif salario < 200000:
    print("No puedes casarte con esa persona, necesitas mejorar tu situación financiera.")
else: 
    print("Tu salario es excelente, puedes casarte y vivir cómodamente.")

print("Fin del programa.")

    
