from math import sqrt as raiz
from calculosAula4 import dobro_mais_raiz
# Exercício 1:
print("Exercício 1:\n")

linguagens = ("Python", "C#", "Java", "PHP")

print(linguagens[1])
print(linguagens[-1])
print("\n")

# linguagens[0] = "C++"
# Não dá certo pois tuplas são imutáveis ☝️🤓
# ====================================================
# Exercício 2:
print("Exercício 2:\n")

estados = {
    "Paraná" : "Curitiba",
    "Bahia" : "Salvador",
    "São Paulo" : "São Paulo",
    "Santa Catarina" : "Florianópolis",
    "Acre" : "Rio Branco"
}

for estado, capital in estados.items():
    print(f"Estado: {estado}, Capital: {capital}\n")
# ====================================================
# Exercício 3:
print("Exercício 3:\n")
alunos = {
    "Isabela" : [8.0, 4.0, 0.1],
    "Pedro": [3.0, 8.0, 4.0],
    "Luiz" : [9.0, 8.0, 10.0],
    "Keity": [4.0, 3.0, 2.0]
}

for aluno, nota in alunos.items():
    if (sum(nota) / 3 >= 6.0):
        print(f"{aluno} foi aprovado(a) com a média {round(sum(nota) / 3, 1)}\n")
    else:
        print(f"{aluno} foi reprovado(a) com a média {round(sum(nota) / 3, 1)}\n")
# ====================================================
# Exercício 4:
print("Exercício 4:\n")
print(raiz(625))

print(f"O dobro de 10 somado à raiz de 10 é {dobro_mais_raiz(10)}")