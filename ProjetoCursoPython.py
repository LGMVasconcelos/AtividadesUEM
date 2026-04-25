def adicionarItem():
    print("\033[H\033[J", end="")
    print("Adicionar item:\n")
    item = int(input("Digite o nome do item que deseja adicionar: "))
    if item != "":
        carrinho.update({item})
        return
    else:
        print("\033[H\033[J", end="")
        print("Adicionar item:\n")
        item = int(input("O item não pode ser vazio, tente inserir um item válido: "))

def removerItem():
    print("\033[H\033[J", end="")
    print("Remover item:\n")
    remocao = int(input("Digite o nome do item que deseja remover: "))
opcoes = {"1 - Adicionar item", "2 - Remover item", "3 - Atualizar quantidade", "4 - Visualizar lista", "5 - Sair" }    
carrinho = {}
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


    