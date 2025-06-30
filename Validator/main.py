# 1. O que é um Validator?
# No InquirerPy, um Validator é uma função que você pode usar para validar 
# as respostas dos usuários antes de elas serem aceitas como válidas. 
# Ele permite garantir que a entrada do usuário esteja em conformidade com as regras que você definiu, 
# como um formato de e-mail válido, um número positivo ou uma resposta dentro de um intervalo específico.

# Função de Validação
# O Validator é uma função que recebe o valor inserido pelo usuário e deve retornar um valor booleano ou lançar uma exceção 
# (raise Exception) se o valor não for válido.

# 2. Como Funciona o Validator?
# A principal função de um Validator é verificar se o valor inserido pelo usuário atende aos critérios definidos. 
# Se o valor não for válido, ele retorna uma exceção ou um erro, forçando o usuário a inserir um valor correto.

# Exemplo Básico de Validação de Entrada:
# Vamos criar um exemplo de validador simples que verifica se o nome inserido tem pelo menos 3 caracteres.

# Importa a biblioteca InquirerPy, que é usada para criar prompts interativos no terminal.
from InquirerPy import inquirer

# Cria uma pergunta de texto (input) para o usuário.
# O parâmetro "message" define a mensagem que será exibida ao usuário.
# O parâmetro "validate" é uma função que valida a entrada do usuário.
# Neste caso, usamos uma função lambda (uma função anônima) para verificar se o nome tem 3 ou mais caracteres.
# O parâmetro "invalid_message" define a mensagem de erro que será exibida se a validação falhar.
resultado = inquirer.text(
    message="Qual é o seu nome?",  # Pergunta exibida ao usuário.
    validate=lambda result: len(result) >= 3,  # Validação: o nome deve ter 3 ou mais caracteres.
    invalid_message="O nome precisa ter pelo menos 3 caracteres.",  # Mensagem de erro se a validação falhar.
).execute()  # Executa o prompt e aguarda a entrada do usuário.

# Exibe o resultado no terminal.
# A função "print" imprime uma mensagem formatada.
# O "f" antes da string permite que variáveis sejam inseridas diretamente dentro dela, usando chaves {}.
# Aqui, o valor da variável "resultado" (o nome digitado pelo usuário) é inserido na mensagem.
print(f"Nome válido: {resultado}")



# Importa a função "prompt" da biblioteca InquirerPy, que é usada para criar prompts interativos no terminal.
from InquirerPy import prompt

# Define uma lista de perguntas. Cada pergunta é um dicionário com parâmetros específicos.
# Neste caso, temos apenas uma pergunta: o nome do usuário.
perguntas = [
    {
        "type": "input",  # Tipo da pergunta: entrada de texto.
        "name": "nome",   # Nome da variável que armazenará a resposta.
        "message": "Qual é o seu nome?",  # Mensagem exibida ao usuário.
        "validate": lambda resposta: len(resposta) >= 3,  # Função de validação.
        "invalid_message": "O nome precisa ter pelo menos 3 caracteres.",  # Mensagem de erro.
    }
]

# Executa o prompt com as perguntas definidas.
# A função "prompt" exibe as perguntas ao usuário e coleta as respostas.
respostas = prompt(perguntas)

# Exibe o resultado no terminal.
# A função "print" imprime uma mensagem formatada.
# O "f" antes da string permite que variáveis sejam inseridas diretamente dentro dela, usando chaves {}.
# Aqui, o valor da chave "nome" no dicionário "respostas" é inserido na mensagem.
print(f"Nome válido: {respostas['nome']}")

# 3.1 Validador de E-mail
# Um validador que verifica se o valor inserido parece um endereço de e-mail válido.


# Importa o módulo "re" para trabalhar com expressões regulares.
# O módulo re é usado para trabalhar com expressões regulares, que são úteis para validar padrões de texto, como e-mails.
import re
# Importa a função "prompt" da biblioteca InquirerPy, que é usada para criar prompts interativos no terminal.
from InquirerPy import prompt

# Função de validação de e-mail
def valida_email(email):
    """
    Valida se o e-mail fornecido está no formato correto.
    Retorna True se o e-mail for válido ou False se for inválido.
    """
    # A função valida_email recebe um e-mail como entrada e verifica se ele está no formato correto.
    # A função re.match retorna um objeto de correspondência se o e-mail for válido ou None se for inválido.
    #A função bool converte o resultado em True (válido) ou False (inválido).
    
    # Expressão regular para validar o formato do e-mail.
    # A expressão regular r"[^@]+@[^@]+\.[^@]+" verifica se o e-mail contém:
    # A expressão verifica se o e-mail contém:
    # - Um ou mais caracteres antes do "@" ([^@]+).
    # - Um "@".
    # - Um ou mais caracteres após o "@" ([^@]+).
    # - Um ponto ".".
    # - Um ou mais caracteres após o ponto ([^@]+).
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

