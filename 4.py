import math

valor_por_hora = float(input("Quanto você ganha por hora? R$: "))
horas_trabalhadas = float(input("Quantas horas você trabalhou neste mês? "))
salario_total = valor_por_hora * horas_trabalhadas
print(f"Seu salário neste mês será de R$ {salario_total:.2f}")
print("--------------")

valorSalario = float(input("Digite o valor do salário: "));
valorBeneficios = float(input("Digite o valor do benefício: "));
valorImposto = 0
if valorSalario >= 0 and valorSalario <= 1100:
     valorImposto = 0.05 * valorSalario
elif valorSalario > 1100 and valorSalario <= 2500:
     valorImposto = 0.10 * valorSalario
else:
     valorImposto = 0.15 * valorSalario

saida = valorSalario - valorImposto + valorBeneficios
print(f"Resultado: {saida:.2f}")
saldoTotal = saida
while True:
  Retirada = float(input("digite o quanto vai querer sacar: "))
      
  if Retirada > saldoTotal:
    print("Erro: Valor da retirada excede o saldo disponível. Escolha outro valor.")
  elif Retirada <= 0:
    print("Erro: O valor da retirada deve ser maior que zero. Escolha outro valor.")
  elif saldoTotal - Retirada < 100:
    print("Erro: A conta deve manter pelo menos R$100 após o saque. Escolha outro valor.")
  else:
    saldoTotal -= Retirada
    print(f"Saque de R${Retirada:.2f} realizado com sucesso.")
    print(f"Saldo disponível: R${saldoTotal:.2f}")
    break
print("--------------") 

salariobruto = float(input("digite o seu salario: "))
salarioliquido = salariobruto - 11/100 - 8/100 - 5/100
print(f"Você tinha um salario bruto no valor de {salariobruto}") 
print(f"O valor total tirando os impostos é de {salarioliquido}")
print("--------------")  
  
limite = 50
multa = 4
peso = float(input("Digite o peso de peixes (em quilos): "))
excesso = max(0, peso - limite)
multa = excesso * multa
print("\n=== Resultado ===")
print(f"Peso total dos peixes: {peso:.2f} Kg")
if excesso > 0:
    print(f"Excesso de peso: {excesso:.2f} kg")
    print(f"Multa a ser paga: R$ {multa:.2f}")
else:
    print("Não houve excesso de peso. Nenhuma multa será aplicada.")
print("--------------")    
