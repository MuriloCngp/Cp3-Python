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
 
# Função para exibir os produtos e adicionar ao carrinho
def exibir_vinhos(vinhos):
    for i, (vinho, preco) in enumerate(vinhos.items(), start=1):
        print(f"{i}- {vinho} – R$ {preco:.2f}")
    print(f"{len(vinhos) + 1}- Voltar")
 
def adicionar_ao_carrinho(vinhos):
    while True:
        exibir_vinhos(vinhos)
        opcao = input("Selecione o número do vinho que deseja adicionar ao carrinho ou 'Voltar' para retornar: ")
 
        # Tratamento de erro mais robusto para a opção de voltar
        if opcao.lower() == "voltar":
            break
 
        if opcao.isnumeric():
            opcao = int(opcao)
            if 1 <= opcao <= len(vinhos):
                vinho_selecionado = list(vinhos.items())[opcao - 1]
                while True:  # Loop para garantir quantidade válida
                    try:
                        quantidade = int(input(f"Digite a quantidade de '{vinho_selecionado[0]}' que deseja: "))
                        if quantidade > 0:
                            break
                        else:
                            print("Quantidade inválida. Digite um número maior que zero.")
                    except ValueError:
                        print("Entrada inválida. Digite um número inteiro.")
                carrinho.append((vinho_selecionado[0], vinho_selecionado[1], quantidade))
                print(f"{quantidade}x '{vinho_selecionado[0]}' adicionado ao carrinho com sucesso!")
            elif opcao == len(vinhos) + 1:
                break
            else:
                print("Opção inválida, por favor tente novamente.")
        else:
            print("Opção inválida, por favor tente novamente.")
 
# Função para visualizar o carrinho
def visualizar_carrinho():
    print("-" * 30)
    print("Seu carrinho de compras:")
    if not carrinho:
        print("Seu carrinho está vazio!")
    else:
        total = 0
        for vinho, preco, quantidade in carrinho:
            print(f"{quantidade}x {vinho} - R$ {preco:.2f} = R$ {preco * quantidade:.2f}")
            total += preco * quantidade
        print("-" * 30)
        print(f"Total: R$ {total:.2f}")
        print("-" * 30)
 
 
# Função para calcular e exibir o desconto
def calcular_desconto():
    total = 0
    for _, preco, quantidade in carrinho:
        total += preco * quantidade
 
    quantidade_itens = len(carrinho)
    desconto = 0
 
    if quantidade_itens == 2:
        desconto = 0.05
    elif quantidade_itens >=4:
        desconto = 0.2
    elif quantidade_itens == 3:
        desconto = 0.1
 
    valor_desconto = total * desconto
    total_com_desconto = total - valor_desconto
 
    print(f"Desconto aplicado: R$ {valor_desconto:.2f} ({desconto * 100:.0f}%)")
    print(f"Total com desconto: R$ {total_com_desconto:.2f}")
 
# Função da mensagem inicial
def mensagem_inicial():
    print("-" * 50)
    print("Vinheria Agnello")
    print("Bem-vindo(a) ao nosso e-commerce!")
    print("-" * 50)
 
# Função da mensagem final
def mensagem_final():
    print("-" * 50)
    print("O seu pedido foi finalizado. 🥳")
    print("Agradecemos a confiança depositada em nossa loja!")
    print("Vinheria Agnello, agradeçe! 🍷🥂")
    print("-" * 50)
 
 
def informacoes_usario():
    # Obter informações do usuário
    nome_usuario = input("Digite seu nome completo: ")
    email = input("Digite o seu email: ")
    # Implementação de validações para CPF, data de nascimento, CEP, etc.
    # ...
    # (Você pode usar bibliotecas como 're' para expressões regulares)
    cpf = input("Digite o seu CPF: ")
    data_nascimento = input("Digite a sua data de nascimento (AAAA-MM-DD): ")
    cep = input("Digite o seu CEP: ")
    cidade = input("Digite sua cidade: ")
    estado = input("Digite o seu estado: ")
 
# Função para finalizar a compra
def finalizar_compra():
    if not carrinho:
        print("O carrinho está vazio. Não é possível finalizar a compra.")
        return
 
    print("-" * 30)
    print("Finalizando compra...")
    print("-" * 30)
    informacoes_usario()
 
    print("-" * 30)
    print("Escolha o metodo de pagamento")
    print("1 - Pix")
    print("2 - Boleto")
    print("3 - Débito")
    print("4 - Crédito")
    print("-" * 30)
 
    metodo_pagamento = int(input("Método de pagamento: "))
 
    match metodo_pagamento:
        case 1:
            print("Enviaremos o código do QR Code/Chave aleatória em seu dispositivo móvel")
        case 2:
            print("Verifique seu email para acessar o boleto")
        case 3:
            print("Insira a seguir os dados do seu cartão de débito")
            print("-" * 30)
            numero_car = int(input("Insira os números do seu cartão de Débito: "))
            cvv_car = int(input("Insira o número de segurança do seu cartão de Débito: "))
            data_car = int(input("Insira a data de validade do seu cartão de Débito"))

        case 4:
            print("Insira a seguir os dados do seu cartão de Crédito: ")
            
            numero_car = int(input("Insira os números do seu cartão de Crédito: "))
            cvv_car = int(input("Insira o número de segurança do seu cartão de Crédito: "))
            data_car = int(input("Insira a data de validade do seu cartão de Crédito: "))
        case _:
            print("Opção inválida, por favor tente novamente!")

 
    # Exibir resumo da compra1
    visualizar_carrinho()
    calcular_desconto()
 
    # Confirmar compra
    confirmacao = input("Confirmar compra? (S/N): ").strip().upper()
    if confirmacao == "S":
        mensagem_final()
        carrinho.clear()
    else:
        print("Compra cancelada.")
 
# Corpo principal do programa
mensagem_inicial()
 
while True:
    print("\nEscolha uma opção:")
    print("1- Ver Vinhos Tintos")
    print("2- Ver Vinhos Brancos")
    print("3- Ver Vinhos Rosés")
    print("4- Ver Carrinho")
    print("5- Finalizar Compra")
    print("6- Sair")
 
    opcao_vinhos = input("Selecione uma opção: ")
 
    # Tratamento de erro para opção inválida (não numérica)
    if not opcao_vinhos.isnumeric():
        print("Opção inválida, por favor tente novamente!")
        continue
 
    opcao_vinhos = int(opcao_vinhos)
 
    match opcao_vinhos:
        case 1:
            adicionar_ao_carrinho(vinhos_tintos)
        case 2:
            adicionar_ao_carrinho(vinhos_brancos)
        case 3:
            adicionar_ao_carrinho(vinhos_roses)
        case 4:
            visualizar_carrinho()
        case 5:
            finalizar_compra()
        case 6:
            print("Obrigado por visitar a Vinheria Agnelo!")
            break
        case _:
            print("Opção inválida, por favor tente novamente!")