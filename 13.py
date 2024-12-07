def generate_invoice(invoice):
 total = 0
    # Soma o valor dos produtos e exibe cada item
 for index in invoice["products"]:
        product_name, product_price = invoice["products"][index]
        print(f"- {product_name}: R$ {product_price:.2f}")
        total += product_price  # Acumula o total dos produtos
    
    # Soma dos produtos com os impostos
 total_with_taxes = total + invoice["taxes"]
 print("--------------")
 print(f"Impostos: R$ {invoice['taxes']:.2f}")
 print(f"Total com impostos: R$ {total_with_taxes:.2f}")

# Chama a função para gerar a fatura
 generate_invoice(invoice)
print("--------------")

class FormaBolo:
    def __init__(self, sabor_massa, sabor_recheio):
        self.sabor_massa = sabor_massa
        self.sabor_recheio = sabor_recheio

    def escrever(self):
        print(f"Um delicioso bolo de {self.sabor_massa} com recheio de {self.sabor_recheio}.")

    def assar(self):
        print(f"Bolo assando de {self.sabor_massa}.")

# Criando instâncias
bolo_festa = FormaBolo("chocolate", "nutella")
bolo_premium = FormaBolo("baunilha", "coco")

# Chamando métodos
bolo_festa.escrever()  # Saída: Um delicioso bolo de chocolate com recheio de nutella.
bolo_premium.escrever()  # Saída: Um delicioso bolo de baunilha com recheio de coco.
bolo_premium.assar()  # Saída: Bolo assando de baunilha.

print("--------------")

def torrar(pao, nome = "cliente", valor =19.90):

    print(f"torrada feita com {pao}")
    print(f"pedido de {nome}")
    print(f"o valor total é  {valor}")
torrar ("pão integral", "vanessa")
print("--------------")


try:
    valorProduto = float(input("Digite o valor do produto: R$ "))
    if valorProduto <= 0:
        print("Por favor, insira um valor válido para o produto.");
        exit()
except ValueError:
    print("Por favor, insira um valor válido para o produto.")
    exit()
print("\nEscolha a forma de pagamento:");
print("1 - Dinheiro ou PIX (10% de desconto)");
print("2 - Cartão à vista (5% de desconto)");
print("3 - Cartão 2x (preço normal)");
print("4 - Cartão 3x ou mais (10% de acréscimo)");
try:
    formaPagamento = int(input("Digite a forma de pagamento (1, 2, 3 ou 4): "))
    if formaPagamento < 1 or formaPagamento > 4:
        print("Por favor, insira uma forma de pagamento válida (1, 2, 3 ou 4).")
        exit() 
except ValueError:
    print("Por favor, insira um número inteiro válido para a forma de pagamento.")
    exit()
if formaPagamento == 1:
    valorFinal = valorProduto * 0.9  # 10% de desconto
elif formaPagamento == 2:
    valorFinal = valorProduto * 0.95  # 5% de desconto
elif formaPagamento == 3:
    valorFinal = valorProduto  # Preço normal
elif formaPagamento == 4:
    valorFinal = valorProduto * 1.1  # 10% de acréscimo

print(f"\nO valor final do produto é: R$ {valorFinal:.2f}")
print("--------------")

frutas = ["maçã", "banana", "laranja", "uva"]
for fruta in frutas:
  print(fruta)
print("--------------")

# Definindo o objeto invoice como um dicionário
invoice = {
    "name": "Vanessa",
    "age": 19,
    "products": {
        0: ["mouse", 29.90],
        1: ["teclado", 129.99],
        2: ["monitor", 899.90]
    },
    "taxes": 98.90
}





