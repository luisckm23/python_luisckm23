edad = int(input("Ingresa tu edad: " ))

if edad < 0 or edad > 100:
    print("La edad es incorrecta")
else:
    print("Edad correcta")

salario_empresa = int(input("Ingrese su salario: "))

salario_presidente = 30
salario_director = 15
salario_gerente = 10
salario_operador = 7

if salario_empresa == salario_director:
    print("Eres el director")
elif salario_empresa == salario_presidente:
    print("Eres el presidente")
elif salario_empresa == salario_gerente:
    print("Eres el gerente")
elif salario_empresa == salario_operador:
    print("Eres el operador")
else:
    print("No trabajas aqui")