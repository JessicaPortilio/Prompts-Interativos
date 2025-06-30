# 1. O que é o prompt list?
# O list permite que o usuário escolha uma opção de uma lista usando as teclas de seta (↑ e ↓).

# 2. Como usar o list?
# Aqui está um exemplo simples onde o usuário escolhe um idioma:

# Importa a função 'prompt' da biblioteca InquirerPy, que é usada para criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista contendo um dicionário com os detalhes da pergunta.
pergunta = [
    {
        # Define o tipo da pergunta como 'list', que permite ao usuário escolher uma opção de uma lista.
        "type": "list",  
        
        # Define um nome para armazenar a resposta escolhida. Esse nome será usado ao recuperar a resposta.
        "name": "idioma",  
        
        # Define a mensagem que será exibida para o usuário antes de mostrar as opções.
        "message": "Escolha um idioma:",  
        
        # Lista de opções que o usuário pode selecionar.
        "choices": ["Português", "Inglês", "Espanhol"],  
    }
]

# Exibe a pergunta ao usuário e armazena a resposta escolhida na variável 'resposta'.
resposta = prompt(pergunta)

# Exibe no terminal qual idioma foi selecionado pelo usuário.
print(f"Idioma selecionado: {resposta['idioma']}")

# 3. Adicionando um Valor Padrão (default)
# Podemos definir uma opção pré-selecionada:

# Importa a função 'prompt' da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista contendo um dicionário com os detalhes da pergunta.
pergunta = [
    {
        # Define o tipo da pergunta como 'list', que exibe uma lista de opções para o usuário selecionar.
        "type": "list",  
        
        # Define um nome para armazenar a resposta escolhida. Esse nome será usado para acessar a resposta depois.
        "name": "tema",  
        
        # Define a mensagem que será exibida ao usuário antes de mostrar as opções disponíveis.
        "message": "Escolha um tema:",  
        
        # Lista de opções disponíveis para o usuário escolher.
        "choices": ["Claro", "Escuro", "Automático"],  
        
        # Define a opção padrão que será selecionada caso o usuário apenas pressione "Enter" sem escolher outra opção.
        "default": "Escuro",  
    }
]

# Exibe a pergunta ao usuário e armazena a resposta escolhida na variável 'resposta'.
resposta = prompt(pergunta)

# Exibe no terminal qual tema foi escolhido pelo usuário.
print(f"Tema escolhido: {resposta['tema']}")

# 4. Exibir Diferentes Mensagens Baseadas na Resposta
# Podemos exibir mensagens personalizadas dependendo da escolha do usuário:

# Importa a função 'prompt' da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista contendo um dicionário com os detalhes da pergunta.
pergunta = [
    {
        # Define o tipo da pergunta como 'list', que exibe uma lista de opções para o usuário escolher.
        "type": "list",  
        
        # Define um nome para armazenar a resposta escolhida. Esse nome será usado para acessar a resposta depois.
        "name": "plano",  
        
        # Define a mensagem que será exibida ao usuário antes de mostrar as opções disponíveis.
        "message": "Escolha seu plano de assinatura:",  
        
        # Lista de opções de planos disponíveis para o usuário selecionar.
        "choices": ["Básico", "Premium", "Empresarial"],  
    }
]

# Exibe a pergunta ao usuário e armazena a resposta escolhida na variável 'resposta'.
resposta = prompt(pergunta)

# Verifica qual plano o usuário escolheu e exibe a mensagem correspondente.
if resposta["plano"] == "Básico":  # Se o usuário escolheu o plano "Básico"
    print("Plano Básico: Acesso limitado. 📉")  # Exibe uma mensagem indicando acesso limitado.
elif resposta["plano"] == "Premium":  # Se o usuário escolheu o plano "Premium"
    print("Plano Premium: Acesso completo! 🚀")  # Exibe uma mensagem indicando acesso completo.
else:  # Se o usuário escolheu o plano "Empresarial"
    print("Plano Empresarial: Solução personalizada para empresas. 🏢")  # Exibe uma mensagem indicando uma solução personalizada.

# Dependendo da escolha, uma mensagem diferente é exibida.
# Isso é útil para mostrar detalhes sobre cada opção antes de continuar.

# 5. Criando uma Lista de Opções com Tuplas
# Podemos usar discionário para armazenar um valor interno diferente do exibido:

