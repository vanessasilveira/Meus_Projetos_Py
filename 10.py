quadrados = {x: x**2 for x in range(1, 6)}
print(quadrados)
print("--------------")

quadrados = [x**2 for x in range(1, 11)]
print(quadrados)
print("--------------")

numero = int(input("digite um valor : "))
print(f"Tabuada de {numero}:")
for  i in range (1,11):
    print(f"{numero} x {i} = {numero * i}")
print("--------------")

for numero in range(1,11):
    print(f"\nTabuada de {numero}: ")
    for i in range (1,11):
        print(f"{numero} x {i} = {numero * i}")
print("--------------")
