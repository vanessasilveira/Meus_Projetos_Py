def soma(numA, numB):
    somatorio = numA + numB 
    return somatorio 
resultado = soma(5, 10)
print(f"O resultado da função: {resultado}")
print("--------------")

def somas(numc, numd):
    return numc * numd 
result = somas(5, 5)
print(f"O resultado é {result}")
print("--------------")

def somass(nume, numed):
    return nume / numed
resulta = somass(10,5)
print(f"o resultsdo é   {resulta}")
print("--------------")

numero = int(input("Informe um numero: "))
numero1 = int(input("Informe um numero: "))
soma = numero+numero1
print(f"a soma do numero {numero} + {numero1} é igual a {soma}")
print("--------------")

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite um número real: "))
resultado1 = (2 * num1) * (num2 / 2)
resultado2 = (3 * num1) + num3
resultado3 = num3 ** 3
print(f"O produto do dobro do primeiro com metade do segundo é: {resultado1}")
print(f"A soma do triplo do primeiro com o terceiro é: {resultado2}")
print(f"O terceiro número elevado ao cubo é: {resultado3}")
print("--------------")
def soma(a, b):
 return a + b
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = soma(num1, num2)
print("A soma é:", resultado)
print("--------------")

valora = int(input("Digite o valor de a: "))
print(f"Você digitou: {valora}")
valerb = int(input("digite o valor de b: "))

valorc =""
if valora == valerb:
    valorc =  valora + valerb
else:
    valorc = valora * valerb
print("O valor de C é:", valorc)
print("--------------")

a=float(input("Digite o primeiro numero: "))
b=float(input("Digite o primeiro numero: "))
operacao = input("Escolha a operação(+, -, *, /, //, **, %): ")
if operacao == "+":
  print(f"Resultado: {a + b}")
elif operacao == "-":
  print(f"Resultado: {a - b}")
elif operacao == "*":
  print(f"Resultado: {a * b}")
elif operacao == "/":
  print(f"Resultado: {a / b}")
elif operacao == "//":
  print(f"Resultado: {a // b}")
elif operacao == "**":
  print(f"Resultado: {a ** b}")
elif operacao == "%":
  print(f"Resultado: {a % b}")
else:
  print("Operação inválida.")
print("--------------")

a = float(input("Digite um numero: "))
b = float(input("Digite outro numero: "))
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)
print("--------------")

print(12/2)
print(12//2)
print(12%2)
print(12*2)
print(12**2)
print("--------------")

produto1 = 20
produto2 = 10
print( produto1 + produto2)
print( produto1 - produto2)
print( produto1 * produto2)
print( produto1 / produto2)
print( produto1 // produto2)
print( produto1 % produto2)
print( produto1 ** produto2)
print("--------------")

x = (10+5)*4
x1 = 10+5*4
print(f" o valor de x é: {x} e o valor de x1 é: {x1}  ")
y = 10/2+25*2-2**2
y1 = (10/2) + 25*((2- 2)**2)
print(f"o valor de y é igua a: {y} e o valor de y1 é igual a: {y1}")
print("--------------")

num = int(input("Digite um numero: "))
if num % 2 == 0:
  print(f"{num} é par. ")
else:
  print(f"{num} é impar. ")
print("--------------")


numeros = sorted(map(int, input("Digite os números separados por espaço: ").split()))
alvo = int(input("Digite o número a buscar: "))

esq, dir = 0, len(numeros) - 1
while esq <= dir:
    meio = (esq + dir) // 2
    if numeros[meio] == alvo:
        print(f"{alvo} encontrado na posição {meio}.")
        break
    elif numeros[meio] < alvo:
        esq = meio + 1
    else:
        dir = meio - 1
else:
    print(f"{alvo} não encontrado.")
print("--------------")

numero = int(input("Informe um numero: "))
print(f"o numero informado foi {numero}")
print("--------------")


numero1 = int(input("digite o primeiro valor: "))
numero2 = int(input("digite o segundo valor: "))
diferença = numero1 / numero2
print(f"a diferença entre o {numero1} e o {numero2} é igual a {diferença}")
print("--------------")

numA = int(input("digite o primeiro valor: "))
numB = int(input("digite o segundo valor: "))
res = numA
numA = numB 
numB = res
print(f"o valor de a era {numA} agora o valor de a é: {numB}")
print(f"o valor de b era {numB} agora o valor de b é: {numA}")
print("--------------")

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
if num1 > num2:
    print("O primeiro número é maior.")
elif num1 < num2:
    print("O segundo número é maior.")
else:
    print("Os números são iguais.")
print("--------------")


# Solicita ao usuário que insira os dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Verifica se o segundo número é diferente de zero para evitar divisão por zero
if num2 == 0:
    print("Erro: Divisão por zero não é permitida.")
else:
    # Verifica a divisibilidade
    if num1 % num2 == 0:
        print(f"{num1} é divisível por {num2}.")
    else:
        print(f"{num1} não é divisível por {num2}.")
print("--------------")

def gerador_numeros():
 for i in range(1, 6):
  yield i
for numero in gerador_numeros():
 print(numero)
print("--------------")

try:
 num1 = float(input("Digite o primeiro número: "))
 num2 = float(input("Digite o segundo número: "))
 resultado = num1 / num2
 print("O resultado da divisão é:", resultado)
except ZeroDivisionError:
 print("Erro: Divisão por zero não é permitida.")
print("--------------")

n = int(input("Digite o número de termos: "))
a, b = 0, 1
for _ in range(n):
  print(a, end=" ")
  a, b = b, a + b
print("--------------")
