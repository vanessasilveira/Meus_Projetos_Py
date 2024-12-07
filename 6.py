def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]  # Troca os valores
    return lista

# Exemplo de uso:
lista = [5, 2, 9, 1, 5, 6]
print("Lista ordenada:", ordenar_lista(lista))
print("--------------")

def encontrar_maior(lista):
    if not lista:  # Verifica se a lista está vazia
        return "A lista está vazia."
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

# Entrada de valores da lista
valores = [10, 23, 58, 4, 7, 33]

# Exibição do maior número
maior_numero = encontrar_maior(valores)
print(f"--------------\no maior numero na lista é: {maior_numero}\n--------------")

def encontrarLista(lista):
    return max(lista)
lista = [10,200,15,8,25,55]
print(f"o maior numero é: {encontrarLista(lista)}")
print("--------------")

def encontrar_numero_faltando(lista):
    n = len(lista) + 1  # O número total de elementos seria len(lista) + 1
    soma_total = n * (n + 1) // 2  # Fórmula da soma dos números de 1 a N
    soma_lista = sum(lista)  # Soma dos números na lista fornecida
    return soma_total - soma_lista  # O número faltante é a diferença

# Exemplo de uso:
lista = [1, 2, 4, 5, 6]
print("Número faltando:", encontrar_numero_faltando(lista))
print("--------------")

def encontrar_menor_numero(lista):
    menor = min(lista)  # Função min encontra o menor valor na lista
    return menor

# Exemplo de uso:
lista = [10, 4, 7, 1, 9]
print("O menor número da lista é:", encontrar_menor_numero(lista))
print("--------------")

lista = [ 5,6,8,9,2,3,]
soma = sum(lista)
print(f"A soma dos numeros é {soma}")
print("--------------")

numeros = list(map(int, input("Digite os numeros separados por espaço: ").split()))
for i in range(len(numeros)):
  for j in range(0, len(numeros)- i -1):
    if numeros[j]>numeros[j + 1]:
        numeros[j], numeros[j + 1]= numeros[j + 1], numeros[j]
print("Lista ordenada:", numeros)
        
print("--------------")

numeros = list(map(int, input("Digite os números separados por espaço: ").split()))
alvo = int(input("Digite o número a buscar: "))
if alvo in numeros:
    print(f"{alvo} encontrado na posição {numeros.index(alvo)}.")
else:
    print(f"{alvo} não encontrado.")
print("--------------")

dobro = lambda x: x * 2
numeros = [1, 2, 3, 4, 5]
dobrados = list(map(dobro, numeros))
print(dobrados)
print("--------------")

from functools import reduce
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
soma_pares = reduce(lambda x, y: x + y, pares)
print("Números pares:", pares)
print("Soma dos números pares:", soma_pares)
print("--------------")
def verificar_conjuntos_iguais(conjunto1, conjunto2):
    return conjunto1 == conjunto2

# Exemplo de uso:
conjunto1 = {1, 2, 3, 4}
conjunto2 = {4, 3, 2, 1}
if verificar_conjuntos_iguais(conjunto1, conjunto2):
    print("Os conjuntos são iguais!")
else:
    print("Os conjuntos não são iguais!")
print("--------------")

for it in range(1,11):
  print(it)
print("--------------")

for i in range(10,0, -1):
    print(i)
print("contagem regressiva terminada! ")
print("--------------")

contador = 10
while contador > 0:
    print(contador)
    contador -= 1
print("contagem regressiva terminada! ")
print("--------------")

import time

# Contagem regressiva de 10 até 1 com intervalo de 1 segundo
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)  # Aguarda 1 segundo

print("Contagem regressiva terminada!")
print("--------------")

