# Importa a biblioteca InquirerPy e os módulos necessários para criar menus interativos no terminal
from InquirerPy import inquirer
from InquirerPy.prompts.expand import ExpandChoice, ExpandHelp
from InquirerPy.separator import Separator

#Um prompt compacto com a capacidade de expandir e selecionar as opções disponíveis.
# Define uma lista de opções de frutas para o usuário escolher
opcoes_frutas = [
    ExpandChoice(key="m", name="Maçã", value="Maçã"),  # Opção "Maçã" com a tecla "m"
    ExpandChoice(key="c", name="Cereja", value="Cereja"),  # Opção "Cereja" com a tecla "c"
    ExpandChoice(key="l", name="Laranja", value="Laranja"),  # Opção "Laranja" com a tecla "l"
    ExpandChoice(key="p", name="Pêssego", value="Pêssego"),  # Opção "Pêssego" com a tecla "p"
    ExpandChoice(key="m", name="Melão", value="Melão"),  # Opção "Melão" com a tecla "m"
    ExpandChoice(key="e", name="Morango", value="Morango"),  # Opção "Morango" com a tecla "e"
    ExpandChoice(key="u", name="Uva", value="Uva"),  # Opção "Uva" com a tecla "u"
]

# Função para criar as opções de método de entrega, incluindo um separador visual
def opcoes_entrega(_):
    return [
        ExpandChoice(key="e", name="Entrega", value="entrega"),  # Opção "Entrega" com a tecla "e"
        ExpandChoice(key="r", name="Retirada", value="retirada"),  # Opção "Retirada" com a tecla "r"
        Separator(line="*" * 15),  # Adiciona um separador visual com asteriscos
        ExpandChoice(key="e", name="Estacionamento", value="estacionamento"),  # Opção "Estacionamento" com a tecla "e"
        ExpandChoice(key="t", name="Terceirizado", value="terceirizado"),  # Opção "Terceirizado" com a tecla "t"
    ]

# Função principal do programa
def main():
    # Solicita ao usuário que escolha sua fruta favorita
    fruta_selecionada = inquirer.expand(
        message="Escolha sua fruta favorita:",  # Mensagem exibida ao usuário
        choices=opcoes_frutas,                 # Lista de opções de frutas
        default="l",                           # Define "Laranja" como a opção padrão
    ).execute()  # Executa o menu e armazena a escolha do usuário

    # Solicita ao usuário que escolha seu método de entrega preferido
    metodo_selecionado = inquirer.expand(
        message="Selecione seu método de entrega preferido:",  # Mensagem exibida ao usuário
        choices=opcoes_entrega,                               # Lista de opções de entrega gerada pela função
        expand_help=ExpandHelp(key="h", message="Pressione 'h' para mais opções."),  # Mensagem de ajuda personalizada
    ).execute()  # Executa o menu e armazena a escolha do usuário

    # Exibe o resultado da escolha do usuário
    print(f"Você selecionou {fruta_selecionada} como sua fruta.")  # Exibe a fruta escolhida
    print(f"Você selecionou {metodo_selecionado} como seu método de entrega.")  # Exibe o método de entrega escolhido

# Verifica se o programa está sendo executado diretamente (e não importado como módulo)
if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
