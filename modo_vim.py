# O modo Vim é uma funcionalidade que permite ao usuário interagir 
# com o prompt de entrada utilizando comandos inspirados 
# no editor de texto Vim

# Importa a biblioteca InquirerPy para interagir com o usuário de forma simples
from InquirerPy import inquirer

resultado = inquirer.select(
    message="Escolha um item:",
    choices=["Opção 1", "Opção 2", "Opção 3"],
    vi_mode=True  # Ativa o modo VIM
).execute()

# Modo VIM: Permite navegar, selecionar opções e realizar outras ações com atalhos de teclado, como:
# j para mover para baixo.
# k para mover para cima.
# Enter para confirmar a escolha.
# (ao invés de usar as setas do teclado)

print(f"Você escolheu: {resultado}")
