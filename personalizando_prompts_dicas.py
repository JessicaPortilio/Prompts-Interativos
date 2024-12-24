# Importa a biblioteca InquirerPy, usada para criar perguntas interativas no terminal.
from InquirerPy import inquirer  

# Prompt com dicas
escolha = inquirer.select(  # Cria um menu de seleção no terminal onde o usuário escolhe uma opção de uma lista.
    message='Escolha uma fruta:',  # Mensagem que será exibida para o usuário, indicando o que ele deve fazer.
    choices=[  # Lista de opções que o usuário pode escolher.
        {"name": "Uva 🍇", "value": "uva 🍇"},  # Cada opção tem um "name" (o que é exibido para o usuário) e um "value" (o valor real associado à escolha).
        {"name": "Maçã 🍎", "value": "maçã 🍎"},
        {"name": "Banana 🍌", "value": "banana 🍌"},
        {"name": "Laranja 🍊", "value": "laranja 🍊"},
    ],
    default="banana",  # Define a opção padrão que será destacada se o usuário não fizer nenhuma seleção.
).execute()  # Executa o prompt e retorna a opção selecionada pelo usuário.

print(f'Você escolheu: {escolha}')  
# Exibe no terminal a escolha feita pelo usuário. Por exemplo, se o usuário escolher "Maçã 🍎", será exibido: "Você escolheu: maçã 🍎".
