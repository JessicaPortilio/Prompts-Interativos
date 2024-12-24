# Importa a biblioteca InquirerPy, que ajuda a criar perguntas interativas no terminal.
from InquirerPy import inquirer  

# Permita ao usuário selecionar mais de uma opção.
# Checkboxes
linguagens = inquirer.checkbox(  # Cria um prompt onde o usuário pode selecionar várias opções marcando caixas de seleção (checkboxes).
    message="Quais linguagens você conhece?",  # Mensagem exibida para o usuário, explicando o que ele deve fazer.
    choices=["Python", "Java", "C", "C++"],  # Lista de opções que o usuário pode marcar.
).execute()  # Executa o prompt e retorna as opções selecionadas pelo usuário em forma de lista.

print(f"Você selecionou: {', '.join(linguagens)}")  
# Combina as opções selecionadas em uma única string, separando-as por vírgulas, e exibe no terminal.
# Por exemplo, se o usuário selecionar "Python" e "Java", o programa exibirá: "Você selecionou: Python, Java".