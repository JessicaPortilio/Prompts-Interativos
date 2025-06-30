# 1. O que é o checkbox?
# O checkbox permite que o usuário selecione múltiplas opções de uma lista.
# ✅ O usuário pode marcar/desmarcar opções usando a barra de espaço.
# ✅ Ideal para selecionar múltiplos itens antes de confirmar.
# ✅ O resultado final será uma lista de valores selecionados.

# 📌 Quando usar?

# Escolha de preferências (ex: gêneros musicais, categorias de produtos).
# Seleção de múltiplos arquivos para uma ação.
# Listagem de opções obrigatórias e opcionais em um formulário.


# 2. Como usar o checkbox?
# Aqui está um exemplo básico onde o usuário escolhe suas linguagens favoritas:

# Importa a função `prompt` da biblioteca InquirerPy, que permite criar perguntas interativas no terminal
from InquirerPy import prompt

# Define uma lista contendo um dicionário que representa uma pergunta interativa
pergunta = [
    {
        "type": "checkbox",  # Define o tipo da pergunta como checkbox (múltipla escolha)
        "name": "linguagens",  # Nome da variável onde as respostas selecionadas serão armazenadas
        "message": "Quais linguagens de programação você conhece?",  # Pergunta que será exibida no terminal
        "choices": [  # Lista de opções que o usuário pode selecionar
            "Python",     # Primeira opção disponível
            "JavaScript", # Segunda opção disponível
            "Java",       # Terceira opção disponível
            "C++",        # Quarta opção disponível
            "Go",         # Quinta opção disponível
            "Ruby",       # Sexta opção disponível
        ],
    }
]

# Exibe a pergunta no terminal e armazena a resposta do usuário na variável `resposta`
resposta = prompt(pergunta)

# Exibe no terminal a lista de linguagens que o usuário escolheu
print(f"Linguagens escolhidas: {resposta['linguagens']}")


# 3. Adicionando Valores Padrão, Use enabled nas escolhas
# Podemos definir explicitamente as opções como marcadas usando a chave "enabled" nas escolhas:

# Importa a função `prompt` da biblioteca InquirerPy, que permite criar interfaces interativas no terminal
from InquirerPy import prompt

# Define uma lista contendo um dicionário que representa uma pergunta para o usuário
pergunta = [
    {
        "type": "checkbox",  # Define o tipo de entrada como uma lista de seleção múltipla (checkbox)
        "name": "ferramentas",  # Nome da variável que armazenará a resposta
        "message": "Quais ferramentas você usa?",  # Mensagem exibida para o usuário
        "choices": [  # Lista de opções disponíveis para seleção
            {"name": "Docker", "value": "docker", "enabled": True},  # Opção pré-selecionada (enabled=True)
            {"name": "Git", "value": "git", "enabled": True},  # Outra opção pré-selecionada
            {"name": "Kubernetes", "value": "kubernetes"},  # Opção disponível, mas não pré-selecionada
            {"name": "Jenkins", "value": "jenkins"},  # Outra opção disponível sem pré-seleção
        ],
    }
]

# Exibe a pergunta ao usuário e armazena a resposta em um dicionário chamado `resposta`
resposta = prompt(pergunta)

# Exibe a resposta do usuário no terminal, mostrando as ferramentas escolhidas
print(f"Ferramentas escolhidas: {resposta['ferramentas']}")


# 4. Criando Grupos com Separator
# Podemos agrupar opções separando-as com Separator:

from InquirerPy import prompt  # Importa a função 'prompt' da biblioteca InquirerPy para interagir com o usuário no terminal
from InquirerPy.separator import Separator  # Importa a classe 'Separator' para criar divisores visuais nas opções

# Define a pergunta que será exibida ao usuário
pergunta = [
    {
        "type": "checkbox",  # Tipo de entrada: lista de seleção múltipla (checkbox)
        "name": "tecnologias",  # Nome da resposta, usado como chave para armazenar os dados
        "message": "Escolha suas tecnologias favoritas:",  # Mensagem que será exibida para o usuário
        "choices": [  # Lista de opções disponíveis para escolha
            Separator("-- Linguagens --"),  # Adiciona um separador com o título "Linguagens"
            {"name": "Python", "value": "python"},  # Opção para Python
            {"name": "JavaScript", "value": "javascript"},  # Opção para JavaScript
            {"name": "C++", "value": "c++"},  # Opção para C++
            Separator("-- Bancos de Dados --"),  # Adiciona um separador com o título "Bancos de Dados"
            {"name": "PostgreSQL", "value": "postgresql"},  # Opção para PostgreSQL
            {"name": "MongoDB", "value": "mongodb"},  # Opção para MongoDB
            {"name": "MySQL", "value": "mysql"},  # Opção para MySQL
        ],
    }
]

resposta = prompt(pergunta)  # Exibe a pergunta ao usuário e armazena a resposta na variável 'resposta'
print(f"Tecnologias escolhidas: {resposta['tecnologias']}")  # Exibe a lista de tecnologias escolhidas pelo usuário

# 5. Exemplo Completo: Personalizando um Pedido de Pizza

from InquirerPy import prompt  # Biblioteca para criar perguntas interativas no terminal
from InquirerPy.validator import EmptyInputValidator  # Validador para impedir respostas vazias
from InquirerPy.separator import Separator  # Permite adicionar separadores visuais nas listas de opções

# Dicionário contendo os preços de cada tamanho de pizza
PRECOS_TAMANHO = {
    "pequena": 25.00,  # Preço da pizza pequena
    "media": 35.00,  # Preço da pizza média
    "grande": 45.00,  # Preço da pizza grande
}

