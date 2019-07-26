salario = int(input('5000'))
imposto = float(input('20.5'))
salario_real = (salario - (salario*imposto*0.01))
print("Valor real: {0}".format(salario_real))