# Importa a função 'prompt' da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista contendo um dicionário com os detalhes da pergunta.
pergunta = [
    {
        # Define o tipo da pergunta como 'list', que exibe uma lista de opções para o usuário escolher.
        "type": "list",  
        
        # Define um nome para armazenar a resposta escolhida. Esse nome será usado para acessar a resposta depois.
        "name": "moeda",  
        
        # Define a mensagem que será exibida ao usuário antes de mostrar as opções disponíveis.
        "message": "Escolha sua moeda:",  
        
        # Lista de opções de moedas disponíveis para o usuário selecionar.
        # Cada moeda tem um 'name' (o que será exibido ao usuário) e um 'value' (o que será armazenado na resposta).
        "choices": [
            {"name": "Real Brasileiro", "value": "BRL"},  # Opção para escolher o Real Brasileiro, armazenado como "BRL".
            {"name": "Dólar Americano", "value": "USD"},  # Opção para escolher o Dólar Americano, armazenado como "USD".
            {"name": "Euro", "value": "EUR"},  # Opção para escolher o Euro, armazenado como "EUR".
        ],
    }
]

# Exibe a pergunta ao usuário e armazena a resposta escolhida na variável 'resposta'.
resposta = prompt(pergunta)

# Exibe no terminal a moeda escolhida pelo usuário.
# O valor armazenado na resposta será o código da moeda (por exemplo, "BRL", "USD" ou "EUR").
print(f"Moeda escolhida: {resposta['moeda']}")


# 6. Criando um Menu com Ícones Personalizados
# Podemos adicionar ícones para cada opção:

# Importa a função 'prompt' da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista contendo um dicionário com os detalhes da pergunta.
pergunta = [
    {
        # Define o tipo da pergunta como 'list', que exibe uma lista de opções para o usuário escolher.
        "type": "list",  
        
        # Define um nome para armazenar a resposta escolhida. Esse nome será usado para acessar a resposta depois.
        "name": "rede_social",  
        
        # Define a mensagem que será exibida ao usuário antes de mostrar as opções disponíveis.
        "message": "Escolha uma rede social:",  
        
        # Lista de opções de redes sociais disponíveis para o usuário selecionar.
        # Cada opção tem um 'name' (o que será exibido ao usuário) e um 'value' (o que será armazenado na resposta).
        "choices": [
            {"name": "📘 Facebook", "value": "facebook"},  # Opção para Facebook, armazenada como "facebook".
            {"name": "📸 Instagram", "value": "instagram"},  # Opção para Instagram, armazenada como "instagram".
            {"name": "🐦 Twitter", "value": "twitter"},  # Opção para Twitter, armazenada como "twitter".
            {"name": "🎥 YouTube", "value": "youtube"},  # Opção para YouTube, armazenada como "youtube".
        ],
    }
]

# Exibe a pergunta ao usuário e armazena a resposta escolhida na variável 'resposta'.
resposta = prompt(pergunta)

# Exibe no terminal a rede social escolhida pelo usuário.
# O valor armazenado na resposta será o identificador da rede social escolhida (por exemplo, "facebook", "instagram").
print(f"Rede social escolhida: {resposta['rede_social']}")


# 7. Criando uma Lista com Opção "Cancelar"
# Podemos adicionar uma opção especial para permitir que o usuário saia do menu sem escolher nada.

# Importa a função 'prompt' da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista contendo um dicionário com os detalhes da pergunta.
pergunta = [
    {
        # Define o tipo da pergunta como 'list', que exibe uma lista de opções para o usuário escolher.
        "type": "list",  
        
        # Define um nome para armazenar a resposta escolhida. Esse nome será usado para acessar a resposta depois.
        "name": "acao",  
        
        # Define a mensagem que será exibida ao usuário antes de mostrar as opções disponíveis.
        "message": "O que deseja fazer?",  
        
        # Lista de opções disponíveis para o usuário escolher.
        "choices": ["Iniciar", "Configurações", "Sair"],  
    }
]

# Exibe a pergunta ao usuário e armazena a resposta escolhida na variável 'resposta'.
resposta = prompt(pergunta)

# Verifica se a opção escolhida pelo usuário foi "Sair".
if resposta["acao"] == "Sair":
    # Se o usuário escolheu "Sair", exibe uma mensagem de despedida.
    print("Saindo... 👋")
else:
    # Se o usuário escolheu qualquer outra opção, exibe a opção escolhida.
    print(f"Você escolheu: {resposta['acao']}")

# 8. Exemplo Completo: Menu de Configurações
# A ideia é criar um sistema de configurações que permita ao usuário escolher entre várias opções e executar ações específicas 
# para cada uma delas. Além disso, vamos adicionar:

# Validação de entrada: Garantir que o usuário escolha uma opção válida.

# Ações personalizadas: Adicionar funcionalidades reais para cada configuração.

# Loop de repetição: Permitir que o usuário faça várias configurações sem sair do programa.

# Mensagens amigáveis: Usar emojis e mensagens claras para melhorar a experiência do usuário.


# Importa a função 'prompt' da biblioteca 'InquirerPy', que é usada para criar perguntas interativas no terminal.
from InquirerPy import prompt

