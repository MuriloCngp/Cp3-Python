# Mensagem de inicio
print("Seja muito bem-vindo(a) à Vinheria Agnelo, pressione Enter para criar um cadastro e aproveitar nossa variedade de vinhos!")

# Criando e validando o Usuário           #Só criei esse pra ter uma base do programa, ai tu pode começar a parte da validação a partir daqui :)
nome_usuario = input("Insira seu nome: ")


# Lista de vinhos e preços por categoria
vinhos_tintos = {
    "Cabernet Sauvignon": 100,
    "Pinot Noir": 115,
    "Tinto Malbec": 80,
    "Tinto Merlot": 95
}
vinhos_brancos = {
    "Chardonnay": 80,
    "Sauvignon Blanc": 70,
    "Riesling": 90,
    "Pinot Grigio": 60
}
vinhos_roses = {
    "Cabernet Franc": 70,
    "Syrah": 80,
    "Grenache": 60
}

# Carrinho de compras
carrinho = []

# Função para exibir os produtos e adicionar ao carrinho --> E criando a função de ver o carrinho e o desconto total
def exibir_vinhos(vinhos):
    for i, (vinho, preco) in enumerate(vinhos.items(), start=1):
        print(f"{i}- {vinho} – R$ {preco};")
    print(f"{len(vinhos) + 1}- Voltar")

def adicionar_ao_carrinho(vinhos):
    while True:
        exibir_vinhos(vinhos)
        opcao = input("Selecione o número do vinho que deseja adicionar ao carrinho ou 'Voltar' para retornar: ")

        if opcao.isnumeric():
            opcao = int(opcao)
            if 1 <= opcao <= len(vinhos):
                vinho_selecionado = list(vinhos.items())[opcao - 1]
                carrinho.append(vinho_selecionado)
                print(f"{vinho_selecionado[0]} adicionado ao carrinho com sucesso!")
            elif opcao == len(vinhos) + 1:
                break
            else:
                print("Opção inválida, por favor tente novamente.")
        else:
            print("Opção inválida, por favor tente novamente.")

def ver_carrinho():
    if not carrinho:
        print("Seu carrinho está vazio!")
    else:
        total, total_com_desconto, percentual_desconto = calcular_total_com_desconto()
        print("Seu carrinho de compras:")
        for item, preco in carrinho:
            print(f"{item} - R$ {preco}")
        print(f"Total acumulado: R$ {total}")
        if percentual_desconto > 0:
            print(f"Desconto aplicado será de: {percentual_desconto}%")
            print(f"Total com desconto: R$ {total_com_desconto:.2f}")

def calcular_total_com_desconto():
    total = sum(preco for _, preco in carrinho)
    quantidade = len(carrinho)
    desconto = 0

    if quantidade == 2:
        desconto = 0.05
    elif quantidade == 3:
        desconto = 0.10
    elif quantidade >= 4:
        desconto = 0.20

    total_com_desconto = total * (1 - desconto)
    return total, total_com_desconto, desconto * 100

# Corpo do programa --> Escolhendo os produtos e os colocando no carrinho de compras
while True:
    print("Escolha uma opção:")
    print("1- Ver Vinhos Tintos")
    print("2- Ver Vinhos Brancos")
    print("3- Ver Vinhos Rosés")
    print("4- Ver Carrinho")

    opcao = input("Selecione uma opção: ")

    match opcao:
        case '1':
            adicionar_ao_carrinho(vinhos_tintos)
        case '2':
            adicionar_ao_carrinho(vinhos_brancos)
        case '3':
            adicionar_ao_carrinho(vinhos_roses)
        case '4':
            ver_carrinho()
        case _:
            print("Opção inválida, por favor tente novamente!")

        
        
        
        
        
