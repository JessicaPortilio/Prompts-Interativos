# 1. O que é o prompt number?
# O prompt number permite que o usuário insira um número no terminal.
# Ele pode ser usado para:
# ✅ Solicitar valores numéricos, como idade, preço ou quantidade.
# ✅ Definir limites mínimos e máximos para a entrada.
# ✅ Garantir que o usuário insira apenas números.

# 2. Como usar o number prompt?
# Aqui está um exemplo básico onde o usuário insere um número:

# Importa a função 'prompt' da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista chamada 'pergunta' contendo um dicionário que configura a pergunta interativa.
pergunta = [
    {
        "type": "number",  # Define o tipo da pergunta como 'number', garantindo que o usuário digite apenas números.
        "name": "idade",  # Nome da variável onde será armazenada a resposta do usuário.
        "message": "Qual a sua idade?",  # Mensagem exibida ao usuário solicitando que informe sua idade.
    }
]

# Exibe a pergunta no terminal e armazena a resposta na variável 'resposta'.
resposta = prompt(pergunta)

# Exibe no terminal a idade informada pelo usuário.
print(f"Idade informada: {resposta['idade']}")

# "type": "number" → Define que a entrada deve ser um número.
# O usuário só pode inserir valores numéricos.

# 3. Definir um Valor Padrão
# Podemos sugerir um valor padrão usando o parâmetro default:


# Importa a função 'prompt' da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista chamada 'pergunta' contendo um dicionário que configura a pergunta interativa.
pergunta = [
    {
        "type": "number",  # Define o tipo da pergunta como 'number', garantindo que o usuário digite apenas números.
        "name": "quantidade",  # Nome da variável onde será armazenada a resposta do usuário.
        "message": "Quantos produtos deseja comprar?",  # Mensagem exibida ao usuário solicitando a quantidade desejada.
        "default": 1 ,  # Define o valor padrão como 1 caso o usuário não digite nada.
    }
]

# Exibe a pergunta no terminal e armazena a resposta na variável 'resposta'.
resposta = prompt(pergunta)

# Exibe no terminal a quantidade de produtos escolhida pelo usuário.
print(f"Quantidade escolhida: {resposta['quantidade']}")

# O terminal já exibe 1 como valor inicial.
# O usuário pode aceitar ou editar esse valor.

# 4. Definir Mínimo e Máximo
# Podemos definir limites para a entrada do usuário:

# Importa a função 'prompt' da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista chamada 'pergunta' contendo um dicionário que configura a pergunta interativa.
pergunta = [
    {
        "type": "number",  # Define o tipo da pergunta como 'number', garantindo que o usuário digite apenas números.
        "name": "nota",  # Nome da variável onde será armazenada a resposta do usuário.
        "message": "Dê uma nota de 1 a 10:",  # Mensagem exibida ao usuário solicitando uma nota de 1 a 10.
        "min_allowed": 1,  # Define o valor mínimo permitido como 1.
        "max_allowed": 10,  # Define o valor máximo permitido como 10.
    }
]

# Exibe a pergunta no terminal e armazena a resposta na variável 'resposta'.
resposta = prompt(pergunta)

# Exibe no terminal a nota escolhida pelo usuário.
print(f"Nota escolhida: {resposta['nota']}")


# "min_allowed": 1 → O menor valor permitido é 1.
# "max_allowed": 10 → O maior valor permitido é 10.

# Importa a função 'prompt' da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Função para validar se o número inserido pelo usuário é um número PAR.
def validar_numero(entrada):
    try:
        # Converte a entrada do usuário para um número inteiro.
        numero = int(entrada)
        # Verifica se o número é ímpar.
        if numero % 2 != 0:
            return "Por favor, insira um número PAR!"  # Mensagem de erro caso o número seja ímpar.
        # Se o número for par, a validação é aprovada.
        return True
    except ValueError:
        # Se a conversão para inteiro falhar (por exemplo, se o usuário inserir letras), retorna uma mensagem de erro.
        return "Por favor, insira um número válido!"

