# Importa a biblioteca 'inquirer' para criar prompts interativos
from InquirerPy import inquirer

# Solicita ao usuário que digite seu nome e armazena o valor na variável 'nome'
nome = inquirer.text(
    message="Digite seu nome:"  # Mensagem exibida para o usuário
).execute()  # Executa o prompt e retorna a resposta

# Solicita ao usuário que digite uma senha (em texto oculto) e armazena o valor na variável 'senha'
senha = inquirer.secret(
    message="Digite sua senha:"  # Mensagem exibida para o usuário
).execute()  # Executa o prompt e retorna a resposta

print(f"Senha: {'*' * len(senha)} (oculta por segurança)")  # Exibe a senha como asteriscos para segurança

# Como Selecionar Arquivos no Terminal com InquirerPy
# Solicita ao usuário que selecione um arquivo e armazena o caminho do arquivo na variável 'arquivo'
arquivo = inquirer.filepath(
    message="Selecione um arquivo:",  # Mensagem exibida para o usuário
    only_files=True  # Permite que o usuário selecione apenas arquivos, não pastas
).execute()  # Executa o prompt e retorna o caminho do arquivo selecionado

print(f"Arquivo selecionado: {arquivo}")  # Exibe o arquivo selecionado

# Como Criar um Prompt de Idade Personalizado em Python
# Solicita ao usuário que digite a idade, permitindo um valor entre 1 e 120 anos
idade = inquirer.number(
    message="Digite sua idade:",  # Mensagem exibida para o usuário
    min_allowed=1,  # Valor mínimo permitido (1)
    max_allowed=120,  # Valor máximo permitido (120)
).execute()  # Executa o prompt e retorna o valor informado

print(f"Idade: {idade}")  # Exibe a idade fornecida

# Solicita ao usuário que confirme os dados fornecidos (sim ou não)
confirmar = inquirer.confirm(
    message="Você confirma os dados fornecidos?",  # Mensagem exibida para o usuário
    default=True  # Valor padrão é 'Sim' (True)
).execute()  # Executa o prompt e retorna 'True' ou 'False' dependendo da escolha

# Solicita ao usuário que escolha sua cor favorita a partir de uma lista de opções
cor_favorita = inquirer.select(
    message="Escolha sua cor favorita:",  # Mensagem exibida para o usuário
    choices=["Vermelho", "Azul", "Verde", "Amarelo"],  # Opções de cores para o usuário escolher
).execute()  # Executa o prompt e retorna a cor escolhida

# Trabalhando com Inputs Interativos em Python"?

# Solicita ao usuário que escolha um dia da semana a partir de uma lista de opções
dia_da_semana = inquirer.rawlist(
    message="Escolha o dia da semana:",  # Mensagem exibida para o usuário
    choices=["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"],  # Opções de dias da semana
).execute()  # Executa o prompt e retorna o dia escolhido

print(f"Dia da semana: {dia_da_semana}")  # Exibe o dia da semana escolhido

# Solicita ao usuário que escolha uma opção a partir de um menu compacto com teclas de atalho
opcao = inquirer.expand(
    message="Escolha uma opção:",  # Mensagem exibida para o usuário
    choices=[  # Opções de escolha com teclas de atalho
        {"key": "a", "name": "Adicionar", "value": "add"},
        {"key": "r", "name": "Remover", "value": "remove"},
        {"key": "s", "name": "Sair", "value": "exit"},
    ],
).execute()  # Executa o prompt e retorna a opção escolhida

# Solicita ao usuário que selecione seus interesses a partir de uma lista de opções
interesses = inquirer.checkbox(
    message="Selecione seus interesses:",  # Mensagem exibida para o usuário
    choices=["Esportes", "Música", "Tecnologia", "Viagem"],  # Opções de interesses
).execute()  # Executa o prompt e retorna uma lista de interesses selecionados

# Solicita ao usuário que escolha uma linguagem de programação preferida usando busca por sugestão
linguagem = inquirer.fuzzy(
    message="Qual linguagem você prefere?",  # Mensagem exibida para o usuário
    choices=["Python", "Java", "JavaScript", "C++", "C#", "Ruby", "Go"],  # Opções de linguagens de programação
).execute()  # Executa o prompt e retorna a linguagem escolhida

# Exibe todos os resultados fornecidos pelo usuário, com alguns valores ocultos (como a senha)
print("\n--- Resultados ---")
print(f"Nome: {nome}")  # Exibe o nome fornecido
print(f"Senha: {'*' * len(senha)} (oculta por segurança)")  # Exibe a senha como asteriscos para segurança
print(f"Arquivo selecionado: {arquivo}")  # Exibe o arquivo selecionado
print(f"Idade: {idade}")  # Exibe a idade fornecida
print(f"Confirmação: {'Sim' if confirmar else 'Não'}")  # Exibe se os dados foram confirmados (Sim ou Não)
print(f"Cor favorita: {cor_favorita}")  # Exibe a cor favorita escolhida
print(f"Dia da semana: {dia_da_semana}")  # Exibe o dia da semana escolhido
print(f"Opção escolhida: {opcao}")  # Exibe a opção escolhida no menu
print(f"Interesses: {', '.join(interesses)}")  # Exibe os interesses selecionados, separados por vírgula
print(f"Linguagem preferida: {linguagem}")  # Exibe a linguagem preferida escolhida
