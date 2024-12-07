raio = int(input("Digite o raio: "))
print(f"a area é: {math.pi*(raio**2)}")
print("--------------")

import math
lado = int(input("Digite o lado: "))
area = lado **2
print(f"a area é: {area}")
print(f"o dobro da area é {area*2}")
print("--------------")

import math
metrosquadrados = float(input("digite o metro da área: "))
latas = math.ceil(metrosquadrados/54)
preco = latas * 80
print(f"voce precisa comprar {latas:.0f} lata(s), custando R${preco:.2f}")
print("--------------")  

import math
metrosQuadrados = float(input('Digite os m²: '))
metrosQuadradosMaisDez = metrosQuadrados * 1.0
 
rendimentoLitro = 6
litrosLata = 18
precoLata = 80
rendimentoLata = rendimentoLitro * litrosLata
litrosGalao = 3.6
precoGalao = 25
rendimentoGalao = rendimentoLitro * litrosGalao
 
somenteLatas = math.ceil(metrosQuadrados / rendimentoLata)
somenteGaloes = math.ceil(metrosQuadrados / rendimentoGalao)
latas = math.floor(metrosQuadradosMaisDez / rendimentoLata)
galoes = math.ceil((metrosQuadradosMaisDez % rendimentoLata) / rendimentoGalao)
 
print(
    f'Somente Latas: {somenteLatas}, custando R${somenteLatas * precoLata}\n'
    f'Somente Galões: {somenteGaloes}, custando R${somenteGaloes * precoGalao}\n'
    f'Latas: {latas} , Galões: {galoes}, '
    f'custando R${((latas * precoLata) + (galoes *precoGalao)):.2f}')
print("--------------")  

metro = int(input("Informe o metro: "))
print(f"a conversão de metros para centimetro é {metro * 100}")
centimetro  = int(input("Informe o centimetro: "))
print(f"a conversão de centimetro para metros é {centimetro / 100}")
print("--------------")