# Define a pergunta que será feita ao usuário.
pergunta = [
    {
        "type": "input",  # Tipo da pergunta: entrada de texto.
        "name": "email",  # Nome da variável que armazenará a resposta.
        "message": "Qual é o seu e-mail?",  # Mensagem exibida ao usuário.
        "validate": valida_email,  # Função de validação para o e-mail.
        "invalid_message": "Por favor, insira um e-mail válido.",  # Mensagem de erro se a validação falhar.
    }
]

# Executa o prompt com a pergunta definida.
# A função "prompt" exibe a pergunta ao usuário e coleta a resposta.
resposta = prompt(pergunta)

# Exibe o e-mail fornecido pelo usuário.
# A função "print" imprime uma mensagem formatada.
# O "f" antes da string permite que variáveis sejam inseridas diretamente dentro dela, usando chaves {}.
# Aqui, o valor da chave "email" no dicionário "resposta" é inserido na mensagem.
print(f"E-mail fornecido: {resposta['email']}")

# 3.2 Validador de Número Positivo
# Aqui, vamos validar se o número inserido é positivo.

# Importa a função "prompt" da biblioteca InquirerPy, que é usada para criar prompts interativos no terminal.
from InquirerPy import prompt

# Função de validação de número positivo
def valida_numero(numero):
    """
    Valida se o valor fornecido é um número positivo.
    Retorna True se for válido ou False se for inválido.
    """
    try:
        # Tenta converter a entrada para float.
        num = float(numero)
        # Verifica se o número é positivo.
        if num <= 0:
            return False  # Retorna False se o número for negativo ou zero.
        return True  # Retorna True se o número for válido.
    except ValueError:
        # Se a conversão para float falhar, retorna False.
        return False

# Define a pergunta que será feita ao usuário.
pergunta = [
    {
        "type": "input",  # Tipo da pergunta: entrada de texto.
        "name": "numero",  # Nome da variável que armazenará a resposta.
        "message": "Digite um número positivo:",  # Mensagem exibida ao usuário.
        "validate": valida_numero,  # Função de validação para o número.
        "invalid_message": "Entrada inválida. Digite um número positivo.",  # Mensagem de erro.
    }
]

# Executa o prompt com a pergunta definida.
# A função "prompt" exibe a pergunta ao usuário e coleta a resposta.
resposta = prompt(pergunta)

# Exibe o número fornecido pelo usuário.
# A função "print" imprime uma mensagem formatada.
# O "f" antes da string permite que variáveis sejam inseridas diretamente dentro dela, usando chaves {}.
# Aqui, o valor da chave "numero" no dicionário "resposta" é inserido na mensagem.
print(f"Número fornecido: {resposta['numero']}")


# 3.3 Validador de Tamanho Mínimo
# Você também pode validar o tamanho de uma string, por exemplo, para garantir que a senha tenha pelo menos 8 caracteres.

# Importa a função "prompt" da biblioteca InquirerPy, que é usada para criar prompts interativos no terminal.
from InquirerPy import prompt

# Função de validação de senha
def valida_senha(senha):
    """
    Valida se a senha tem pelo menos 8 caracteres.
    Retorna True se for válida ou False se for inválida.
    """
    if len(senha) >= 8:
        return True  # Retorna True se a senha tiver 8 ou mais caracteres.
    return False  # Retorna False se a senha tiver menos de 8 caracteres.

# Define a pergunta que será feita ao usuário.
pergunta = [
    {
        "type": "password",  # Tipo da pergunta: entrada de senha (o texto digitado é ocultado).
        "name": "senha",  # Nome da variável que armazenará a resposta.
        "message": "Digite uma senha (mínimo 8 caracteres):",  # Mensagem exibida ao usuário.
        "validate": valida_senha,  # Função de validação para a senha.
        "invalid_message": "A senha deve ter pelo menos 8 caracteres.",  # Mensagem de erro.
    }
]

# Executa o prompt com a pergunta definida.
# A função "prompt" exibe a pergunta ao usuário e coleta a resposta.
resposta = prompt(pergunta)

# Exibe a senha fornecida pelo usuário.
# A função "print" imprime uma mensagem formatada.
# O "f" antes da string permite que variáveis sejam inseridas diretamente dentro dela, usando chaves {}.
# Aqui, o valor da chave "senha" no dicionário "resposta" é inserido na mensagem.
print(f"Senha fornecida: {resposta['senha']}")


