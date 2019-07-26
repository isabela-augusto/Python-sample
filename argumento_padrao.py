def salario_descontado_imposto(salario, imposto=27.):
    return salario - (salario * imposto * 0.01)
print(salario_descontado_imposto(5000,2))
