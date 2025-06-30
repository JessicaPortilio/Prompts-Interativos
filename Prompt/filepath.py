#1.  O que é o prompt filepath?
# O prompt filepath permite que o usuário digite ou selecione um arquivo ou diretório no terminal.
# Ele é útil para situações como:
# ✅ Pedir ao usuário para escolher um arquivo de entrada.
# ✅ Selecionar um diretório onde um arquivo será salvo.
# ✅ Garantir que o caminho inserido seja válido.

# 2. Como usar o filepath prompt?
# Aqui está um exemplo simples onde o usuário seleciona um arquivo:

# Importa a função 'prompt' da biblioteca InquirerPy, que é usada para criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista chamada 'pergunta' contendo um dicionário com as configurações da pergunta.
pergunta = [
    {
        "type": "filepath",  # Define o tipo da pergunta como 'filepath', permitindo selecionar um arquivo no sistema.
        "name": "arquivo",  # Nome da variável onde a resposta será armazenada.
        "message": "Digite ou selecione o caminho do arquivo:",  # Mensagem que será exibida ao usuário.
    }
]

# Exibe a pergunta ao usuário e armazena a resposta na variável 'resposta'.
resposta = prompt(pergunta)

# Exibe a resposta no terminal, mostrando o caminho do arquivo escolhido pelo usuário.
print(f"Você escolheu o arquivo: {resposta['arquivo']}")

# "type": "filepath" → Especifica que este prompt aceita caminhos de arquivos.
# O usuário pode digitar o caminho manualmente ou navegar pelos diretórios.

# 3. Permitir Apenas Arquivos ou Diretórios
# Se quisermos restringir a entrada apenas para arquivos ou apenas para pastas, usamos o parâmetro only_files.

# Importa a função 'prompt' da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Define uma lista chamada 'pergunta' contendo um dicionário com as configurações da pergunta.
pergunta = [
    {
        "type": "filepath",  # Define que a pergunta permitirá a seleção de um arquivo do sistema.
        "name": "arquivo",  # Nome da variável onde a resposta (o caminho do arquivo escolhido) será armazenada.
        "message": "Escolha um arquivo:",  # Mensagem exibida para o usuário ao fazer a pergunta.
        "only_files": True,  # Restringe a seleção apenas para arquivos, impedindo a escolha de diretórios.
    }
]

# Exibe a pergunta no terminal e armazena a resposta na variável 'resposta'.
resposta = prompt(pergunta)

# Exibe o caminho do arquivo escolhido pelo usuário no terminal.
print(f"Arquivo selecionado: {resposta['arquivo']}")

# "only_files": True → O usuário só pode selecionar arquivos, não pastas.


# 4. Validando se o Arquivo Existe
import os
from InquirerPy import prompt

# Define a pergunta que será feita ao usuário.
pergunta = [
    {
        "type": "filepath",  # Tipo de pergunta: caminho de arquivo.
        "name": "arquivo",   # Nome da resposta (será armazenada em resposta['arquivo']).
        "message": "Digite o caminho do arquivo:",  # Mensagem exibida ao usuário.
    }
]

# Entra em um loop infinito para pedir o caminho do arquivo até que um caminho válido seja fornecido.
while True:
    # Faz a pergunta ao usuário e armazena a resposta.
    resposta = prompt(pergunta)

    # Verifica se o caminho digitado pelo usuário existe no sistema de arquivos.
    if os.path.exists(resposta['arquivo']):
        # Se o caminho existir, imprime uma mensagem de sucesso e sai do loop.
        print(f"Arquivo encontrado: {resposta['arquivo']}")
        break
    else:
        # Se o caminho não existir, exibe uma mensagem de erro e pede para tentar novamente.
        print("Erro: O caminho do arquivo não existe! Tente novamente.")

# 5. Definir um Caminho Padrão
# Podemos sugerir um caminho padrão para facilitar a escolha do usuário:

# Define a pergunta que será feita ao usuário.
pergunta = [
    {
        "type": "filepath",  # Tipo de pergunta: caminho de arquivo.
        "name": "arquivo",   # Nome da resposta (será armazenada em resposta['arquivo']).
        "message": "Digite o caminho do arquivo:",  # Mensagem exibida ao usuário.
        "default": "C:\\Aulas_Prompts_Interativos_Em_Python\\Prompt\\secret.py" # Passando como Padrão o caminho sugerido
    }
]

# Entra em um loop infinito para pedir o caminho do arquivo até que um caminho válido seja fornecido.
while True:
    # Faz a pergunta ao usuário e armazena a resposta.
    resposta = prompt(pergunta)

    # Verifica se o caminho digitado pelo usuário existe no sistema de arquivos.
    if os.path.exists(resposta['arquivo']):
        # Se o caminho existir, imprime uma mensagem de sucesso e sai do loop.
        print(f"Arquivo encontrado: {resposta['arquivo']}")
        break
    else:
        # Se o caminho não existir, exibe uma mensagem de erro e pede para tentar novamente.
        print("Erro: O caminho do arquivo não existe! Tente novamente.")

# O terminal já abre com um caminho sugerido.
# O usuário pode aceitar ou editar esse caminho.

# 6. Customizando a Interface
# Podemos estilizar o prompt para deixá-lo mais bonito:

# Importa a função 'prompt' da biblioteca InquirerPy, que permite criar perguntas interativas no terminal.
from InquirerPy import prompt

