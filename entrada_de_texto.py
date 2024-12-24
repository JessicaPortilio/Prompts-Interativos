# Importa a biblioteca InquirerPy, que permite criar prompts interativos no terminal para coletar dados do usuário.
from InquirerPy import inquirer

# Solicite informações do usuário
# Cria um prompt que pede ao usuário para digitar o nome e armazena a resposta na variável 'nome'.
nome = inquirer.text(message="Digite o seu nome:").execute()

# Exibe uma mensagem no terminal saudando o usuário com o nome que ele digitou.
print(f"Olá, {nome}!")  
