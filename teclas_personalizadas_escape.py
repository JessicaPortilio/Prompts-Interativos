# Importa o módulo `inquirer` da biblioteca `InquirerPy`, usado para criar prompts interativos no terminal.
from InquirerPy import inquirer

# Importa uma versão modificada do comando `print`, chamada `patched_print`, que é útil para integração com a biblioteca `InquirerPy`.
from InquirerPy.utils import patched_print as print

# Cria um prompt de entrada de texto que exibe a mensagem "Digite algo:" no terminal.
prompt = inquirer.text(message="Digite algo:")

# Define uma função que será executada quando a tecla "ESC" for pressionada durante o prompt.
@prompt.register_kb("escape")  # Associa a função à tecla "ESC".
def precionando_escape(_):
    # Exibe uma mensagem no terminal informando que a tecla "ESC" foi pressionada.
    print("Você pressionou ESC!")

# Executa o prompt no terminal, permitindo que o usuário insira texto. 
# Retorna o texto inserido quando o usuário pressiona "Enter".
result = prompt.execute()
