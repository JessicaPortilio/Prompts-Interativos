# https://inquirerpy.readthedocs.io/en/latest/pages/style.html
from InquirerPy import prompt  # Importa a biblioteca InquirerPy para criar perguntas interativas no terminal
from InquirerPy.base.control import Choice  # Importa a classe Choice para personalizar opções de escolha

# Define o estilo personalizado como um dicionário
style = {
    "questionmark": "#249486",  # Cor do símbolo "?" que aparece ao lado das perguntas
    "answermark": "#6e87c7",  # Cor do símbolo que indica a resposta concluída
    "answer": "#61afef",  # Cor usada para exibir a resposta do usuário
    "input": "#98c379",  # Cor do texto digitado pelo usuário
    "question": "#783c70",  # Cor do texto da pergunta
    "answered_question": "#221954",  # Cor do texto de perguntas já respondidas
    "instruction": "#0e5835",  # Cor das instruções curtas exibidas para o usuário
    "long_instruction": "#b4ce48",  # Cor das instruções mais longas
    "pointer": "#7019d2",  # Cor do indicador que mostra a opção selecionada
    "checkbox": "#98c379",  # Cor dos itens de seleção múltipla (checkbox)
    "separator": "#bd6674",  # Cor dos separadores visuais entre opções
    "skipped": "#900e23",  # Cor para perguntas que foram puladas
    "validator": "#ff029a",  # Cor para mensagens de erro ao validar entradas do usuário
    "marker": "#ca9411",  # Cor para símbolos de destaque, como obrigatoriedade
    "fuzzy_prompt": "#c678dd",  # Cor do texto inicial em uma busca fuzzy
    "fuzzy_info": "#024aff",  # Cor das informações adicionais na busca fuzzy
    "fuzzy_border": "#5b1414",  # Cor da borda do componente fuzzy
    "fuzzy_match": "#c678dd",  # Cor das palavras destacadas em uma busca fuzzy
    "spinner_pattern": "#e5c07b",  # Cor do padrão de carregamento (spinner)
    "spinner_text": "#b4185a",  # Cor do texto exibido durante o carregamento
}

# Lista de perguntas que serão feitas ao usuário
questions = [
    {
        "type": "input",  # Tipo da pergunta: entrada de texto
        "message": "Digite seu nome:",  # Mensagem exibida ao usuário
        "name": "input",  # Nome da resposta que será armazenada
        "instruction": "Exemplo de input colorido.",  # Instrução adicional para o usuário
    },
    {
        "type": "input",  # Outra pergunta do tipo entrada de texto
        "message": "Digite a resposta da pergunta:",  # Mensagem da pergunta
        "name": "questionmark",  # Nome da resposta
    },
    {
        "type": "list",  # Tipo da pergunta: lista de opções
        "message": "Escolha uma opção (Exemplo de pointer):",  # Mensagem da pergunta
        "choices": ["Opção 1", "Opção 2", "Opção 3"],  # Lista de opções para o usuário escolher
        "name": "pointer",  # Nome da resposta
    },
    {
        "type": "checkbox",  # Tipo da pergunta: seleção múltipla
        "message": "Selecione opções (Exemplo de checkbox):",  # Mensagem da pergunta
        "choices": [
            Choice("Item 1"),  # Primeira opção da lista
            Choice("Item 2"),  # Segunda opção
            Choice("Item 3"),  # Terceira opção
        ],
        "name": "checkbox",  # Nome da resposta
    },
    {
        "type": "list",  # Outra pergunta do tipo lista
        "message": "Escolha uma opção (Exemplo de answered_question):",  # Mensagem da pergunta
        "choices": ["Sim", "Não"],  # Opções da lista
        "name": "answered_question",  # Nome da resposta
    },
    {
        "type": "input",  # Pergunta do tipo entrada de texto
        "message": "Escreva algo (Exemplo de marker):",  # Mensagem da pergunta
        "name": "marker",  # Nome da resposta
        "instruction": "Este campo é obrigatório.",  # Instrução adicional para o usuário
    },
    {
        "type": "fuzzy",  # Tipo da pergunta: busca fuzzy (filtra opções enquanto o usuário digita)
        "message": "Escolha uma cidade (Exemplo de fuzzy_prompt):",  # Mensagem da pergunta
        "choices": ["Paris", "Nova York", "Londres", "Tóquio"],  # Lista de opções disponíveis
        "name": "fuzzy",  # Nome da resposta
    },
    {
        "type": "input",  # Outra pergunta do tipo entrada de texto
        "message": "Validação de entrada (Exemplo de validator):",  # Mensagem da pergunta
        "name": "validator",  # Nome da resposta
        "validate": lambda x: len(x) > 3 or "A entrada deve ter mais de 3 caracteres.",  # Validação personalizada para entrada
    },
    {
        "type": "list",  # Pergunta do tipo lista com separador visual
        "message": "Exemplo de separator e spinner:",  # Mensagem da pergunta
        "choices": [
            Choice("Opção A"),  # Primeira opção da lista
            {"name": "---", "value": None, "disabled": True},  # Separador visual
            Choice("Opção B"),  # Segunda opção da lista
        ],
        "name": "separator_spinner",  # Nome da resposta
    },
]

# Exibe as perguntas ao usuário e coleta as respostas
answers = prompt(questions, style=style)

# Exibe as respostas coletadas
print("\nRespostas:")  # Mensagem introdutória
for key, value in answers.items():  # Percorre cada resposta coletada
    print(f"{key}: {value}")  # Exibe o nome da pergunta e a resposta correspondente
