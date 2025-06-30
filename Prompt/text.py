# Aula 1: Prompt text no InquirerPy
# 1. O que é o prompt text?
# O text é um dos prompts mais básicos da biblioteca InquirerPy. 
# Ele permite que o usuário insira um texto livremente no terminal.

# Casos de uso:

# Capturar nomes de usuários.
# Solicitar um e-mail ou qualquer outro dado textual.
# Perguntar ao usuário um código ou palavra-chave.


# Importa a função "prompt" da biblioteca InquirerPy, 
# que é usada para fazer perguntas interativas no terminal
from InquirerPy import prompt

# Aqui está um exemplo básico de uso:

# Define a pergunta que será feita ao usuário. 
# A pergunta é armazenada em uma lista (mesmo que tenha apenas uma pergunta)
pergunta = [{
    "type": "input",  # Tipo de pergunta, que será uma entrada de texto (onde o usuário digita algo)
    "name": "nome",  # O nome da variável onde a resposta do usuário será armazenada (aqui será 'nome')
    "message": "Qual é o seu nome?",  # A mensagem que será exibida para o usuário na tela
}]

# Faz a pergunta para o usuário e armazena a resposta na variável 'resposta'. 
# O usuário vai digitar algo.
resposta = prompt(pergunta)

# Exibe a mensagem de saudação na tela, incluindo o nome do usuário que foi inserido
print(f'Olá, {resposta["nome"]}!')  # A resposta do usuário, que está armazenada na chave 'nome', 
# será inserida na saudação

# Então resumindo:
# "type": "input" → Define que este é um prompt de texto.
# "name": "nome" → Nome da variável que armazenará a resposta.
# "message": "Qual é o seu nome?" → Mensagem exibida no terminal.

# 3. Adicionando Validação
# Podemos validar a entrada do usuário, como garantir que o nome não esteja vazio:

# Importa a função "prompt" da biblioteca InquirerPy, que é usada para fazer perguntas interativas no terminal
from InquirerPy import prompt

# Importa o validador "EmptyInputValidator", que verifica se o campo de entrada está vazio
from InquirerPy.validator import EmptyInputValidator

# Define a pergunta que será feita ao usuário. 
# A pergunta é armazenada em uma lista (mesmo que tenha apenas uma pergunta)
pergunta = [
    {
        "type": "input",  # Tipo de pergunta, que será uma entrada de texto (onde o usuário digita algo)
        "name": "nome",  # O nome da variável onde a resposta do usuário será armazenada (aqui será 'nome')
        "message": "Digite seu nome:",  # A mensagem que será exibida para o usuário na tela
        "validate": EmptyInputValidator("O nome não pode estar vazio!"),  # A validação que impede que o nome seja deixado em branco
    }
]

# Faz a pergunta para o usuário e armazena a resposta na variável 'resposta'. 
# O usuário vai digitar algo.
resposta = prompt(pergunta)

# Exibe a mensagem de boas-vindas na tela, 
# incluindo o nome do usuário que foi inserido
print(f"Bem-vindo(a), {resposta['nome']}!")  
# A resposta do usuário, que está armazenada na chave 'nome', 
# será inserida na saudação

# O que foi adicionado?

# "validate": EmptyInputValidator("O nome não pode estar vazio!")
# → Exibe um erro se o usuário pressionar Enter sem digitar nada.

# 4. Personalizando o Estilo
# Podemos mudar as cores e o estilo do terminal com style:

# Importa a função 'prompt' da biblioteca InquirerPy, que permite fazer perguntas interativas
from InquirerPy import prompt
# Importa a validação que verifica se a entrada do usuário não está vazia
from InquirerPy.validator import EmptyInputValidator

# Definindo o estilo personalizado para as mensagens
custom_style = {
    "questionmark": "fg:#4B0082 bold",  # Define a cor roxa escura e o estilo em negrito para o ponto de interrogação "?"
    "question": "fg:#191970 bold",  # Define a cor azul escura e o estilo em negrito para a pergunta
    "answer": "fg:#FF1493 bold",  # Define a cor rosa choque e o estilo em negrito para a resposta do usuário
}

# Definindo a pergunta a ser feita ao usuário
pergunta = [
    {
        "type": "input",  # Especifica que a pergunta será uma entrada de texto, onde o usuário deve digitar uma resposta
        "name": "nome",  # Nome da variável onde será armazenada a resposta do usuário
        "message": "Digite seu nome:",  # Mensagem que será exibida pedindo ao usuário para digitar seu nome
        "validate": EmptyInputValidator("O nome não pode estar vazio!"),  # Valida se o campo não foi deixado em branco
    }
]

# Exibe a pergunta para o usuário, aplica o estilo personalizado e armazena a resposta do usuário
resposta = prompt(pergunta, style=custom_style)

# Exibe uma mensagem de boas-vindas com o nome que o usuário digitou
print(f"Bem-vindo, {resposta['nome']}!")


#  O que mudou?

# questionmark → Altera a cor do "?"
# question → Altera a cor do texto da pergunta
# answer → Altera a cor da resposta do usuário

# 5. Criando um Input Dinâmico
# Podemos alterar a pergunta com base na resposta anterior:

# Importa a função 'prompt' da biblioteca InquirerPy, que é usada para criar perguntas interativas
from InquirerPy import prompt

# Definindo uma lista de perguntas que serão feitas ao usuário
perguntas = [
    # A primeira pergunta é sobre o nome do usuário
    {
        "type": "input",  # Define que a pergunta será de entrada de texto, ou seja, o usuário deve digitar algo
        "name": "nome",  # O nome da variável onde a resposta do usuário será armazenada
        "message": "Digite seu nome:",  # A mensagem que será exibida ao usuário pedindo para digitar o nome
    },
    # A segunda pergunta é sobre o sobrenome do usuário
    {
        "type": "input",  # Define que esta também será uma entrada de texto
        "name": "sobrenome",  # O nome da variável onde o sobrenome do usuário será armazenado
        # A mensagem da pergunta usa uma função lambda, que cria uma mensagem personalizada com base no nome dado
        "message": lambda respostas: f"Olá {respostas['nome']}, qual é o seu sobrenome?",  
        # A função lambda acessa a resposta da primeira pergunta (nome) para personalizar a mensagem da segunda
    }
]

# A função 'prompt' exibe as perguntas para o usuário e armazena as respostas na variável 'respostas'
# O usuário irá primeiro digitar o nome e depois o sobrenome, com a segunda pergunta sendo personalizada
respostas = prompt(perguntas)

# Exibe o nome completo do usuário na tela, juntando o nome e o sobrenome
# As respostas são acessadas usando as chaves 'nome' e 'sobrenome' que foram definidas nas perguntas
print(f"Seu nome completo é {respostas['nome']} {respostas['sobrenome']}.")


# Resumo da Aula
# ✅ O prompt text permite entrada livre do usuário.
# ✅ Podemos validar a entrada com EmptyInputValidator.
# ✅ O estilo pode ser customizado passando um discionário.
# ✅ É possível criar perguntas dinâmicas.