# Define a pergunta que será feita ao usuário.
pergunta = [
    {
        "type": "number",  # Tipo de pergunta: número.
        "name": "numero_par",  # Nome da resposta (será armazenada em resposta['numero_par']).
        "message": "Digite um número PAR:",  # Mensagem exibida ao usuário.
    }
]

# Loop para garantir que o usuário insira um número par válido.
while True:
    # Faz a pergunta ao usuário e armazena a resposta na variável 'resposta'.
    resposta = prompt(pergunta)
    
    # Verifica se a resposta passou na validação e se é um número par.
    if validar_numero(resposta["numero_par"]) == True:
        # Se a resposta for válida, sai do loop e continua a execução do código.
        break
    else:
        # Se a resposta for inválida, exibe uma mensagem de erro e repete a pergunta.
        print("Número inválido! Tente novamente.")

# Exibe no terminal o número par escolhido pelo usuário.
print(f"Número escolhido: {resposta['numero_par']}")

# 7. Customizando a Interface
# Podemos mudar a aparência do prompt com cores personalizadas:

# Importa a função 'prompt' da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Definindo um estilo personalizado para as mensagens exibidas no terminal.
custom_style = {
    "questionmark": "fg:#4B0082 bold",  # Define o ponto de interrogação "?" na cor roxa escura e em negrito.
    "question": "fg:#191970 bold",  # Define a cor azul escura e o estilo em negrito para a pergunta.
    "answer": "fg:#FF1493 bold",  # Define a cor rosa choque e o estilo em negrito para a resposta do usuário.
}

# Criando uma lista com a pergunta que será feita ao usuário.
pergunta = [
    {
        "type": "number",  # Define que o usuário deve inserir um número.
        "name": "nota",  # Nome da resposta (será armazenada em resposta['nota']).
        "message": "Dê uma nota de 1 a 10:",  # Mensagem exibida para solicitar uma nota ao usuário.
        "min_allowed": 1,  # Define que o menor valor permitido é 1.
        "max_allowed": 10,  # Define que o maior valor permitido é 10.
    }
]

# Exibe a pergunta no terminal com o estilo personalizado e armazena a resposta na variável 'resposta'.
resposta = prompt(pergunta, style=custom_style)

# Exibe no terminal a nota escolhida pelo usuário.
print(f"Nota escolhida: {resposta['nota']}")


# 8. Exemplo Completo: Calculadora de validar_desconto
# A ideia é criar um sistema de cálculo de descontos que permita ao usuário escolher diferentes porcentagens de desconto 
# e validar entradas para garantir que os valores sejam corretos.

# Importa a função 'prompt' da biblioteca 'InquirerPy', que é usada para criar perguntas interativas no terminal.
from InquirerPy import prompt

# Função para validar se o preço é um número válido e maior que zero.
def validar_preco(entrada):
    try:
        # Tenta converter a entrada para um número decimal (float).
        preco = float(entrada)
        # Verifica se o preço é menor ou igual a zero.
        if preco <= 0:
            # Se for, retorna uma mensagem de erro.
            return "O preço deve ser maior que zero!"
        # Se o preço for válido, retorna True.
        return True
    except ValueError:
        # Se a conversão para float falhar (por exemplo, se o usuário digitar texto), retorna uma mensagem de erro.
        return "Por favor, insira um número válido."

# Função para validar se a porcentagem de desconto é um número válido e maior que zero.
def validar_desconto(entrada):
    try:
        # Tenta converter a entrada para um número decimal (float).
        desconto = float(entrada)
        # Verifica se o desconto é menor ou igual a zero.
        if desconto <= 0:
            # Se for, retorna uma mensagem de erro.
            return "A porcentagem de desconto deve ser maior que zero!"
        # Se o desconto for válido, retorna True.
        return True
    except ValueError:
        # Se a conversão para float falhar (por exemplo, se o usuário digitar texto), retorna uma mensagem de erro.
        return "Por favor, insira um número válido."

