# Importa a biblioteca InquirerPy, que ajuda a criar perguntas interativas no terminal para coletar dados do usuário.
from InquirerPy import inquirer  

# Permita ao usuário escolher uma opção entre várias.
# Pergunta de múltipla escolha
linguagem = inquirer.select(  # Cria um prompt onde o usuário pode selecionar uma opção de uma lista.
    message="Qual linguagem de programação você prefere?",  # Mensagem exibida no terminal para o usuário.
    choices=["Python", "Java", "C", "C++"],  # Lista de opções que o usuário pode escolher.
).execute()  # Executa o prompt para que o usuário possa interagir com ele e retorna a escolha.

print(f'Você escolheu: {linguagem}')  # Exibe no terminal a opção que o usuário escolheu.
