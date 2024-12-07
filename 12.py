def inverter_string(texto):
    return texto[::-1]  # Inverte a string usando slicing

# Entrada do usuário
texto = input("Digite uma string para inverter: ")

# Inversão e saída
texto_invertido = inverter_string(texto)
print(f"A string invertida é: {texto_invertido}")
print("--------------")

def verificar_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()  # Remove espaços e converte para minúsculas
    return palavra == palavra[::-1]

# Exemplo de uso:
palavra = input("Digite uma palavra: ")
if verificar_palindromo(palavra):
    print(f"{palavra} é um palíndromo!")
else:
    print(f"{palavra} não é um palíndromo!")
print("--------------")

def inverterString(str):
    return str[::-1]
palavra = "hello"
print(f"a palavra invertida é {inverterString(palavra)}")
print("--------------")

texto = input("Digite uma string: ")
print(f"a string tem {len(texto)} caracteres. ")
print("--------------")

texto = input("Digite uma string: ")
print(f"a string invertida {texto[::-1]}")
print("--------------")

texto = input("Digite uma string: ").replace("", "").lower()
if texto == texto[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
print("--------------")

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
print("--------------")

print("Hello, World")
print("--------------")

nome = input("digite o seu nome: ")
sobrenome = input("digite o seu sobrenome: ")
print(f"o nome completo é {nome} {sobrenome}")
print("--------------")

def meu_decorador(func):
 def wrapper():
    print("Iniciando função")
    func()
    print("Função finalizada")
 return wrapper
@meu_decorador
def diz_ola():
 print("Olá!")
diz_ola()
print("--------------")

frase = input("Digite uma frase: ")
print("Maiúsculas:", frase.upper())
print("Minúsculas:", frase.lower())
print("Capitalizado:", frase.title())
print("--------------")
