# Vamos implementar um menu interativo no terminal
# para um programa fictício. O menu deve ter as opções:
# - Cadastrar novo usuário
# - Ver usuários cadastrados
# - Sair

# Importa a biblioteca InquirerPy, que permite criar menus interativos no terminal.
from InquirerPy import inquirer


usuarios = []
# Inicializa uma lista vazia chamada 'usuarios', que será usada para armazenar os nomes cadastrados.

while True:
    # Inicia um loop infinito que será interrompido apenas quando o usuário escolher a opção "Sair".

    opcao = inquirer.select(
        message="Escolha uma opção",
        # Exibe uma mensagem pedindo ao usuário para selecionar uma das opções do menu.
        choices=[
            "Cadastrar novo usuário",
            # Primeira opção: Cadastrar um novo usuário.
            "Ver usuários cadastrados",
            # Segunda opção: Exibir a lista de usuários já cadastrados.
            "Sair",
            # Terceira opção: Sair do programa.
        ],
    ).execute()
    # Apresenta o menu interativo e armazena a opção selecionada na variável 'opcao'.

    if opcao == "Cadastrar novo usuário":
        # Verifica se o usuário escolheu a opção de cadastrar um novo usuário.
        nome = inquirer.text(
            message="Digite o nome do usuário:"
            # Exibe uma mensagem pedindo para o usuário digitar o nome do novo usuário.
        ).execute()
        # Recebe o nome digitado pelo usuário e armazena na variável 'nome'.
        usuarios.append(nome)
        # Adiciona o nome digitado à lista 'usuarios'.
        print(f'Usuário {nome} cadastrado com sucesso!')
        # Exibe uma mensagem informando que o usuário foi cadastrado com sucesso.

    elif opcao == "Ver usuários cadastrados":
        # Verifica se o usuário escolheu a opção de ver os usuários cadastrados.
        print('Usuários cadastrados:')
        # Exibe uma mensagem indicando que será mostrada a lista de usuários cadastrados.
        for i, usuario in enumerate(usuarios, 1):
            # Faz um loop pela lista 'usuarios', enumerando cada usuário com números a partir de 1.
            print(f'{i}. {usuario}')
            # Exibe o número e o nome de cada usuário na lista.

    elif opcao == "Sair":
        # Verifica se o usuário escolheu a opção de sair do programa.
        print("Saindo...")
        # Exibe uma mensagem informando que o programa está encerrando.
        break
        # Interrompe o loop e finaliza o programa.
