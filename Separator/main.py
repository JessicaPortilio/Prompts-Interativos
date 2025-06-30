# 1. O que é um Separator?
# No InquirerPy, o Separator é um tipo especial de item utilizado para criar 
# uma linha separadora visual entre diferentes opções em listas ou menus interativos. 
# Ele ajuda a organizar melhor as escolhas, agrupando itens de maneira mais clara e legível.

# Função do Separator
# O Separator não é uma opção clicável, mas serve para dividir visualmente as opções, 
# tornando a interface do usuário mais organizada, especialmente quando você tem muitas opções em um select/list ou rawlist.

# 2. Como Usar o Separator?

# O Separator pode ser utilizado dentro de prompts como select/list, rawlist ou checkbox para adicionar separadores entre os itens. 
# Ele ajuda a agrupar opções de forma mais clara.

# Exemplo Básico de Separator em um select/list:

# Importa o módulo inquirer da biblioteca InquirerPy, que permite criar perguntas interativas no terminal
from InquirerPy import inquirer  

# Importa Separator da biblioteca InquirerPy, que permite adicionar separadores visuais entre as opções
from InquirerPy.separator import Separator  


# Cria uma variável chamada 'resposta' que armazenará a escolha do usuário
resposta = inquirer.select(  
    message='Qual linguagem de programação você prefere?',  # Define a mensagem da pergunta que será exibida ao usuário
    choices=[  # Lista de opções disponíveis para seleção
        "Python",  # Primeira opção disponível na lista
        "JavaScript",  # Segunda opção disponível na lista
        Separator(),  # Adiciona um separador visual para organizar melhor as opções
        "C++",  # Terceira opção disponível na lista
        "Java",  # Quarta opção disponível na lista
        Separator(),  # Adiciona outro separador visual para melhorar a organização das opções
        "Ruby",  # Quinta opção disponível na lista
        "Swift"  # Sexta opção disponível na lista
    ]
).execute()  # Executa o prompt, exibe as opções e espera a escolha do usuário

# Exibe no console a linguagem escolhida pelo usuário, formatando a string para incluir a resposta selecionada
print(f"Linguagem escolhida: {resposta}")  


# Importa a função prompt do InquirerPy para exibir perguntas interativas no terminal
from InquirerPy import prompt  
# Importa Separator para adicionar separadores visuais entre as opções da lista
from InquirerPy.separator import Separator  

# Define a lista de perguntas para o prompt
pergunta = [
    {
        "type": "list",  # Define o tipo de entrada como uma lista de opções
        "name": "linguagem",  # Nome da variável que armazenará a resposta
        "message": "Qual linguagem de programação você prefere?",  # Mensagem exibida ao usuário
        "choices": [  # Lista de opções disponíveis para seleção
            "Python",  # Primeira opção
            "JavaScript",  # Segunda opção
            Separator(),  # Adiciona um separador visual
            "C++",  # Terceira opção
            "Java",  # Quarta opção
            Separator(),  # Adiciona outro separador visual
            "Ruby",  # Quinta opção
            "Swift"  # Sexta opção
        ]
    }
]

# Exibe a pergunta ao usuário e armazena a resposta
resposta = prompt(pergunta)  

# Exibe a linguagem escolhida no console
print(f"Linguagem escolhida: {resposta['linguagem']}")  

# 3. Como Personalizar o Separator?
# Você pode personalizar o Separator para alterar seu estilo ou aparência. 
# Para isso, você pode passar um texto específico ou até mesmo usar um caractere especial para desenhar a linha separadora.

from InquirerPy import prompt
from InquirerPy.separator import Separator  


pergunta = [
    {
        "type": "list",
        "name": "linguagem",
        "message": "Qual linguagem de programação você prefere?",
        "choices": [
            "Python",
            "JavaScript",
            Separator("----"),
            "C++",
            "Java",
            Separator("****"),
            "Ruby",
            "Swift",
        ]
    }
]

resposta = prompt(pergunta)
# print(f"Linguagem escolhida: {resposta['linguagem']}")


# 4. Usando Separator em Outros Tipos de Prompts
# Embora o Separator seja comumente usado em select/list e rawlist, 
# você também pode aplicá-lo em outros tipos de listas e menus para melhorar a organização.

from InquirerPy import prompt
from InquirerPy.separator import Separator

pergunta = [
    {
        "type": "rawlist",
        "name": "linguagem",
        "message": "Qual linguagem de programação você prefere?",
        "choices": [
            "Python",
            "JavaScript",
            Separator(),
            "C++",
            "Java",
            Separator("====="),
            "Ruby",
            "Swift"
        ]
    }
]

resposta = prompt(pergunta)
print(f"Linguagem escolhida: {resposta['linguagem']}")
