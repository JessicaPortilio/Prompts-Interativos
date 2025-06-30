# 1. Introdução ao color_print

# color_print é uma função auxiliar fornecida pela biblioteca InquirerPy que permite a 
# impressão de mensagens coloridas no terminal. Esta função é particularmente útil em aplicações interativas 
# onde é necessário fornecer feedback visual ao usuário sem interromper a experiência do prompt.

# 2. Funcionamento do color_print

# A função color_print é inteligente o suficiente para detectar se o terminal está executando um prompt no momento da impressão. Se um 
# prompt estiver ativo, a mensagem colorida será impressa acima do prompt, sem interrompê-lo. Caso contrário, a mensagem será 
# simplesmente exibida no terminal.
#-------------------------------------------------------------------------------------------
# Parâmetros da Função

# formatted_text: Uma lista de tuplas, onde cada tupla contém uma string que define a classe de estilo e o texto a ser formatado.

# style: Um dicionário opcional que mapeia classes de estilo para códigos de cores ou estilos.

# 1 Exemplo
# Importa a função 'color_print' da biblioteca InquirerPy, que permite imprimir textos coloridos no terminal.
from InquirerPy.utils import color_print

# Utiliza a função 'color_print' para exibir a mensagem "Hello World" no terminal.
# O texto "Hello" será exibido em vermelho, e o texto "World" será exibido em azul.
color_print([("red", "Hello"), ("blue", " World")])


# 2 Exemplo
# Agora bora integrar com um Prompt de Texto, tá?

# Importa a função 'inquirer' da biblioteca InquirerPy, que permite criar prompts interativos no terminal.
from InquirerPy import inquirer

# Importa a função 'color_print' da biblioteca InquirerPy, que permite imprimir textos coloridos no terminal.
from InquirerPy.utils import color_print

# Cria um prompt interativo para solicitar ao usuário que digite seu nome.
prompt = inquirer.text(message="Digite seu nome:")

# Define um atalho de teclado "Alt + B" que, quando pressionado, imprime a mensagem "Olá Mundo" no terminal.
@prompt.register_kb("alt-b")
def _(_):
    # Exibe a mensagem "Olá Mundo" com cores personalizadas:
    # "Olá" será exibido em um tom amarelado (#e5c07b) e "Mundo" será branco (#ffffff).
    color_print([("#e5c07b", "Olá"), ("#ffffff", " Mundo")])

# Executa o prompt e armazena a resposta do usuário na variável 'name'.
name = prompt.execute()

# Exibe a mensagem "Bem-vindo" no terminal com a cor verde (#00ff00).
color_print([("class:aaa", "Bem-vindo")], style={"aaa": "#00ff00"})

# Exibe no terminal o nome digitado pelo usuário.
print(name)

# 3 Exemplo

# Importa a função 'color_print' da biblioteca InquirerPy, que permite imprimir textos coloridos no terminal.
from InquirerPy.utils import color_print

# Define uma função chamada 'imprimir_boas_vindas' que recebe um nome como parâmetro.
def imprimir_boas_vindas(nome):
    # Cria uma mensagem de boas-vindas personalizada usando cores diferentes para cada palavra.
    mensagem = [
        ("#FF5733", f"Bem-vindo(a), {nome} "),  # "Bem-vindo(a), [nome]" será exibido em laranja.
        ("#33FF57", "ao "),                     # "ao" será exibido em verde.
        ("#3357FF", "nosso "),                  # "nosso" será exibido em azul.
        ("#FF33A1", "sistema! ")                # "sistema!" será exibido em rosa.
    ]
    
    # Exibe a mensagem colorida no terminal.
    color_print(mensagem)

# Chama a função 'imprimir_boas_vindas' passando "Jessica" como nome de exemplo.
# Isso fará com que a mensagem colorida "Bem-vindo(a), Jessica ao nosso sistema!" seja exibida no terminal.
imprimir_boas_vindas('Jessica')


# A função color_print do InquirerPy é uma ferramenta poderosa para melhorar a interatividade 
# e a experiência do usuário em aplicações de terminal. Com ela, você pode facilmente 
# adicionar cores e estilos ao texto, proporcionando um feedback visual rico e contextual.