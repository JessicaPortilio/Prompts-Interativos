# 1. O que é o expand?
# O expand é um tipo de prompt interativo que:
# ✅ Permite ao usuário escolher uma opção pressionando apenas uma tecla.
# ✅ Exibe um menu com uma letra associada a cada opção.
# ✅ Ideal para menus rápidos e acessíveis sem necessidade de setas (↑ e ↓).

# 📌 Diferença entre expand e rawlist?

# No rawlist, o usuário digita um número.
# No expand, o usuário pressiona uma única letra associada à opção.

# 2. Como usar o expand?
# Aqui está um exemplo básico de um menu para confirmar uma ação:

# Importa a função prompt da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista chamada 'pergunta', que contém um dicionário com os detalhes da pergunta interativa.
pergunta = [
    {
        "type": "expand",  # Define o tipo da pergunta como "expand", que permite respostas curtas com atalhos de teclado.
        "name": "confirmacao",  # Nome da variável onde será armazenada a escolha do usuário.
        "message": "Deseja continuar?",  # Mensagem que será exibida no terminal para o usuário.
        "choices": [  # Lista de opções que o usuário pode escolher.
            {"key": "s", "name": "Sim", "value": "sim"},  # Opção 'Sim', pode ser escolhida pressionando 's'.
            {"key": "n", "name": "Não", "value": "nao"},  # Opção 'Não', pode ser escolhida pressionando 'n'.
            {"key": "m", "name": "Mais informações", "value": "info"},  # Opção 'Mais informações', pode ser escolhida pressionando 'm'.
        ],
    }
]

# Exibe a pergunta no terminal e armazena a resposta escolhida pelo usuário na variável 'resposta'.
resposta = prompt(pergunta)

# Exibe no terminal a opção que o usuário escolheu.
print(f"Você escolheu: {resposta['confirmacao']}")


# 3. Adicionando uma Opção Padrão (default)
# Podemos definir uma opção padrão, que será usada se o usuário apenas pressionar Enter:

# Importa a função prompt da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista chamada 'pergunta', que contém um dicionário com os detalhes da pergunta interativa.
pergunta = [
    {
        "type": "expand",  # Define o tipo da pergunta como "expand", permitindo atalhos de teclado para escolher opções.
        "name": "modo",  # Nome da variável que armazenará a resposta do usuário.
        "message": "Escolha o modo de operação:",  # Mensagem que será exibida ao usuário no terminal.
        "choices": [  # Lista de opções disponíveis para o usuário escolher.
            {"key": "a", "name": "Automático", "value": "auto"},  # Se o usuário pressionar 'a', escolherá "Automático".
            {"key": "m", "name": "Manual", "value": "manual"},  # Se pressionar 'm', escolherá "Manual".
            {"key": "c", "name": "Cancelar", "value": "cancelar"},  # Se pressionar 'c', escolherá "Cancelar".
        ],
        "default": "manual",  # Define "Manual" como a opção padrão se o usuário apenas pressionar "Enter".
    }
]

# Exibe a pergunta no terminal e armazena a resposta escolhida pelo usuário na variável 'resposta'.
resposta = prompt(pergunta)

# Exibe no terminal a opção que o usuário selecionou.
print(f"Modo selecionado: {resposta['modo']}")


# 4. Exemplo: Configuração de Preferências
# Vamos criar um menu para selecionar o tema do sistema:

# Importa a função prompt da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista chamada 'pergunta', que contém um dicionário com os detalhes da pergunta interativa.
pergunta = [
    {
        "type": "expand",  # Define o tipo da pergunta como "expand", permitindo atalhos de teclado para escolher opções.
        "name": "tema",  # Nome da variável que armazenará a resposta do usuário.
        "message": "Escolha um tema:",  # Pergunta exibida ao usuário no terminal.
        "choices": [  # Lista de opções disponíveis para o usuário escolher.
            {"key": "c", "name": "Claro", "value": "claro"},  # Pressionar 'c' seleciona o tema Claro.
            {"key": "e", "name": "Escuro", "value": "escuro"},  # Pressionar 'e' seleciona o tema Escuro.
            {"key": "s", "name": "Sistema", "value": "sistema"},  # Pressionar 's' seleciona o tema do Sistema.
        ],
        "default": "sistema",  # Se o usuário pressionar "Enter" sem escolher, o tema padrão será "Sistema".
    }
]