# Função para alterar a resolução.
def alterar_resolucao():
    # Exibe as opções de resolução disponíveis.
    print("\nOpções de resolução disponíveis:")
    print("1. 1920x1080 (Full HD)")
    print("2. 1280x720 (HD)")
    print("3. 800x600 (SVGA)")
    # Pede ao usuário para escolher uma resolução.
    escolha = input("Escolha uma resolução (1, 2 ou 3): ")
    # Verifica a escolha do usuário e exibe a mensagem correspondente.
    if escolha == "1":
        print("Resolução alterada para 1920x1080 (Full HD). 🖥️")
    elif escolha == "2":
        print("Resolução alterada para 1280x720 (HD). 🖥️")
    elif escolha == "3":
        print("Resolução alterada para 800x600 (SVGA). 🖥️")
    else:
        # Se a escolha for inválida, exibe uma mensagem de erro.
        print("Opção inválida. Nenhuma alteração foi feita. ❌")

# Função para alterar o tema.
def alterar_tema():
    # Exibe as opções de tema disponíveis.
    print("\nTemas disponíveis:")
    print("1. Claro ☀️")
    print("2. Escuro 🌙")
    # Pede ao usuário para escolher um tema.
    escolha = input("Escolha um tema (1 ou 2): ")
    # Verifica a escolha do usuário e exibe a mensagem correspondente.
    if escolha == "1":
        print("Tema alterado para Claro. ☀️")
    elif escolha == "2":
        print("Tema alterado para Escuro. 🌙")
    else:
        # Se a escolha for inválida, exibe uma mensagem de erro.
        print("Opção inválida. Nenhuma alteração foi feita. ❌")

# Função para ajustar o volume.
def ajustar_volume():
    # Pede ao usuário para digitar o nível de volume.
    volume = input("\nDigite o nível de volume (0 a 100): ")
    # Verifica se o valor digitado é um número entre 0 e 100.
    if volume.isdigit() and 0 <= int(volume) <= 100:
        # Se for válido, exibe o volume ajustado.
        print(f"Volume ajustado para {volume}%. 🔊")
    else:
        # Se for inválido, exibe uma mensagem de erro.
        print("Valor inválido. O volume deve estar entre 0 e 100. ❌")

# Função principal do programa.
def sistema_configuracoes():
    # Loop infinito para permitir que o usuário faça várias configurações.
    while True:
        # Pergunta ao usuário qual configuração deseja alterar.
        pergunta = [
            {
                "type": "list",  # Tipo de pergunta: lista de opções.
                "name": "config",  # Nome da resposta (será armazenada em resposta['config']).
                "message": "Escolha uma configuração:",  # Mensagem exibida ao usuário.
                "choices": [  # Opções disponíveis.
                    {"name": "🖥️  Alterar resolução", "value": "resolucao"},  # Opção 1.
                    {"name": "🎨 Alterar tema", "value": "tema"},  # Opção 2.
                    {"name": "🔊 Ajustar volume", "value": "volume"},  # Opção 3.
                    {"name": "❌ Sair", "value": "sair"},  # Opção 4.
                ],
            }
        ]
        # Faz a pergunta ao usuário e armazena a resposta.
        resposta = prompt(pergunta)

        # Executa a ação correspondente à escolha do usuário.
        if resposta["config"] == "resolucao":
            # Se o usuário escolher "Alterar resolução", chama a função correspondente.
            alterar_resolucao()
        elif resposta["config"] == "tema":
            # Se o usuário escolher "Alterar tema", chama a função correspondente.
            alterar_tema()
        elif resposta["config"] == "volume":
            # Se o usuário escolher "Ajustar volume", chama a função correspondente.
            ajustar_volume()
        else:
            # Se o usuário escolher "Sair", exibe uma mensagem e encerra o loop.
            print("Saindo do sistema de configurações. Até mais! 👋")
            break  # Sai do loop e encerra o programa.

        # Pergunta ao usuário se deseja fazer outra configuração.
        pergunta_repetir = [
            {
                "type": "confirm",  # Tipo de pergunta: confirmação (sim/não).
                "name": "repetir",  # Nome da resposta (será armazenada em resposta['repetir']).
                "message": "Deseja fazer outra configuração?",  # Mensagem exibida ao usuário.
                "default": True,  # Valor padrão (sim).
            }
        ]
        # Faz a pergunta ao usuário e armazena a resposta.
        resposta_repetir = prompt(pergunta_repetir)
        if not resposta_repetir["repetir"]:
            # Se o usuário escolher não continuar, exibe uma mensagem de agradecimento e encerra o programa.
            print("Obrigado por usar o sistema de configurações! Até mais! 👋")
            break

# Executa o programa.
if __name__ == "__main__":
    sistema_configuracoes()