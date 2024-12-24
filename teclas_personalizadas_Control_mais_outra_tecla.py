# Importa o módulo `inquirer` da biblioteca `InquirerPy`, usado para criar prompts interativos no terminal.
from InquirerPy import inquirer

# Importa uma versão especial do comando `print`, chamada `patched_print`, que funciona bem com os prompts interativos.
from InquirerPy.utils import patched_print as print

# Cria um prompt de entrada de texto que exibe a mensagem "Digite algo:" no terminal.
prompt = inquirer.text(message="Digite algo:")

# Define uma funcionalidade personalizada para o prompt, que será executada quando a combinação de teclas "CTRL+A" for pressionada.
@prompt.register_kb("c-a")  # Registra a combinação "CTRL+A" para esta função.
def precionando_ctrl_a(_):  # Define a função que será chamada ao pressionar "CTRL+A".
    # Exibe a mensagem "Você pressionou CTRL+A!" no terminal.
    print("Você pressionou CTRL+A!")

# Define outra funcionalidade personalizada para o prompt, que será executada quando a combinação de teclas "CTRL+Z" for pressionada.
@prompt.register_kb("c-z")  # Registra a combinação "CTRL+Z" para esta função.
def precionando_ctrl_z(_):  # Define a função que será chamada ao pressionar "CTRL+Z".
    # Exibe a mensagem "Você pressionou CTRL+Z!" no terminal.
    print("Você pressionou CTRL+Z!")

# Executa o prompt no terminal, permitindo ao usuário digitar algo e usar as combinações de teclas personalizadas (CTRL+A e CTRL+Z).
result = prompt.execute()

