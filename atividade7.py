lista = []

while True:
    opcao = input("Digite o que você deseja adicionar na sua lista ou 'sair' para finalizar.")
    if opcao.lower() == 'sair':
        break
    lista.append(opcao)
    print("Aqui está sua lista de compras:")
    for i, opcao in enumerate(lista, start=1):
        print(f"{i}. {opcao}")
