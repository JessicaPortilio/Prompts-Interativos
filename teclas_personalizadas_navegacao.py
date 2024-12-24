# Importa o módulo `inquirer` da biblioteca `InquirerPy`, usado para criar prompts interativos no terminal.
from InquirerPy import inquirer

# Importa uma versão especial do comando `print`, chamada `patched_print`, que funciona corretamente com os prompts interativos.
from InquirerPy.utils import patched_print as print

# Cria um prompt de entrada de texto que exibe a mensagem "Digite algo:" no terminal.
prompt = inquirer.text(message="Digite algo:")

# Define uma funcionalidade personalizada para o prompt que será executada quando a tecla "HOME" for pressionada.
@prompt.register_kb("home")  # Registra a tecla "HOME" para esta função.
def precionando_home(_):  # Define a função que será executada ao pressionar "HOME".
    # Exibe a mensagem "Você pressionou HOME!" no terminal.
    print("Você pressionou HOME!")

# Define outra funcionalidade personalizada que será executada quando a tecla "END" for pressionada.
@prompt.register_kb("end")  # Registra a tecla "END" para esta função.
def precionando_end(_):  # Define a função que será executada ao pressionar "END".
    # Exibe a mensagem "Você pressionou END!" no terminal.
    print("Você pressionou END!")

# Define outra funcionalidade personalizada que será executada quando a tecla "DELETE" for pressionada.
@prompt.register_kb("delete")  # Registra a tecla "DELETE" para esta função.
def precionando_delete(_):  # Define a função que será executada ao pressionar "DELETE".
    # Exibe a mensagem "Você pressionou DELETE!" no terminal.
    print("Você pressionou DELETE!")

# Executa o prompt no terminal, permitindo ao usuário digitar algo e usar as teclas personalizadas (HOME, END e DELETE).
result = prompt.execute()