# Definindo um estilo personalizado para modificar as cores e o formato das mensagens no terminal
custom_style = {
    "questionmark": "fg:#4B0082 bold",  # Define a cor roxa escura e negrito para o ponto de interrogação "?" antes da pergunta.
    "question": "fg:#191970 bold",  # Define a cor azul escura e negrito para o texto da pergunta exibida ao usuário.
    "answer": "fg:#FF1493 bold",  # Define a cor rosa choque e negrito para a resposta digitada pelo usuário.
}

# Cria uma lista contendo um dicionário que configura a pergunta interativa
pergunta = [
    {
        "type": "filepath",  # Define o tipo da pergunta como 'filepath', permitindo que o usuário escolha um arquivo no sistema.
        "name": "arquivo",  # Nome da variável onde será armazenado o caminho do arquivo selecionado.
        "message": "Escolha um arquivo:",  # Mensagem exibida ao usuário para solicitar a escolha de um arquivo.
    }
]

# Exibe a pergunta no terminal com o estilo personalizado e armazena a resposta na variável 'resposta'.
resposta = prompt(pergunta, style=custom_style)

# Exibe no terminal o caminho do arquivo selecionado pelo usuário.
print(f"Arquivo selecionado: {resposta['arquivo']}")

# 7.  Exemplo Completo: Abrindo um Arquivo Escolhido
# Podemos usar o caminho escolhido para abrir e ler um arquivo:

# Importa a função 'prompt' da biblioteca 'InquirerPy', que é usada para criar perguntas interativas no terminal.
from InquirerPy import prompt

# Importa a biblioteca 'os', que permite interagir com o sistema operacional, como verificar se um arquivo existe ou abrir arquivos.
import os

# Importa a biblioteca 'subprocess', que permite executar comandos do sistema operacional, como abrir arquivos com programas padrão.
import subprocess

# Define a pergunta que será feita ao usuário.
pergunta = [
    {
        "type": "filepath",  # Tipo de pergunta: caminho de arquivo.
        "name": "arquivo",   # Nome da resposta (será armazenada em resposta['arquivo']).
        "message": "Escolha um arquivo para abrir:",  # Mensagem exibida ao usuário.
        "only_files": True,  # Permite apenas a seleção de arquivos, não diretórios.
    }
]

# Faz a pergunta ao usuário e armazena a resposta na variável 'resposta'.
resposta = prompt(pergunta)

# Obtém o caminho do arquivo digitado pelo usuário a partir da resposta.
caminho_arquivo = resposta["arquivo"]

# Verifica se o arquivo existe no sistema de arquivos.
if not os.path.exists(caminho_arquivo):
    # Se o arquivo não existir, exibe uma mensagem de erro.
    print(f"Erro: O arquivo '{caminho_arquivo}' não existe!")
else:
    # Se o arquivo existir, tenta abri-lo com o programa padrão do sistema operacional.
    try:
        # Verifica se o sistema operacional é Windows.
        if os.name == "nt":  # 'nt' é o nome interno do Windows.
            # Abre o arquivo com o programa padrão do Windows.
            os.startfile(caminho_arquivo)
        # Verifica se o sistema operacional é Linux ou macOS.
        elif os.name == "posix":  # 'posix' é o nome interno de sistemas Unix-like (Linux/macOS).
            # Abre o arquivo com o comando 'xdg-open', que usa o programa padrão no Linux/macOS.
            subprocess.run(["xdg-open", caminho_arquivo])
        else:
            # Se o sistema operacional não for reconhecido, exibe uma mensagem de erro.
            print("Sistema operacional não suportado.")
    except Exception as e:
        # Se ocorrer algum erro ao tentar abrir o arquivo, exibe uma mensagem de erro.
        print(f"Erro ao abrir o arquivo: {e}")

# Outra forma de abrir o arquivo, lendo seu conteúdo e exibindo no terminal antes de abrir com o programa padrão.
try:
    # Abre o arquivo no modo de leitura ('r') com codificação UTF-8.
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        # Lê todo o conteúdo do arquivo e armazena na variável 'conteudo'.
        conteudo = f.read()
        # Exibe uma mensagem indicando que o conteúdo do arquivo será mostrado.
        print("\nConteúdo do arquivo:\n")
        # Exibe o conteúdo do arquivo no terminal.
        print(conteudo)
        # Tenta abrir o arquivo com o programa padrão do Windows (se for Windows).
        os.startfile(caminho_arquivo)
except Exception as e:
    # Se ocorrer algum erro ao tentar ler ou abrir o arquivo, exibe uma mensagem de erro.
    print(f"Erro ao abrir o arquivo: {e}")
    
# Como funciona:
# O usuário escolhe um arquivo usando a interface interativa do InquirerPy.

# O programa verifica se o arquivo existe.

# Se o arquivo existir, ele é aberto com o programa padrão do sistema operacional.

# Em seguida, o conteúdo do arquivo é lido e exibido no terminal.

# Se ocorrer algum erro, uma mensagem de erro é exibida.


# Resumo da Aula
# ✅ O prompt filepath permite que o usuário selecione arquivos ou pastas.
# ✅ Podemos restringir a entrada para apenas arquivos ou apenas diretórios.
# ✅ Podemos validar se o caminho existe.
# ✅ Um caminho padrão pode ser sugerido.
# ✅ O estilo do prompt pode ser customizado.
# ✅ Podemos abrir o arquivo escolhido pelo usuário.