def ePrimo (numero):
    if numero < 2:
     return False
    for i in range(2, int (numero ** 0.5) + 1):
     if numero % i == 0:
      return False
    return True
numero = int(input("digite um numero: "))
print(f"{numero} é primo? {ePrimo(numero)}")
print("--------------")

num = int(input("Digite um numero: "))
if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5)+1)):
  print(f"{num} é primo.")
else:
  print(f"{num} não é primo. ")
print("--------------")

def decimal_para_binario(numero):
    if numero == 0:
        return "0"  # Caso especial para 0, pois o binário de 0 é 0
    binario = ""  # String para armazenar o número binário
    while numero > 0:
        resto = numero % 2  # Obtém o resto da divisão por 2 (0 ou 1)
        binario = str(resto) + binario  # Adiciona o resto à frente do binário
        numero = numero // 2  # Divida o número por 2 (parte inteira)
    return binario

# Exemplo de uso:
numero_decimal = float(input("Digite um número decimal: "))
binario = decimal_para_binario(numero_decimal)
print(f"O número {numero_decimal} em binário é: {binario}")
print("--------------")

