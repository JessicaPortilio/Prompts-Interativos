# 1. Apresentação do InquirerPy
# O InquirerPy é uma biblioteca Python poderosa e flexível para criar prompts interativos no terminal. 
# Ele permite que desenvolvedores construam interfaces de linha de comando (CLI) amigáveis e intuitivas, com funcionalidades como:

# Entrada de texto.

# Seleção de opções.

# Confirmações (sim/não).

# E muito mais.

# Esses prompts são amplamente utilizados em ferramentas de interfaces de linha de comando (CLI), scripts de automação 
# e aplicações que exigem interação com o usuário.


# Quando trabalhamos com prompts interativos, 
# um problema comum surge ao tentar imprimir valores no terminal enquanto o prompt está ativo. Por exemplo:

# Se você usar a função print() padrão do Python durante a execução de um prompt, a saída pode:

# Interromper o layout do prompt.

# Causar comportamentos inesperados, como sobreposição de texto.

# Tornar a experiência do usuário confusa.

# Isso acontece porque o terminal não foi projetado para lidar com impressões simultâneas enquanto um prompt está em execução.

# 3. Então vamos falar sobre a função patched_print como solução para o problema para esse problema

# Para resolver esse problema, o InquirerPy oferece uma função especial patched_print. Essa função permite:

# Imprimir valores acima do prompt sem interromper sua execução.

# Manter a integridade do layout do terminal.

# E isso é  útil para depuração (debugging), onde você precisa exibir informações temporárias sem afetar a experiência do usuário.

# Essa função patched_print é uma versão adaptada da função print() do Python, 
# projetada para funcionar harmoniosamente com os prompts do InquirerPy.

# Exemplo Rápido

# Imagine que você está criando um prompt para coletar o nome do usuário e, 
# ao pressionar um atalho de teclado (como Alt + B), deseja exibir uma mensagem de depuração. 
# Com essa função patched_print, você podemos fazer isso sem interromper o prompt:



from InquirerPy.utils import patched_print
from InquirerPy import inquirer

prompt = inquirer.text(message="Name:")

@prompt.register_kb("alt-b")
def _(_):
    patched_print("Debug: Botão Alt + B pressionado!")

name = prompt.execute()




