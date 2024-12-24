# Importa o módulo `inquirer` da biblioteca `InquirerPy`, que permite criar prompts interativos no terminal.
from InquirerPy import inquirer

# Importa uma versão especial do comando `print`, chamada `patched_print`, que é compatível com os prompts interativos da biblioteca.
from InquirerPy.utils import patched_print as print

# Cria um prompt de entrada de texto que exibe a mensagem "Digite algo:" no terminal.
prompt = inquirer.text(message="Digite algo:")

# Adiciona uma funcionalidade personalizada ao prompt para capturar a combinação de teclas "CTRL + seta para a esquerda".
@prompt.register_kb("c-left")  # Registra a combinação de teclas "CTRL+Left" para esta função.
def handle_ctrl_left(_):  # Define a função que será executada ao pressionar "CTRL + Left".
    # Exibe a mensagem "Você pressionou CTRL+Left!" no terminal.
    print("Você pressionou CTRL+Left!")

# Adiciona outra funcionalidade personalizada ao prompt para capturar a combinação de teclas "CTRL + seta para a direita".
@prompt.register_kb("c-right")  # Registra a combinação de teclas "CTRL+Right" para esta função.
def handle_ctrl_right(_):  # Define a função que será executada ao pressionar "CTRL + Right".
    # Exibe a mensagem "Você pressionou CTRL+Right!" no terminal.
    print("Você pressionou CTRL+Right!")

# Executa o prompt interativo, permitindo que o usuário digite algo ou pressione as combinações de teclas personalizadas.
result = prompt.execute()



