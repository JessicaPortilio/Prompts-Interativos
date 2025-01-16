# Importa a biblioteca InquirerPy para interagir com o usuário de forma simples
from InquirerPy import inquirer

# Define os atalhos de teclado personalizados para a interação com o usuário
keybindings = {
    "skip": [{"key": "c-c"}],       # Permite pular o prompt com Ctrl+C
    "interrupt": [{"key": "c-d"}],  # Interrompe com Ctrl+D
    "toggle-all": [{"key": "c-a"}]  # Seleciona todas as opções com Ctrl+A
}

try:
    # Cria uma pergunta de checkbox para o usuário escolher itens
    resultado = inquirer.checkbox(
        message="Escolha os itens:",        # A mensagem que será exibida para o usuário
        choices=["Item1", "Item2", "Item3"],  # Lista de itens que o usuário pode escolher
        keybindings=keybindings,            # Define os atalhos de teclado personalizados
    ).execute()  # Executa o prompt e armazena as escolhas do usuário na variável 'resultado'

    # Exibe os itens que o usuário selecionou
    print(f"Itens selecionados: {resultado}")

except KeyboardInterrupt:
    print("\nA operação foi interrompida com Ctrl+D.")
# except EOFError:
#     print("\nA operação foi interrompida com Ctrl+D.")





