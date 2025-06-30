# Importa a biblioteca InquirerPy, que é usada para criar prompts interativos no terminal
from InquirerPy import inquirer

# Importa a função get_style da biblioteca InquirerPy, que permite criar estilos personalizados para os prompts
from InquirerPy.utils import get_style

# Importa o validador pronto EmptyInputValidator da biblioteca InquirerPy
from InquirerPy.validator import EmptyInputValidator

# Style:
# Personalize o estilo do prompt, como cores e formatação.

# Define um estilo personalizado para o prompt usando a função get_style
# O estilo é passado como um dicionário, onde cada chave define um componente do prompt e o valor define sua aparência
custom_style = get_style({
    "questionmark": "#FF1493 bold",  # Define a cor e o estilo do símbolo de interrogação (rosa e em negrito)
    "answer": "#40E0D0",             # Define a cor da resposta digitada pelo usuário (verde)
})

# Cria um prompt de texto para perguntar o nome do usuário
# O método `text` é usado para criar uma pergunta que espera uma resposta em formato de texto
nome = inquirer.text(
    message="Qual é o seu nome 'style'?",  # Define a mensagem que será exibida ao usuário
    validate=EmptyInputValidator(message='A entrada não pode estar vazia'), # Usando o validador EmptyInputValidator para garantir que o nome não esteja vazio
    style=custom_style,            # Aplica o estilo personalizado definido anteriormente
).execute()  # Executa o prompt e aguarda a resposta do usuário

# Exibe uma mensagem de boas-vindas com o nome fornecido pelo usuário
# A função `print` é usada para mostrar a mensagem no terminal
print(f"Olá, {nome}!")



# Keybindings:
# Defina atalhos de teclado personalizados.



# Usa um bloco 'try' para executar o código que pode gerar exceções (erros)
try:
    # Cria um campo de texto para o usuário digitar o nome
    nome = inquirer.text(
        # Define a mensagem que será exibida ao usuário
        message="Qual é o seu nome 'Keybindings'?",
        # Define um valor padrão ("Desconhecido") caso o usuário pressione Enter sem digitar nada
        default="Desconhecido",
        # Configura uma tecla para o usuário interromper o programa (Ctrl+C no caso, representado por 'c')
        keybindings={"interrupt": [{"key": "c"}]},
        # Adiciona um validador para garantir que o usuário não deixe o campo vazio
        validate=EmptyInputValidator("O nome não pode estar vazio. Por favor, digite algo!"),
    ).execute()  # Executa o prompt para coletar a entrada do usuário

    # Exibe uma mensagem personalizada com o nome informado pelo usuário
    print(f"Olá, {nome}!")

# Este bloco será executado caso o usuário interrompa o programa usando Ctrl+C
except KeyboardInterrupt:
    # Exibe uma mensagem informando que a operação foi interrompida pelo usuário
    print("\nOperação interrompida pelo usuário.")

# Environment Variables:
# Use variáveis de ambiente para preencher valores padrão.

# Importa o módulo 'os', que permite interagir com o sistema operacional, como acessar variáveis de ambiente
import os

# Define uma variável de ambiente chamada "USER_NAME" e atribui o valor "Visitante"
os.environ["USER_NAME"] = "Visitante"

# Usa a biblioteca InquirerPy para criar uma pergunta interativa no terminal
nome = inquirer.text(
    # Mensagem que será exibida para o usuário
    message="Qual é o seu nome 'Environment Variables'?",
    
    # Define um valor padrão, que será mostrado caso o usuário não digite nada
    # O valor padrão é obtido da variável de ambiente "USER_NAME" que foi configurada acima
    # A função lambda recebe um parâmetro (que não é utilizado, por isso o nome '_' é dado)
    default=lambda _: os.getenv("USER_NAME"),
).execute()  # Executa a pergunta e armazena a resposta do usuário na variável 'nome'

# Exibe o nome que o usuário digitou ou o valor padrão caso ele não tenha digitado nada
print(nome)


