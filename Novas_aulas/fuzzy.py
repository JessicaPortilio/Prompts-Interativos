# O prompt fuzzy é uma ferramenta poderosa para interfaces de linha de comando (CLI) 
# que permite ao usuário pesquisar e selecionar uma opção de uma lista usando 
# correspondência difusa (fuzzy search).

# Importa a biblioteca InquirerPy, que é usada para criar prompts interativos no terminal.
from InquirerPy import inquirer

# Cria um prompt de pesquisa difusa (fuzzy search) para o usuário.
# O usuário verá uma mensagem e poderá digitar para pesquisar e selecionar uma opção.
escolha = inquirer.fuzzy(
    # Define a mensagem que será exibida para o usuário.
    message="Pesquise e selecione uma opção:",
    # Define a lista de opções que o usuário pode escolher.
    choices=["Python", "JavaScript", "Java", "C++", "Ruby"],
).execute()  # Executa o prompt e aguarda a escolha do usuário.

# Exibe a opção que o usuário escolheu.
print(f"Você escolheu: {escolha}")