# Função principal do programa.
def calcular_desconto():
    # Loop infinito para permitir que o usuário calcule descontos para vários produtos.
    while True:
        # Pergunta ao usuário o preço do produto.
        pergunta_preco = [
            {
                "type": "input",  # Tipo de pergunta: entrada de texto.
                "name": "preco",  # Nome da resposta (será armazenada em resposta['preco']).
                "message": "Informe o preço do produto:",  # Mensagem exibida ao usuário.
            }
        ]
        # Faz a pergunta ao usuário e armazena a resposta.
        resposta_preco = prompt(pergunta_preco)
        # Obtém o preço digitado pelo usuário.
        preco = resposta_preco["preco"]

        # Valida o preço manualmente usando a função 'validar_preco'.
        validacao_preco = validar_preco(preco)
        if validacao_preco != True:
            # Se o preço for inválido, exibe a mensagem de erro.
            print(validacao_preco)
            # Volta ao início do loop para pedir o preço novamente.
            continue

        # Converte o preço para float (número decimal).
        preco_original = float(preco)

        # Pergunta ao usuário a porcentagem de desconto.
        pergunta_desconto = [
            {
                "type": "list",  # Tipo de pergunta: lista de opções.
                "name": "desconto",  # Nome da resposta (será armazenada em resposta['desconto']).
                "message": "Escolha a porcentagem de desconto:",  # Mensagem exibida ao usuário.
                "choices": ["10%", "20%", "30%", "Outro valor"],  # Opções disponíveis.
            }
        ]
        # Faz a pergunta ao usuário e armazena a resposta.
        resposta_desconto = prompt(pergunta_desconto)

        # Define a porcentagem de desconto com base na escolha do usuário.
        if resposta_desconto["desconto"] == "Outro valor":
            # Se o usuário escolher "Outro valor", entra em um loop para pedir a porcentagem de desconto.
            while True:
                pergunta_outro_desconto = [
                    {
                        "type": "input",  # Tipo de pergunta: entrada de texto.
                        "name": "outro_desconto",  # Nome da resposta (será armazenada em resposta['outro_desconto']).
                        "message": "Informe a porcentagem de desconto (ex: 15 para 15%):",  # Mensagem exibida ao usuário.
                    }
                ]
                # Faz a pergunta ao usuário e armazena a resposta.
                resposta_outro_desconto = prompt(pergunta_outro_desconto)
                # Obtém o valor do desconto digitado pelo usuário.
                outro_desconto = resposta_outro_desconto["outro_desconto"]

                # Valida a porcentagem de desconto manualmente usando a função 'validar_desconto'.
                validacao_desconto = validar_desconto(outro_desconto)
                if validacao_desconto == True:
                    # Se o desconto for válido, converte para decimal e divide por 100 para obter a porcentagem.
                    desconto_percentual = float(outro_desconto) / 100
                    # Sai do loop.
                    break
                else:
                    # Se o desconto for inválido, exibe a mensagem de erro.
                    print(validacao_desconto)
        else:
            # Se o usuário escolher uma das opções predefinidas (10%, 20%, 30%),
            # remove o símbolo '%' e converte para decimal, dividindo por 100.
            desconto_percentual = float(resposta_desconto["desconto"].replace("%", "")) / 100

        # Calcula o valor do desconto.
        desconto = preco_original * desconto_percentual
        # Calcula o preço final após o desconto.
        preco_final = preco_original - desconto

        # Exibe os resultados formatados.
        print(f"\nPreço original: R$ {preco_original:.2f}")
        print(f"Desconto de {desconto_percentual * 100:.0f}%: R$ {desconto:.2f}")
        print(f"Preço final: R$ {preco_final:.2f}\n")

        # Pergunta ao usuário se deseja calcular outro desconto.
        pergunta_repetir = [
            {
                "type": "confirm",  # Tipo de pergunta: confirmação (sim/não).
                "name": "repetir",  # Nome da resposta (será armazenada em resposta['repetir']).
                "message": "Deseja calcular o desconto para outro produto?",  # Mensagem exibida ao usuário.
                "default": True,  # Valor padrão (sim).
            }
        ]
        # Faz a pergunta ao usuário e armazena a resposta.
        resposta_repetir = prompt(pergunta_repetir)
        if not resposta_repetir["repetir"]:
            # Se o usuário escolher não continuar, exibe uma mensagem de agradecimento e encerra o programa.
            print("Obrigado por usar o sistema de descontos! Até mais!")
            break

# Executa o programa.
if __name__ == "__main__":
    calcular_desconto()