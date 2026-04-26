'''
Eu fiz este projeto baseado em um anterior de mesmo propósito feito em C#, mas para sistema de notas naquele caso.
Como eu já havia conhecimento prévio, utilizei técnicas como try e except, que não foram passadas no curso,
mas que eu pesquisei sobre como implementar em python, baseado no que eu já tinha aprendido em C#.
Outra coisa nova que eu não sabia antes era a impressão de "\033[H\033[J", end="" que é uma técnica para
limpar a tela do terminal. Como o Python não tem um comando como o "Console.Clear()" do C#, eu pesquisei e
encontrei essa solução que funciona na maioria dos terminais. Ou seja, não fiz o uso de IAs generativas para fazer
o trabalho.
'''

import sys
carrinho = {}

def menu():
    opcoes = ("1 - Adicionar item", "2 - Remover item", "3 - Atualizar quantidade", "4 - Visualizar lista", "5 - Sair" )    
    
    for item in opcoes:
        print(item)
    opcao = int(input(f"Por favor, digite uma opção entre 1 e {len(opcoes)}: "))

    if opcao == 1:
        adicionarItem()
    elif opcao == 2:
        removerItem()
    elif opcao == 3:
        atualizarQuantidade()
    elif opcao == 4:
        visualizarLista()
    elif opcao == 5:
        sair()
    else:
        print("\033[H\033[J", end="")
        opcao = int(input(f"Por favor, digite uma opção entre 1 e {len(opcoes)}: "))
        
def adicionarItem():
    print("\033[H\033[J", end="")
    print("Adicionar item:\n")
    item = str(input("Digite o nome do item que deseja adicionar: "))
    
    while True:
        try:
            preco = float(input("Digite o preço do item: "))
            if preco < 0:
                print("O preço não pode ser negativo!")
                continue
            break
        except ValueError:
            print("Erro! Digite um valor numérico válido para o preço.")
    
    while True:
        try:
            quantidade = int(input("Digite a quantidade em estoque: "))
            if quantidade < 0:
                print("A quantidade não pode ser negativa!")
                continue
            break
        except ValueError:
            print("Erro! Digite um valor inteiro válido para a quantidade.")
    
    if item != "":
        carrinho[item] = {
            "preco": preco,
            "quantidade": quantidade,
            "valor_total": preco * quantidade
        }
        print("\033[H\033[J", end="")
        menu()
    else:
        print("O item não pode ser vazio!")
        adicionarItem()

def removerItem():
    print("\033[H\033[J", end="")
    print("Remover item:\n")
    if not carrinho:
        input("Carrinho vazio. Pressione Enter para voltar ao menu principal...")
        print("\033[H\033[J", end="")
        menu()
        return

    for indice, item in enumerate(carrinho):
        print(f"{indice} - {item}")
    
    while True:
        try:
            remocao = int(input(f"Digite o número correspondente ao item que deseja remover, ou {len(carrinho)} para limpar toda a lista: "))
            if 0 <= remocao < len(carrinho):
                break
            elif remocao == len(carrinho):
                carrinho.clear()
                print("\033[H\033[J", end="")
                print("Todos os elementos do carrinho foram limpos.\n")
                menu()
                return
            else:
                print(f"Opção inválida, digite um número entre 0 e {len(carrinho) - 1}")
        except ValueError:
            print("Erro! Digite um valor inteiro válido.")

    chave_item = list(carrinho.keys())[remocao]
    carrinho.pop(chave_item)
    print("Item removido com sucesso!")
    print("\033[H\033[J", end="")
    menu()
    return

def atualizarQuantidade():
    print("\033[H\033[J", end="")
    print("Atualizar quantidade do item:\n")
    if not carrinho:
        input("Carrinho vazio. Pressione Enter para voltar ao menu principal...")
        print("\033[H\033[J", end="")
        menu()
        return

    for indice, item in enumerate(carrinho):
        print(f"{indice} - {item}")
    
    while True:
        try:
            atualizacao = int(input("Digite o número do item que deseja atualizar: "))
            if 0 <= atualizacao < len(carrinho):
                break
            else:
                print(f"Opção inválida, digite um número entre 0 e {len(carrinho) - 1}")
        except ValueError:
            print("Erro! Digite um valor inteiro válido.")

    chave_item = list(carrinho.keys())[atualizacao]
    print(f"Atualizando: {chave_item}")
    
    while True:
        try:
            nova_quantidade = int(input(f"Digite a nova quantidade para {chave_item}: "))
            if nova_quantidade < 0:
                print("\033[H\033[J", end="")
                carrinho.pop(chave_item)
                print("O item foi removido do carrinho, pois a quantidade inserida é negativa.\n")
                menu()
            break
        except ValueError:
            print("Erro! Digite um valor inteiro válido.")

    carrinho[chave_item]["quantidade"] = nova_quantidade
    carrinho[chave_item]["valor_total"] = carrinho[chave_item]["preco"] * nova_quantidade
    print("\033[H\033[J", end="")
    menu()
    return

def visualizarLista():
    print("\033[H\033[J", end="")
    print("Lista de compras:\n")
    for item, detalhes in carrinho.items():
        print(f"{item} - Preço: R${detalhes['preco']:.2f}, Quantidade: {detalhes['quantidade']}, Valor Total: R${detalhes['valor_total']:.2f}\n")
    print(f"Quantidade de itens no carrinho: {len(carrinho)}\n")
    if not carrinho:
        print("O carrinho está vazio.")
    retornar = input("Pressione Enter para voltar ao menu principal...")
    if retornar == "":
        print("\033[H\033[J", end="")
        menu()
        return
    else:
        visualizarLista()

def sair():
    print("\033[H\033[J", end="")
    print("Saindo do programa. Obrigado por usar o carrinho de compras!")
    sys.exit(0)


menu()