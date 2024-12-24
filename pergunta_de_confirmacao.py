# Importa a biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import inquirer  

# Ideal para decisões binárias. 
# Decisões binárias referem-se a situações onde existem apenas duas opções possíveis 
# ou dois resultados possíveis.

confirmar = inquirer.confirm(message="Deseja continuar?").execute()  
# Cria um prompt de confirmação, onde o usuário pode responder "sim" ou "não" à pergunta "Deseja continuar?".
# A resposta (True para "sim" e False para "não") é armazenada na variável 'confirmar'.

if confirmar:  # Verifica se a resposta do usuário foi "sim" (True).
    print('Você decidiu continuar!')  # Exibe uma mensagem informando que o usuário decidiu continuar.
else:  # Caso a resposta seja "não" (False).
    print("Você optou por sair!")  # Exibe uma mensagem informando que o usuário decidiu sair.
