# Importa o módulo `inquirer` da biblioteca `InquirerPy`, que permite criar prompts interativos no terminal.
from InquirerPy import inquirer

# Importa uma versão especial do comando `print` chamada `patched_print`, que funciona bem com os prompts da biblioteca.
from InquirerPy.utils import patched_print as print

# Cria um prompt de entrada de texto que exibe a mensagem "Digite algo:" no terminal.
prompt = inquirer.text(message="Digite algo:")

# Adiciona uma funcionalidade personalizada para o prompt: 
# executa uma ação quando a tecla "seta para cima" (UP) é pressionada.
@prompt.register_kb("up")  # Registra a tecla "seta para cima" para esta função.
def precionando_up(_):  # Define a função que será chamada ao pressionar a tecla.
    # Exibe uma mensagem no terminal informando que a seta para cima foi pressionada.
    print("Você pressionou a seta para CIMA!")

# Adiciona outra funcionalidade personalizada para o prompt: 
# executa uma ação quando a tecla "seta para baixo" (DOWN) é pressionada.
@prompt.register_kb("down")  # Registra a tecla "seta para baixo" para esta função.
def precionando_down(_):  # Define a função que será chamada ao pressionar a tecla.
    # Exibe uma mensagem no terminal informando que a seta para baixo foi pressionada.
    print("Você pressionou a seta para BAIXO!")

# Executa o prompt no terminal. 
# Permite que o usuário insira texto e interaja com as funcionalidades personalizadas para as teclas.
result = prompt.execute()

