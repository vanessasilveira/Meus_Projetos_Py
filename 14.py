DISTANCIA_SP_RJ_KM = 435  # Distância entre São Paulo e Rio de Janeiro em km
CONVERSAO_KMH_PARA_MS = 3.6  # Fator de conversão de km/h para m/s

# Entrada de dados
velocidade_kmh = float(input("Digite a velocidade do veículo em km/h: "))

# Conversão de velocidade
velocidade_ms = velocidade_kmh / CONVERSAO_KMH_PARA_MS

# Cálculo do tempo de viagem
tempo_horas = DISTANCIA_SP_RJ_KM / velocidade_kmh
tempo_minutos = tempo_horas * 60  # Convertendo de horas para minutos

# Resultados
print(f"\nVelocidade convertida: {velocidade_ms:.2f} m/s")
print(f"Tempo estimado de viagem de São Paulo até o Rio de Janeiro:")
print(f"  - {tempo_horas:.2f} horas")
print(f"  - ou aproximadamente {tempo_minutos:.0f} minutos")
print("--------------")

temperatura = float(input("digite uma temperatura: "))
if temperatura <= 15:
    print("temperatura esta muito fria ")
elif temperatura >= 15 and temperatura <= 30:
    print("temperatura esta agradavel ")
else:
    print("temperatura esta quente ")
print("--------------")

# Programa para conversão de temperaturas

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius:.2f}°C é igual a {fahrenheit:.2f}°F")
fahrenheit = float(input("Digite a temperatura em fahrenheit: "))
celsius = (fahrenheit * 9/5)-32
print(f"{fahrenheit:.2f} °F é iguel a {celsius:.2f}°C")
print("--------------")

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (5 * (celsius+32) / 9)
print(f"{celsius:.2f}°C é igual a {fahrenheit:.2f}°F")
fahrenheit = float(input("Digite a temperatura em fahrenheit: "))
celsius = (5 * (celsius-32) / 9)
print(f"{fahrenheit:.2f} °F é iguel a {celsius:.2f}°C")
print("--------------")

tamanho = float(input('Digite o tamanho do arquivo em MB: '))
velocidade = float(input('Digite a velocidade da conexão em Mbps: '))
tempos = (tamanho * 8) / velocidade
minutos = tempos // 60
segundos = (tempos % 60)
print(f'{minutos:.0f} Minutos e {segundos:.0f} Segundos')
print("--------------")  
