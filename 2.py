nomeAluno = "luiz"
print("Aluno "+ nomeAluno)
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
nota4 = float(input("Digite a quarta nota do aluno: "))
soma = (nota1 + nota2 + nota3 + nota4) / 4
if  soma >= 7:
    print(f"{nomeAluno} foi aprovado com nota {soma: .1f}")
else:
   print(f"{nomeAluno} foi reprovado com nota {soma:.1f}");
print("--------------")

primeiraNota = float(input("Digite a primeira nota do aluno: "))
segundaNota = float(input("Digite a segunda nota do aluno: "))
terceiraNota = float(input("Digite a terceira nota do aluno: "))
somaNotas = (primeiraNota + segundaNota + terceiraNota) / 3
print(f"a media das notas é  {somaNotas:.2f}")
print("--------------")

grade = float(input("Insira a sua nota: "))
if grade < 7:
    print("Você foi reprovado.")
else:
    print("Você foi aprovado.")
print("--------------")

nota4 = int(input("Informe um numero: "))
nota3 = int(input("Informe um numero: "))
nota2 = int(input("Informe um numero: "))
nota1 = int(input("Informe um numero: "))
media = (nota1+nota2+nota3+nota4)/4
print(f"a media das notas é {media}")
print("--------------")
