nome = input("Digite o nome do herói: ")
xp = int(input("Digite a quantidade de experiência (XP) do herói: "))  # Converte para inteiro

# Inicializando a variável de nível com base no XP
if xp < 1000:
    nivel = "Ferro"
elif xp <= 2000:
    nivel = "Bronze"
elif xp <= 5000:
    nivel = "Prata"
elif xp <= 7000:
    nivel = "Ouro"
elif xp <= 8000:
    nivel = "Platina"
elif xp <= 9000:
    nivel = "Ascendente"
elif xp <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

# Exibindo o resultado
print(f"O Herói de nome {nome} está no nível de {nivel}.")
print("--------------")

class Heroi:
    def __init__(self, nome_heroi, idade_heroi, tipo_heroi):
        self.nome_heroi = nome_heroi
        self.idade_heroi = idade_heroi
        self.tipo_heroi = tipo_heroi

    def atacar(self):
        if self.tipo_heroi == "mago":
            ataque = "magia"
        elif self.tipo_heroi == "guerreiro":
            ataque = "espada"
        elif self.tipo_heroi == "monge":
            ataque = "artes marciais"
        elif self.tipo_heroi == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido"

        print(f"O {self.tipo_heroi} atacou usando {ataque}.")

# Exemplo de uso:
heroi1 = Heroi("Arthur", 30, "guerreiro")
heroi2 = Heroi("Merlin", 150, "mago")

heroi1.atacar()  # Saída: O guerreiro atacou usando espada.
heroi2.atacar()  # Saída: O mago atacou usando magia.
print("--------------")

a = 10
b = 20
res = a
a = b 
b = res
print(f"o valor de a era 10 agora o valor de a é: {a}")
print(f"o valor de b era 20 agora o valor de b é: {b}")
print("--------------")

def createDatabase(databaseName, user, password):
    print(f"connect:DBCONNECT;user={user};pass={password};initial_database={databaseName}")
createDatabase("db_produts", "vanessa", "8956")
print("--------------")

import requests
resposta = requests.get("https://api.agify.io?name=michael")
dados = resposta.json()
print(dados)
print("--------------")

from datetime import datetime

# Função para ler e validar a data
def ler_data(mensagem):
    while True:
        try:
            data = input(mensagem).strip()
            # Aceita entrada sem barras e converte para o formato com barras
            if len(data) == 8 and data.isdigit():
                data = f"{data[:2]}/{data[2:4]}/{data[4:]}"
            return datetime.strptime(data, "%d/%m/%Y")
        except ValueError:
            print("Formato inválido. Por favor, use o formato dd/mm/yyyy ou ddmmyyyy.")

# Entrada das datas
data1 = ler_data("Digite a primeira data (dd/mm/yyyy ou ddmmyyyy): ")
data2 = ler_data("Digite a segunda data (dd/mm/yyyy ou ddmmyyyy): ")

# Exibindo a diferença entre as datas
diferenca = abs((data2 - data1).days)
print(f"A diferença entre as datas é de {diferenca} dias.")
print("--------------")
