# Função para gerar a fatura
def generate_invoice(invoice):
    print(f"O comprador é {invoice['name']}.")
    print(f"A idade é {invoice['age']}.")
    print("\nProdutos comprados:")
    
    total = 0  # Variável para calcular o total
    for index, value in invoice["products"].items():  # Aqui é corrigido o acesso
        product, price = value
        print(f"- {product}: R$ {price:.2f}")
        total += price
    
    print(f"\nImpostos: R$ {invoice['taxes']:.2f}")
    total += invoice["taxes"]
    print(f"Total a pagar: R$ {total:.2f}")
    print("--------------")

# Chamando a função


invoice = {
    "name": "vanessa",
    "age": 19,
    "products": {
        0: ["mouse", 29.90],
        1: ["teclado", 129.99],
        2: ["monitor", 899.90]
    },
    "taxes": 98.90  # Corrigido o valor para um float ao invés de string
}

def generate_invoice(invoice):
    print(f"O comprador é {invoice['name']}")
    print(f"A idade é {invoice['age']}")
    print("--------------")

nome = input("informe o seu nome: ")
idade = int(input("informe sua idade: "))
print(f" Meu nome é {nome}, tenho {idade} anos")
print(5//5)# = 1
print("--------------")

nome = "luiz"
idade = int(input("Digite a idade: "))
peso = 80
if (idade < 18):
  print(f"{nome} que pesa {peso}kg é menor de idade porque tem {idade} anos")
else:
     print(f"{nome} que pesa {peso}kg é maior de idade porque tem {idade} anos")
print("--------------")

pessoa = {
"nome": "Ana",
"idade": 30,
"cidade": "São Paulo"
}

print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
print("--------------")

class Pessoa:
 def __init__(self, nome, idade):
  self.nome = nome
  self.idade = idade

 def cumprimentar(self):
  print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
pessoa1 = Pessoa("Carlos", 28)
pessoa1.cumprimentar()
print("--------------")

import sqlite3
# Conectando ao banco de dados (ou criando um novo)
conexao = sqlite3.connect('meu_banco.db')
cursor = conexao.cursor()
# Criando uma tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas
(id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)''')
# Inserindo alguns registros
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES ('Bob', 25)")
# Confirmando as alterações
conexao.commit()
# Consultando os registros
cursor.execute("SELECT * FROM pessoas")
for row in cursor.fetchall():
 print(row)
# Fechando a conexão
conexao.close()
print("--------------")
