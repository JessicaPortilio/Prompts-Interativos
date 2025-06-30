from InquirerPy import prompt 

# 1. O que é o rawlist?
# O rawlist é um prompt que permite ao usuário selecionar uma opção digitando o número correspondente.

# Ele é útil para:
# ✅ Criar menus rápidos sem necessidade de navegação pelas setas.
# ✅ Interfaces minimalistas onde o usuário já sabe a opção desejada.
# ✅ Permitir seleção mais eficiente em terminais sem suporte a interfaces interativas.

# 2. Como usar o rawlist?
# Aqui está um exemplo básico onde o usuário escolhe um sistema operacional:

# Importa a função prompt da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista chamada 'pergunta', que contém um dicionário com os detalhes da pergunta interativa.
pergunta = [
    {
        "type": "rawlist",  # Define o tipo de pergunta como uma lista de opções para escolher.
        "name": "sistema",  # Nome da variável que armazenará a resposta do usuário.
        "message": "Qual sistema operacional você usa?",  # Pergunta exibida ao usuário.
        "choices": ["Windows", "Linux", "MacOS"],  # Lista de opções disponíveis para escolha.
    }
]

# Exibe a pergunta no terminal e armazena a resposta escolhida pelo usuário na variável 'resposta'.
resposta = prompt(pergunta)

# Exibe no terminal qual sistema operacional o usuário escolheu, acessando a resposta armazenada.
print(f"Sistema escolhido: {resposta['sistema']}")


# 3. Adicionando um Valor Padrão (default)
# Podemos definir uma opção pré-selecionada para facilitar a escolha do usuário:

# Importa a função prompt da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista chamada 'pergunta', que contém um dicionário com os detalhes da pergunta interativa.
pergunta = [
    {
        "type": "rawlist",  # Define o tipo de pergunta como uma lista de opções para escolher.
        "name": "navegador",  # Nome da variável que armazenará a resposta do usuário.
        "message": "Escolha seu navegador preferido:",  # Pergunta que será exibida ao usuário no terminal.
        "choices": ["Google Chrome", "Firefox", "Edge", "Safari"],  # Lista de navegadores disponíveis para escolha.
        "default": 2,  # Define a opção padrão como a terceira da lista (posição 2, pois a contagem começa do zero).
    }
]

# Exibe a pergunta no terminal e armazena a resposta escolhida pelo usuário na variável 'resposta'.
resposta = prompt(pergunta)

# Exibe no terminal qual navegador foi escolhido, acessando a resposta armazenada.
print(f"Navegador escolhido: {resposta['navegador']}")



# 4. Exemplo: Menu de Configurações
# Vamos criar um menu onde o usuário pode configurar sua experiência de uso:

# Importa a função prompt da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista chamada 'pergunta', que contém um dicionário com os detalhes da pergunta interativa.
pergunta = [
    {
        "type": "rawlist",  # Define o tipo de pergunta como uma lista de opções para o usuário escolher.
        "name": "config",  # Nome da variável que armazenará a opção selecionada pelo usuário.
        "message": "O que deseja configurar?",  # Pergunta exibida ao usuário no terminal.
        "choices": ["Alterar idioma", "Ajustar brilho", "Mudar senha", "Sair"],  # Opções disponíveis para escolha.
    }
]

# Exibe a pergunta no terminal e armazena a resposta escolhida pelo usuário na variável 'resposta'.
resposta = prompt(pergunta)

# Verifica qual opção o usuário escolheu e executa a ação correspondente.

if resposta["config"] == "Alterar idioma":  # Se o usuário escolheu "Alterar idioma"
    print("Redirecionando para configurações de idioma... 🌍")  # Exibe a mensagem de redirecionamento.
    
elif resposta["config"] == "Ajustar brilho":  # Se o usuário escolheu "Ajustar brilho"
    print("Ajustando brilho da tela... 💡")  # Exibe a mensagem indicando o ajuste de brilho.

elif resposta["config"] == "Mudar senha":  # Se o usuário escolheu "Mudar senha"
    print("Redirecionando para alteração de senha... 🔑")  # Exibe a mensagem de alteração de senha.

else:  # Se o usuário escolheu "Sair" (ou qualquer outra opção inesperada)
    print("Saindo das configurações. ❌")  # Exibe a mensagem informando que está saindo.


