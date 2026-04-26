carrinho = {}

def adicionarItem():
    print("\033[H\033[J", end="")
    print("Adicionar item:\n")
    item = str(input("Digite o nome do item que deseja adicionar: "))
    preco = float(input("Digite o preço do item que deseja adicionar:"))
    quantidade = int(input("Digite a quantidade em estoque do item que deseja adicionar:"))
    valor_total = preco * quantidade
    if item != "":
        carrinho[item] = {
        "preco": preco,
        "quantidade": quantidade,
        "valor_total": preco * quantidade
        }
        return
    else:
        print("\033[H\033[J", end="")
        print("Adicionar item:\n")
        item = str(input("O item não pode ser vazio, tente inserir um item válido: "))

def removerItem():
    print("\033[H\033[J", end="")
    print("Remover item:\n")
    if not carrinho:
        input("Carrinho vazio. Pressione Enter para voltar ao menu principal...")
        return

    for indice, item in enumerate(carrinho):
        print(f"{indice} - {item}")
    remocao = int(input("Digite o número correspondente ao item que deseja remover: "))
    while remocao < 0 or remocao >= len(carrinho):
        print("\033[H\033[J", end="")
        print("Remover item:\n")
        remocao = int(input(f"Opção inválida, por favor digite um número entre 0 e {len(carrinho) - 1}: "))

    chave_item = list(carrinho.keys())[remocao]
    carrinho.pop(chave_item)
    return

def atualizarQuantidade():
    print("\033[H\033[J", end="")
    print("Atualizar quantidade do item:\n")
    if not carrinho:
        input("Carrinho vazio. Pressione Enter para voltar ao menu principal...")
        return

    for indice, item in enumerate(carrinho):
        print(f"{indice} - {item}")
    atualizacao = int(input("Digite o número correspondente ao item que deseja atualizar a quantidade: "))
    while atualizacao < 0 or atualizacao >= len(carrinho):
        atualizacao = int(input(f"Opção inválida, por favor digite um número entre 0 e {len(carrinho) - 1}: "))

    chave_item = list(carrinho.keys())[atualizacao]
    print(f"Atualizando: {chave_item}")
    nova_quantidade = float(input(f"Digite a nova quantidade que você quer para {chave_item}: "))
    while nova_quantidade < 0:
        print("\033[H\033[J", end="")
        print("Atualizar quantidade do item:\n")
        nova_quantidade = float(input(f"A quantidade não pode ser negativa, tente inserir uma quantidade válida para {chave_item}: "))

    carrinho[chave_item]["quantidade"] = nova_quantidade
    carrinho[chave_item]["valor_total"] = carrinho[chave_item]["preco"] * nova_quantidade
    return
    main()

def visualizarLista():
    print("\033[H\033[J", end="")
    print("Lista de compras:\n")
    for item, detalhes in carrinho.items():
        print(f"{item} - Preço: R${detalhes['preco']:.2f}, Quantidade: {detalhes['quantidade']}, Valor Total: R${detalhes['valor_total']:.2f}\n")
    retornar = input("Pressione Enter para voltar ao menu principal...")
    if retornar == "":
        return
    main()

def sair():
    print("\033[H\033[J", end="")
    print("Saindo do programa. Obrigado por usar o carrinho de compras!")

def main():
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


    