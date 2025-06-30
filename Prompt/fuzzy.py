# 1. O que é o fuzzy?
# O fuzzy é um tipo de prompt interativo que permite ao usuário buscar opções de maneira aproximada ao digitar, utilizando correspondência difusa (fuzzy matching).
# ✅ Ideal para listas longas ou quando o usuário não tem certeza do nome exato da opção.
# ✅ O usuário pode digitar uma parte do texto e o fuzzy tentará encontrar a correspondência mais próxima.

# 2. Como usar o fuzzy?
# Aqui está um exemplo básico onde o usuário escolhe um filme, mas pode digitar parte do nome para facilitar a busca:

# Importa a função `prompt` da biblioteca InquirerPy, que permite criar perguntas interativas no terminal
from InquirerPy import prompt

# Define uma lista contendo um dicionário com as configurações da pergunta
pergunta = [
    {
        "type": "fuzzy",  # Define o tipo de entrada como "fuzzy", permitindo sugestões de auto preenchimento baseadas na digitação do usuário
        "name": "filme",  # Define o nome da resposta que será armazenada no dicionário de retorno
        "message": "Escolha um filme:",  # Define a mensagem exibida ao usuário no terminal
        "choices": [  # Lista de opções disponíveis para o usuário escolher
            "O Senhor dos Anéis",
            "Matrix",
            "Star Wars",
            "Titanic",
            "Vingadores",
            "O Jogo da Imitação",
        ],
    }
]

# Exibe a pergunta ao usuário e armazena a resposta na variável `resposta`
resposta = prompt(pergunta)

# Exibe no terminal o filme escolhido pelo usuário
print(f"Filme escolhido: {resposta['filme']}")


# 3. Exemplo Completo: Busca de Cidades
# O que vamos implementar:

# Busca fuzzy mais robusta: Permitir que o usuário encontre cidades mesmo com erros de digitação ou letras faltando.

# Validação de entrada: Garantir que o usuário selecione uma cidade válida da lista.

# Feedback visual: Mostrar sugestões em tempo real enquanto o usuário digita.

# Expansão da lista de cidades: Adicionar mais cidades para tornar a busca mais interessante.

# Interface mais amigável: Adicionar cores ou emojis para melhorar a experiência do usuário.

# Importa a função 'prompt' da biblioteca 'InquirerPy', que é usada para criar interfaces de perguntas no terminal.
# Essa função permite que o programa faça perguntas interativas ao usuário.
from InquirerPy import prompt

# Importa a função 'process' da biblioteca 'fuzzywuzzy', que é usada para fazer buscas aproximadas (fuzzy matching).
# A busca fuzzy permite encontrar correspondências mesmo quando o texto digitado pelo usuário contém erros ou está incompleto.
from fuzzywuzzy import process  # Para busca fuzzy mais robusta

# Lista de cidades disponíveis para busca.
# Essa lista contém os nomes das cidades que o programa reconhece.
CIDADES = [
    "São Paulo",
    "Rio de Janeiro",
    "Belo Horizonte",
    "Curitiba",
    "Porto Alegre",
    "Salvador",
    "Fortaleza",
    "Recife",
    "Manaus",
    "Belém",
    "Brasília",
    "Goiânia",
    "Florianópolis",
    "Vitória",
    "Natal",
    "João Pessoa",
    "Maceió",
    "Campo Grande",
    "Cuiabá",
    "Teresina",
]

# Função para buscar a cidade mais próxima da entrada do usuário usando fuzzy matching.
def buscar_cidade(nome):
    """Busca a cidade mais próxima na lista usando fuzzy matching."""
    # Verifica se o nome não está vazio após o pré-processamento.
    # O método 'strip()' remove espaços em branco no início e no fim do texto.
    if not nome.strip():
        return None  # Retorna 'None' se o texto estiver vazio.

    # Usa fuzzy matching para encontrar a cidade mais próxima.
    # A função 'process.extractOne' compara o texto digitado pelo usuário com a lista de cidades
    # e retorna a cidade mais parecida (com a maior pontuação de similaridade).
    resultado, _ = process.extractOne(nome, CIDADES)

    # Retorna a cidade encontrada.
    return resultado

# Função principal do programa.
def main():
    # Cria um loop infinito para permitir que o usuário tente novamente caso a cidade não seja encontrada ou ele não confirme a escolha.
    while True:
        # Pergunta para o usuário digitar o nome de uma cidade.
        pergunta = [
            {
                "type": "input",  # Tipo de pergunta: entrada de texto.
                "name": "cidade",  # Nome da resposta (será usada como chave no dicionário de respostas).
                "message": "Digite o nome de uma cidade:",  # Mensagem exibida para o usuário.
            }
        ]

        # Exibe a pergunta ao usuário e armazena a resposta.
        # A função 'prompt' exibe a pergunta e retorna um dicionário com a resposta do usuário.
        resposta = prompt(pergunta)

        # Remove espaços em branco no início e no fim do texto digitado pelo usuário.
        cidade_digitada = resposta["cidade"].strip()

        # Busca a cidade mais próxima da entrada do usuário usando a função 'buscar_cidade'.
        cidade_encontrada = buscar_cidade(cidade_digitada)

        # Verifica se a cidade foi encontrada.
        if cidade_encontrada:
            # Pergunta para confirmar se a cidade encontrada é a que o usuário queria.
            pergunta_confirmacao = [
                {
                    "type": "confirm",  # Tipo de pergunta: confirmação (sim/não).
                    "name": "confirmar",  # Nome da resposta (será usada como chave no dicionário de respostas).
                    "message": f"Você quis dizer {cidade_encontrada}?",  # Mensagem exibida para o usuário, mostrando a cidade encontrada.
                    "default": True,  # Valor padrão da confirmação (sim/não). Aqui, "sim" é o padrão.
                }
            ]

            # Exibe a pergunta de confirmação ao usuário e armazena a resposta.
            confirmacao = prompt(pergunta_confirmacao)

            # Verifica se o usuário confirmou a cidade encontrada.
            if confirmacao["confirmar"]:
                # Se confirmou, exibe a cidade escolhida e encerra o loop.
                print(f"\nCidade escolhida: {cidade_encontrada} 🌆")
                break
            else:
                # Se não confirmou, exibe uma mensagem e volta ao início do loop para tentar novamente.
                print("Tente novamente!\n")
        else:
            # Se a cidade não foi encontrada, exibe uma mensagem e volta ao início do loop para tentar novamente.
            print("Cidade não encontrada. Tente novamente!\n")

# Verifica se o script está sendo executado diretamente (não importado como módulo).
if __name__ == "__main__":
    # Chama a função principal para iniciar o programa.
    main()