# 5. Comparação select vs rawlist
# Característica	            select	                rawlist
# Navegação	            Setas (↑ e ↓)	        Digitação de um número
# Usabilidade	            Mais intuitivo	        Mais rápido para usuários experientes
# Recomendado para	    Menus interativos	    Interfaces minimalistas
# Suporte a emoji?	    Sim (📷 Instagram)	    Não (apenas texto)

# Quando usar rawlist?
# 🔹 Quando o usuário já está acostumado com os números das opções.
# 🔹 Quando queremos menus rápidos e sem navegação por setas.
# 🔹 Para interfaces em terminais simples (sem suporte interativo).

# Quando usar select?
# 🔹 Quando o usuário precisa ver todas as opções antes de decidir.
# 🔹 Para interfaces mais amigáveis e visuais.

# 6. Exemplo Completo: Escolha de Pacotes de Software

# Importa a biblioteca 'time' para usar funções relacionadas ao tempo, como pausas (sleep).
import time

# Importa a função 'prompt' da biblioteca 'prompt_toolkit' para criar entradas interativas.
from prompt_toolkit import prompt

# Importa a função 'radiolist_dialog' para criar caixas de diálogo com opções de seleção.
from prompt_toolkit.shortcuts import radiolist_dialog

# Define uma função chamada 'simular_instalacao' que simula o processo de instalação de um software.
def simular_instalacao(software):
    # Exibe uma mensagem informando que a instalação do software selecionado está começando.
    print(f"Iniciando instalação do {software}... 🔄")
    
    # Cria um loop que simula o progresso da instalação, de 20% em 20%.
    for i in range(1, 6):
        # Pausa a execução do programa por 1 segundo para simular o tempo de instalação.
        time.sleep(1)
        
        # Exibe o progresso da instalação em porcentagem.
        print(f"Progresso: {i * 20}%")
    
    # Exibe uma mensagem informando que a instalação foi concluída com sucesso.
    print(f"{software} instalado com sucesso! ✅")

# Define a função principal do programa, chamada 'main'.
def main():
    # Cria um loop infinito para permitir que o usuário faça várias seleções.
    while True:
        # Cria uma lista de opções que serão exibidas ao usuário.
        # Cada opção é uma tupla contendo um valor interno e um texto exibido.
        opcoes = [
            ("Python", "Python"),        # Opção para instalar Python.
            ("Node.js", "Node.js"),      # Opção para instalar Node.js.
            ("Docker", "Docker"),        # Opção para instalar Docker.
            ("Git", "Git"),              # Opção para instalar Git.
            ("Cancelar", "Cancelar instalação"),  # Opção para cancelar a instalação.
        ]

        # Cria uma caixa de diálogo interativa com as opções definidas acima.
        resposta = radiolist_dialog(
            title="Instalador de Software",  # Título da caixa de diálogo.
            text="Qual pacote deseja instalar?",  # Texto exibido na caixa de diálogo.
            values=opcoes,  # Lista de opções que o usuário pode escolher.
        ).run()  # Executa a caixa de diálogo e aguarda a resposta do usuário.

        # Verifica se o usuário cancelou a instalação ou fechou a caixa de diálogo.
        if resposta is None or resposta == "Cancelar":
            # Exibe uma mensagem informando que a instalação foi cancelada.
            print("Instalação cancelada. ❌")
            break  # Sai do loop e encerra o programa.
        else:
            # Se o usuário selecionou um software, chama a função para simular a instalação.
            simular_instalacao(resposta)

        # Cria uma nova caixa de diálogo para perguntar se o usuário deseja continuar.
        continuar = radiolist_dialog(
            title="Continuar?",  # Título da caixa de diálogo.
            text="Deseja instalar outro pacote?",  # Texto exibido na caixa de diálogo.
            values=[
                ("sim", "Sim"),  # Opção para continuar instalando.
                ("nao", "Não"),  # Opção para encerrar o programa.
            ],
        ).run()  # Executa a caixa de diálogo e aguarda a resposta do usuário.

        # Verifica se o usuário escolheu não continuar.
        if continuar != "sim":
            # Exibe uma mensagem de agradecimento e encerra o programa.
            print("Obrigado por usar o instalador! 👋")
            break  # Sai do loop e encerra o programa.

# Verifica se o script está sendo executado diretamente (não importado como módulo).
if __name__ == "__main__":
    # Chama a função principal 'main' para iniciar o programa.
    main()