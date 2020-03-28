#Programa aumento salarial 15%
def salario(atual, aumento_salarial, com_acrescimo):
  print("Salário atual: R$", salario_atual)
  print("Valor do aumento salarial: R$" ,valor_aumento)
  print("Novo salário: R$", novo_salario)

#Pedir o salário atual do funcionário
salario_atual = float(input('Digite seu salário atual: R$'))

#Valor do aumento
valor_aumento = novo_salario - salario_atual

#Salário com acréscimo de 15%
novo_salario = salario_atual * 1.15

salario(salario_atual, valor_aumento, novo_salario)