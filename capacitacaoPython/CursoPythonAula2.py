#Exercício 1:
lista_compras:list[str] = []
lista_compras.append("arroz")
lista_compras.append("feijão")
lista_compras.append("leite")
lista_compras.insert(0, "pão")
print(lista_compras)
lista_compras.remove("feijão")
lista_compras.pop()
print(lista_compras)
# ====================================================
# Exercício 2:
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))
l = [n1, n2, n3]
soma = l[0] + l[1] + l[2]
print(f"A soma total dos valores inseridos é: {soma}")
# ====================================================
# Exercício 3:
frutas = ["maçã", "banana", "laranja", "uva", "manga"]

for fruta in frutas:
    print(fruta)
# ====================================================
# Exercício 4:
listaEx4 = [2, 4, 6, 8, 10]
maior_numero = listaEx4[0]
for numero in range(0, len(listaEx4)):
    if numero > maior_numero:
        maior_numero = numero
print(f"o maior número da lista é: {maior_numero}")
# ====================================================
# Exercício 5:
listaEx5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for numero in listaEx5:
    if (numero % 2 == 0):
        print(numero)
# ====================================================
# Exercício 6:
listaEx6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
listapares = []
listaimpares = []
for numero in listaEx6:
    if (numero % 2 == 0):
        listapares.append(numero)
    else:
        listaimpares.append(numero)
print(listapares)
print(listaimpares)