# Dynamic Values:
# Use funções para gerar valores dinâmicos.

# Usa a biblioteca InquirerPy para criar uma pergunta interativa no terminal
nome = inquirer.text(
    # Mensagem que será exibida para o usuário
    message="Qual é o seu nome 'Dynamic Values'?",
    
    # Define um valor padrão que será mostrado caso o usuário não digite nada
    # A função lambda recebe um parâmetro (que não é utilizado, por isso o nome '_' é dado)
    # O valor padrão é "Usuário", já que a condição 'True' sempre será verdadeira
    # Como 'True' é sempre verdadeiro, a condição vai sempre retornar "Usuário"
    default=lambda _: "Usuário" if True else "Visitante",
).execute()  # Executa a pergunta e armazena a resposta do usuário na variável 'nome'

# Exibe o nome que o usuário digitou ou o valor padrão ("Usuário") caso ele não tenha digitado nada
print(nome)


# KeyboardInterrupt:
# Trate interrupções de teclado (Ctrl+C).

# Inicia um bloco de código que tenta executar o que está dentro do 'try'
try:
    # Usa a biblioteca InquirerPy para criar uma pergunta interativa no terminal
    # A pergunta é "Qual é o seu nome?"
    nome = inquirer.text(message="Qual é o seu nome? 'KeyboardInterrupt'").execute()

# Caso o usuário pressione 'Ctrl+C' ou tente cancelar a operação, o código dentro do 'except' será executado
except KeyboardInterrupt:
    # Exibe a mensagem "Operação cancelada pelo usuário." se o usuário cancelar a operação
    print("Operação cancelada pelo usuário.")

# Height:
# Ajuste a altura do prompt.

# Cria um prompt de seleção com várias opções para o usuário escolher
escolha = inquirer.select(
    message="Escolha uma opção: 'Height'",  # A mensagem que será exibida para o usuário, perguntando qual opção ele deseja escolher.
    choices=["Opção 1", "Opção 2", "Opção 3", "Opção 4", "Opção 5", "Opção 6"],  # As opções de escolha que o usuário pode selecionar.
    height=3,  # O número de opções visíveis na tela ao mesmo tempo. Aqui, ele exibirá 3 opções de cada vez (sem rolar a tela).
).execute()  # Executa o prompt e espera pela seleção do usuário.

# O valor escolhido será armazenado na variável 'escolha' e você pode usá-lo posteriormente no código.
print(escolha)


# Skip:
# Pule o prompt em certas condições.

ask_text = False  # Condição para decidir se o prompt de texto será exibido

if ask_text:
    nome = inquirer.text(
        message="Qual é o seu nome 'Skip'?"
    ).execute()
else:
    print("Prompt de nome pulado.")


# O qmark é uma string que define o símbolo exibido antes da pergunta. Por padrão, o InquirerPy usa o símbolo ?, 
# mas você pode substituí-lo por qualquer outro caractere ou texto.

# O amark é uma string que define o símbolo exibido antes da pergunta após ela ser respondida. 
# Por padrão, o InquirerPy não exibe nenhum símbolo após a resposta, 
# mas você pode personalizá-lo para adicionar um toque visual.

# Cria um prompt de texto para perguntar o nome do usuário
# O método `text` é usado para criar uma pergunta que espera uma resposta em formato de texto
nome = inquirer.text(
    message="Qual é o seu nome?",  # Define a mensagem que será exibida ao usuário
    validate=EmptyInputValidator(message='A entrada não pode estar vazia'), # Usando o validador EmptyInputValidator para garantir que o nome não esteja vazio
    qmark='❓',
    amark='✔'
    
).execute()  # Executa o prompt e aguarda a resposta do usuário

# Exibe uma mensagem de boas-vindas com o nome fornecido pelo usuário
# A função `print` é usada para mostrar a mensagem no terminal
print(f"Olá, {nome}!")