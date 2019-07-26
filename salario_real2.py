salario = int(input('5000'))
imposto = (input('20.5'))
if imposto == '':
    imposto = 20.5
else:
    imposto = float(imposto)
print("Valor real: {0}".format(salario - (salario*imposto*0.01)))