# Dicionário contendo os preços para cada tipo de massa
PRECOS_MASSA = {
    "fina": 0.00,  # Massa fina não tem custo adicional
    "grossa": 5.00,  # Massa grossa custa R$ 5,00 a mais
    "integral": 7.00,  # Massa integral custa R$ 7,00 a mais
}

def escolher_pizza():
    """Função que permite ao usuário escolher o tamanho, tipo de massa e ingredientes da pizza."""
    while True:
        # Pergunta ao usuário qual tamanho de pizza ele deseja
        pergunta_tamanho = [
            {
                "type": "list",  # Tipo de pergunta: lista de opções
                "name": "tamanho",  # Nome da resposta que será armazenada
                "message": "Escolha o tamanho da sua pizza:",  # Mensagem exibida ao usuário
                "choices": [  # Lista de opções disponíveis
                    {"name": f"Pequena 🍕 - R$ {PRECOS_TAMANHO['pequena']:.2f}", "value": "pequena"},
                    {"name": f"Média 🍕🍕 - R$ {PRECOS_TAMANHO['media']:.2f}", "value": "media"},
                    {"name": f"Grande 🍕🍕🍕 - R$ {PRECOS_TAMANHO['grande']:.2f}", "value": "grande"},
                ],
                "default": "media",  # Opção pré-selecionada
            }
        ]

        # Pergunta sobre o tipo de massa
        pergunta_massa = [
            {
                "type": "list",  # Tipo de pergunta: lista de opções
                "name": "massa",  # Nome da resposta armazenada
                "message": "Escolha o tipo de massa:",  # Mensagem exibida ao usuário
                "choices": [
                    {"name": f"Fina 🍕 - R$ {PRECOS_MASSA['fina']:.2f}", "value": "fina"},
                    {"name": f"Grossa 🍕 - R$ {PRECOS_MASSA['grossa']:.2f}", "value": "grossa"},
                    {"name": f"Integral 🍕 - R$ {PRECOS_MASSA['integral']:.2f}", "value": "integral"},
                ],
                "default": "fina",  # Opção pré-selecionada
            }
        ]

        # Pergunta sobre os ingredientes da pizza
        pergunta_ingredientes = [
            {
                "type": "checkbox",  # Tipo de pergunta: múltipla escolha
                "name": "ingredientes",  # Nome da resposta armazenada
                "message": "Escolha os ingredientes da sua pizza:",  # Mensagem exibida ao usuário
                "choices": [
                    {"name": "Queijo extra 🧀", "value": "queijo", "enabled": True},  # Habilitado por padrão
                    {"name": "Pepperoni 🍖", "value": "pepperoni"},
                    {"name": "Champignon 🍄", "value": "champignon"},
                    {"name": "Cebola 🧅", "value": "cebola"},
                    {"name": "Azeitona 🫒", "value": "azeitona"},
                    Separator(),  # Adiciona um separador visual
                    {"name": "Nenhum ingrediente", "value": "nenhum"},
                ],
            }
        ]

        # Captura as respostas do usuário
        resposta_tamanho = prompt(pergunta_tamanho)
        resposta_massa = prompt(pergunta_massa)
        resposta_ingredientes = prompt(pergunta_ingredientes)

        # Se nenhum ingrediente for selecionado, exibe um erro e reinicia a seleção
        if not resposta_ingredientes["ingredientes"]:
            print("Erro: Selecione pelo menos um ingrediente!")
            continue

        # Se o usuário escolher "Nenhum ingrediente", limpa a lista de ingredientes
        if "nenhum" in resposta_ingredientes["ingredientes"]:
            print("Você escolheu uma pizza sem ingredientes. 🍕")
            ingredientes = []
        else:
            ingredientes = resposta_ingredientes["ingredientes"]

        # Calcula o preço final da pizza
        preco_pizza = PRECOS_TAMANHO[resposta_tamanho["tamanho"]] + PRECOS_MASSA[resposta_massa["massa"]]

        return {
            "tamanho": resposta_tamanho["tamanho"],
            "massa": resposta_massa["massa"],
            "ingredientes": ingredientes,
            "preco": preco_pizza,
        }

def main():
    pedidos = []  # Lista para armazenar os pedidos de pizza
    total_pedido = 0.00  # Inicializa o total do pedido

    while True:
        print(f"\nPedido atual: {len(pedidos)} pizza(s) no carrinho.")
        print(f"Total acumulado: R$ {total_pedido:.2f}\n")

        # Pergunta se o usuário deseja adicionar mais uma pizza
        pergunta_nova_pizza = [
            {
                "type": "confirm",  # Tipo de pergunta: confirmação (Sim/Não)
                "name": "adicionar",
                "message": "Deseja adicionar uma pizza ao pedido?",
                "default": True,  # Opção padrão: Sim
            }
        ]
        resposta_nova_pizza = prompt(pergunta_nova_pizza)

        # Se o usuário não quiser mais pizzas, finaliza o pedido
        if not resposta_nova_pizza["adicionar"]:
            break

        # Adiciona uma nova pizza ao pedido
        pizza = escolher_pizza()
        pedidos.append(pizza)
        total_pedido += pizza["preco"]

    # Exibe o resumo final do pedido
    print("\nResumo do seu pedido:")
    for i, pizza in enumerate(pedidos, start=1):
        print(f"\nPizza {i}:")
        print(f"- Tamanho: {pizza['tamanho'].capitalize()}")
        print(f"- Massa: {pizza['massa'].capitalize()}")
        print(f"- Ingredientes: {', '.join(pizza['ingredientes']) if pizza['ingredientes'] else 'Nenhum'}")
        print(f"- Preço: R$ {pizza['preco']:.2f}")

    print(f"\nTotal do pedido: R$ {total_pedido:.2f}")
    print("Obrigado pelo seu pedido! Sua pizza está sendo preparada. 🍕🔥")

if __name__ == "__main__":
    main()
