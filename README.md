🍷 Vinheria Agnello – Sistema de Compras em Python
📝 Descrição

O Vinheria Agnello é um sistema simples de e-commerce em Python que simula a experiência de compra de vinhos diretamente pelo terminal.
O usuário pode navegar entre categorias de vinhos (tintos, brancos e rosés), adicionar produtos ao carrinho, visualizar o total da compra, aplicar descontos automáticos e finalizar o pedido com diferentes métodos de pagamento.

Este projeto é ideal para fins educacionais, demonstrando o uso de estruturas de dados (dicionários, listas), funções, loops, tratamento de erros e controle de fluxo em Python.

🚀 Funcionalidades

✅ Listagem de vinhos por categoria

🛒 Adição de produtos ao carrinho com quantidades personalizadas

💰 Cálculo automático de descontos progressivos:

2 itens → 5% de desconto

3 itens → 10% de desconto

4 ou mais itens → 20% de desconto

👀 Visualização do carrinho e valor total

🧾 Finalização da compra com coleta de dados do cliente

💳 Escolha do método de pagamento (Pix, Boleto, Débito ou Crédito)

🎉 Mensagens personalizadas de boas-vindas e agradecimento

🧩 Estrutura do Código
vinheria_agnello.py
│
├── vinhos_tintos (dict)
├── vinhos_brancos (dict)
├── vinhos_roses (dict)
├── carrinho (list)
│
├── exibir_vinhos()              # Mostra os produtos disponíveis
├── adicionar_ao_carrinho()      # Adiciona produtos ao carrinho
├── visualizar_carrinho()        # Mostra o conteúdo do carrinho
├── calcular_desconto()          # Calcula o desconto aplicável
├── informacoes_usario()         # Coleta dados pessoais
├── finalizar_compra()           # Realiza o processo de compra
├── mensagem_inicial()           # Mensagem de boas-vindas
├── mensagem_final()             # Mensagem de encerramento
└── Loop principal de navegação  # Menu interativo

⚙️ Como Executar
🧠 Pré-requisitos

Python 3.8+ instalado no computador

Nenhuma biblioteca externa é necessária (tudo é padrão do Python)

▶️ Passos para execução

Baixe ou clone este repositório:

git clone https://github.com/seuusuario/vinheria-agnello.git


Acesse a pasta do projeto:

cd vinheria-agnello


Execute o script principal:

python vinheria_agnello.py

💡 Exemplo de Uso
--------------------------------------------------
Vinheria Agnello
Bem-vindo(a) ao nosso e-commerce!
--------------------------------------------------

Escolha uma opção:
1- Ver Vinhos Tintos
2- Ver Vinhos Brancos
3- Ver Vinhos Rosés
4- Ver Carrinho
5- Finalizar Compra
6- Sair


O usuário pode:

Escolher a categoria de vinhos

Adicionar itens ao carrinho

Visualizar o total e o desconto

Finalizar a compra com o método de pagamento de sua preferência

🧮 Exemplo de Desconto
Quantidade de Itens	Desconto Aplicado
2 itens	5%
3 itens	10%
4 ou mais itens	20%
👨‍💻 Autor

Murilo Cordeiro
Desenvolvido como exercício prático de lógica de programação e manipulação de dados em Python.

🏷️ Licença

Este projeto é livre para uso educacional e pessoal.
Sinta-se à vontade para adaptar, modificar e expandir. 🍷
