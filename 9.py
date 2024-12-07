def calcular_fatorial(numero):
    if numero < 0:
        return "Fatorial não é definido para números negativos."
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i  # Multiplica o número atual ao resultado acumulado
    return fatorial

# Entrada do usuário
numero = int(input("Digite um número para calcular o fatorial: "))

# Cálculo e saída
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")
print("--------------")

import math
num = int(input("Digite um numero: "))
print(f"o fatorial de {num} é: {math.factorial(num)}")
print("--------------")

import unittest
# Função a ser testada
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
# Classe de teste
class TestFatorial(unittest.TestCase):
    def test_fatorial_0(self):
        self.assertEqual(fatorial(0), 1)
    
    def test_fatorial_5(self):
        self.assertEqual(fatorial(5), 120)
    
    def test_fatorial_10(self):
        self.assertEqual(fatorial(10), 3628800)
# Executa os testes
if __name__ == '__main__':
    unittest.main()
print("--------------")