# Exibe a pergunta no terminal e armazena a resposta escolhida pelo usuário na variável 'resposta'.
resposta = prompt(pergunta)

# Exibe no terminal a opção que o usuário selecionou.
print(f"Tema escolhido: {resposta['tema']}")



# 5. Comparação expand vs select vs rawlist
# Característica	        expand	                                   select	                               rawlist
# Navegação	        Digitação de uma letra	                        Setas (↑ e ↓)	                    Digitação de um número
# Usabilidade	        Rápido e eficiente	                        Mais intuitivo	                    Mais rápido para usuários experientes
# Ideal para	        Menus curtos e rápidos	                    Listas longas e detalhadas	        Menus simples sem navegação por setas
# Padrão (default)	Sim, tecla pressionada ou Enter	Sim,            seta pré-selecionada	            Sim, número pré-selecionado

# 6. Exemplo Completo: Escolha de Ação em um Sistema

# Importa a função prompt da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define a função principal do programa.
def main():
    lista = []  # Cria uma lista vazia para armazenar os itens adicionados pelo usuário.

    # Inicia um loop infinito para manter o programa em execução até o usuário decidir sair.
    while True:
        # Define a pergunta para o usuário escolher uma ação.
        pergunta = [
            {
                "type": "expand",  # Tipo da pergunta, permitindo atalhos no teclado.
                "name": "acao",  # Nome da variável que armazenará a escolha do usuário.
                "message": "O que deseja fazer?",  # Mensagem exibida ao usuário.
                "choices": [  # Lista de opções disponíveis para o usuário.
                    {"key": "a", "name": "Adicionar novo item", "value": "adicionar"},  # Pressionar 'a' para adicionar um item.
                    {"key": "r", "name": "Remover item", "value": "remover"},  # Pressionar 'r' para remover um item.
                    {"key": "v", "name": "Visualizar lista", "value": "visualizar"},  # Pressionar 'v' para visualizar os itens.
                    {"key": "s", "name": "Sair", "value": "sair"},  # Pressionar 's' para sair do programa.
                ],
                "default": "visualizar",  # Se o usuário pressionar "Enter", a opção padrão será visualizar a lista.
            }
        ]

        # Exibe a pergunta e armazena a resposta na variável 'resposta'.
        resposta = prompt(pergunta)
        acao = resposta["acao"]  # Obtém a escolha do usuário.

        # Se o usuário escolher "adicionar":
        if acao == "adicionar":
            # Pergunta ao usuário o nome do item a ser adicionado.
            novo_item = prompt({"type": "input", "name": "item", "message": "Digite o nome do item:"})["item"]
            if novo_item:  # Verifica se o usuário digitou algo.
                lista.append(novo_item)  # Adiciona o item à lista.
                print(f"Item '{novo_item}' adicionado! ✅")  # Confirma a adição do item.
            else:
                print("Nenhum item adicionado. ❌")  # Se o usuário não digitou nada, exibe uma mensagem.

        # Se o usuário escolher "remover":
        elif acao == "remover":
            if lista:  # Verifica se a lista não está vazia.
                # Pergunta qual item o usuário deseja remover, listando os itens disponíveis.
                escolha = prompt({
                    "type": "list",
                    "name": "item_remover",
                    "message": "Selecione o item para remover:",
                    "choices": lista,  # Mostra os itens atuais na lista como opções.
                })
                lista.remove(escolha["item_remover"])  # Remove o item selecionado da lista.
                print(f"Item '{escolha['item_remover']}' removido! 🗑️")  # Confirma a remoção do item.
            else:
                print("A lista está vazia! ❌")  # Se não houver itens, exibe uma mensagem de erro.

        # Se o usuário escolher "visualizar":
        elif acao == "visualizar":
            if lista:  # Verifica se há itens na lista.
                print("\nLista de itens:")
                for idx, item in enumerate(lista, 1):  # Percorre a lista e exibe os itens numerados.
                    print(f"{idx}. {item}")
            else:
                print("A lista está vazia! ❌")  # Se não houver itens, exibe uma mensagem.

        # Se o usuário escolher "sair":
        elif acao == "sair":
            print("Saindo do sistema. ❌")  # Exibe uma mensagem de despedida.
            break  # Sai do loop e finaliza o programa.

        # Exibe uma linha separadora para melhorar a visualização no terminal.
        print("\n" + "-" * 30 + "\n")

# Verifica se o script está sendo executado diretamente (e não importado como módulo).
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa.
