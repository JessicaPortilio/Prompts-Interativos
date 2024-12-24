from InquirerPy import inquirer
# Importa a biblioteca InquirerPy, que permite criar menus interativos no terminal.

from collections import Counter
# Importa a função Counter da biblioteca collections, que será usada para contar os votos.

# Exibe uma mensagem inicial dando boas-vindas ao usuário.
print("Bem-vindo à Enquete Interativa!")

# Solicita ao usuário que insira o tópico da enquete (por exemplo, "Qual linguagem de programação você prefere?").
topico = inquirer.text(
    message="Digite o tópico da enquete:"
).execute()

# Solicita ao usuário que configure as opções disponíveis para a enquete.
print("\nAgora, configure as opções da enquete.")
nova_opcao = True
# Define a variável de controle 'nova_opcao' como True para permitir a entrada de múltiplas opções.
opcoes = []
# Cria uma lista vazia chamada 'opcoes' para armazenar as opções adicionadas pelo usuário.

while nova_opcao:
    # Inicia um loop que permite ao usuário adicionar várias opções.
    opcao = inquirer.text(
        message="Digite uma opção para a enquete (ou deixe em branco para finalizar):"
    ).execute()
    # Solicita que o usuário insira uma nova opção para a enquete.
    if opcao.strip():
        # Verifica se a entrada não está em branco.
        opcoes.append(opcao)
        # Adiciona a opção digitada à lista 'opcoes'.
    else:
        # Se o usuário não digitar nada, interrompe o processo de adicionar opções.
        nova_opcao = False

# Define opções padrão se o usuário não configurar nenhuma.
if not opcoes:
    opcoes = ["Opção Padrão 1", "Opção Padrão 2"]
# Garante que a enquete terá opções mesmo que o usuário não tenha adicionado nenhuma.

# Lista para armazenar os votos de todos os participantes.
votos = []

# Inicia o processo de votação e informa que cada participante deverá votar individualmente.
print("\nIniciando a enquete. Cada participante deverá votar separadamente.")
while True:
    # Mostra o tópico da enquete para o participante e solicita que ele vote em uma das opções.
    print(f"\nEnquete: {topico}")
    resposta = inquirer.select(
        message="Escolha uma opção:",
        choices=opcoes,
    ).execute()
    # Exibe as opções disponíveis e registra a escolha do participante na variável 'resposta'.
    
    votos.append(resposta)
    # Adiciona o voto do participante à lista de votos.
    print(f"Você votou em: {resposta}")
    # Exibe a opção escolhida pelo participante.

    continuar = inquirer.confirm(
        message="Outro participante deseja votar?"
    ).execute()
    # Pergunta se há mais participantes para votar. Se a resposta for "Sim", continua o loop; se "Não", encerra.
    if not continuar:
        break

# Conta os votos recebidos para cada opção usando a função Counter.
resultado = Counter(votos)

# Exibe o resultado final da enquete com o número de votos para cada opção.
print("\n--- Resultado da Enquete ---")
print(f"Tópico: {topico}")
for opcao, quantidade in resultado.items():
    # Percorre o dicionário criado pelo Counter para mostrar cada opção e seu número de votos.
    print(f"{opcao}: {quantidade} votos")

# Exibe uma mensagem final de agradecimento.
print("Obrigado por participar da enquete!")
