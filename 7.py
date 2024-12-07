saldoTotal = 200
saque = 200
while True:
  Retirada = float(input("digite o quanto vai querer sacar: "))
      
  if Retirada > saldoTotal:
    print("Erro: Valor da retirada excede o saldo disponível. Escolha outro valor.")
  elif Retirada >= saque:
    print("Erro: O valor excede o limite de saque permitido. Escolha outro valor.")
  elif Retirada <= 0:
    print("Erro: O valor da retirada deve ser maior que zero. Escolha outro valor.")
  else:
    saldoTotal -= Retirada
    print(f"Saque de R${Retirada:.2f} realizado com sucesso.")
    print(f"Saldo disponível: R${saldoTotal:.2f}")
    break
print("--------------")

  
soldo = 500
print(soldo)
soldo = 200
print(soldo )
soldo += 10 
print(soldo )
soldo -= 5
print(soldo )
soldo /= 2
print(soldo )
soldo //= 2
print(soldo )
soldo *= 10
print(soldo )
soldo %= 4
print(soldo )
soldo **= 2
print(soldo )
print("--------------")

saldo = 1000
saque =  200
limite = 100
conta = True

exp = saldo >= saque and saque <= limite or conta and saldo >= saque
print(exp)
exp2 = (saldo >= saque and saque <= limite) or (conta and saldo >= saque)
print(exp2)
saldosuficiente = saldo >= saque and saque <= limite 
saldoespecial = conta and saldo >= saque 
exp3 = saldosuficiente or saldoespecial
print(exp3)
print("--------------")

saldo = 1000
saque =  200
limite = 100
print(saldo >= saque and saque >= limite )
print(not saldo <= saque)
print(saldo >= saque or saque <= limite )
print(saldo >= saque or saque >= limite )
print(saldo <= saque or saque <= limite )
print(not saldo >= saque)
print(saldo <= saque or saque <= limite )
print(saldo >= saque and saque <= limite )
print(saldo <= saque and saque <= limite )
print(saldo <= saque and saque <= limite )
print("--------------")



