# 1. O que é o prompt confirm?
# O prompt confirm permite que o usuário responda "Sim" ou "Não" de maneira intuitiva.
# Ele é útil para:
# ✅ Pedir confirmações antes de executar uma ação.
# ✅ Criar menus de opções "Sim" ou "Não".
# ✅ Evitar que o usuário tome uma decisão acidentalmente.

# 2. Como usar o confirm prompt?
# Aqui está um exemplo básico onde o usuário precisa confirmar uma ação:

# Importa a biblioteca InquirerPy, que permite criar perguntas interativas no terminal
from InquirerPy import prompt

# Define uma pergunta para o usuário
pergunta = [
    {
        "type": "confirm",  # O tipo "confirm" cria uma pergunta de "Sim" ou "Não"
        "name": "continuar",  # Nome da variável que armazenará a resposta
        "message": "Deseja continuar?",  # Texto exibido para o usuário
    }
]

# Exibe a pergunta no terminal e armazena a resposta do usuário
resposta = prompt(pergunta)

# Exibe no terminal a resposta do usuário (True para "Sim" e False para "Não")
print(f"Resposta: {resposta['continuar']}")


# Como funciona?

# O prompt exibe "[Y/n]",.
# O valor retornado será True para "Sim" e False para "Não".

# 3. Definir um Valor Padrão (default)
# Podemos definir um valor padrão usando "default":

# Importa a biblioteca InquirerPy, que permite criar perguntas interativas no terminal
from InquirerPy import prompt

# Define uma pergunta para o usuário
pergunta = [
    {
        "type": "confirm",  # O tipo "confirm" cria uma pergunta de "Sim" ou "Não"
        "name": "deletar",  # Nome da variável que armazenará a resposta
        "message": "Tem certeza de que deseja excluir o arquivo?",  # Pergunta exibida ao usuário
        "default": False,  # Define a resposta padrão como "Não" (False)
    }
]

# Exibe a pergunta no terminal e armazena a resposta do usuário
resposta = prompt(pergunta)

# Exibe no terminal a resposta do usuário (True para "Sim" e False para "Não")
print(f"Confirmação: {resposta['deletar']}")

# 4. Exibir Diferentes Mensagens Baseadas na Resposta
# Podemos usar if para exibir mensagens diferentes dependendo da escolha do usuário.

# Importa a biblioteca InquirerPy, que permite criar perguntas interativas no terminal
from InquirerPy import prompt

# Define uma pergunta para o usuário
pergunta = [
    {
        "type": "confirm",  # O tipo "confirm" cria uma pergunta de "Sim" ou "Não"
        "name": "inscricao",  # Nome da variável que armazenará a resposta
        "message": "Deseja se inscrever no nosso curso?",  # Pergunta exibida ao usuário
    }
]

# Exibe a pergunta no terminal e armazena a resposta do usuário
resposta = prompt(pergunta)

# Verifica a resposta do usuário
if resposta["inscricao"]:  # Se o usuário respondeu "Sim" (True)
    print("Ótimo! Você está inscrito! 🎉")  # Exibe mensagem de confirmação
else:  # Se o usuário respondeu "Não" (False)
    print("Que pena! Talvez na próxima. 😢")  # Exibe mensagem de recusa


# 5. Aplicação Prática: Validação de Exclusão de Conta
# Vamos simular um sistema onde o usuário precisa confirmar duas vezes antes de excluir sua conta.

# Importa a biblioteca InquirerPy, que permite criar perguntas interativas no terminal
from InquirerPy import prompt

# Define uma lista de perguntas a serem feitas ao usuário
perguntas = [
    {
        # O tipo "confirm" cria uma pergunta de "Sim" ou "Não"
        "type": "confirm",
        "name": "confirmar_1",  # Nome da variável onde será armazenada a resposta
        "message": "Tem certeza de que deseja excluir sua conta?",  # Pergunta exibida ao usuário
    },
    {
        # Outra pergunta de confirmação
        "type": "confirm",  # Tipo de pergunta "confirm"
        "name": "confirmar_2",  # Nome da variável que armazenará a segunda resposta
        "message": "Essa ação é irreversível. Tem certeza?",  # Pergunta que só aparece se a primeira for "Sim"
        # A opção 'when' faz com que a pergunta apareça apenas se a resposta anterior for 'Sim' (True)
        "when": lambda respostas: respostas["confirmar_1"],  # Checa se a primeira pergunta foi respondida com "Sim"
    }
]

# Exibe as perguntas para o usuário e armazena as respostas
respostas = prompt(perguntas)

# Verifica a resposta à segunda pergunta
if respostas.get("confirmar_2"):  # Se a segunda resposta for "Sim" (True)
    print("Conta excluída com sucesso! 🚨")  # Exibe mensagem de sucesso
else:  # Se a segunda resposta for "Não" (False)
    print("A exclusão foi cancelada. 👍")  # Exibe mensagem de cancelamento


# 6. Personalizando a Aparência
# Podemos mudar a cor do prompt para destacar a pergunta:

# Importa a biblioteca InquirerPy, que permite fazer perguntas interativas ao usuário no terminal
from InquirerPy import prompt

# Define um estilo personalizado para modificar as cores e o formato das mensagens no terminal
custom_style = {
    "questionmark": "fg:#4B0082 bold",  # Modifica o ponto de interrogação "?" para cor roxa escura e estilo negrito
    "question": "fg:#191970 bold",  # Modifica a pergunta exibida para cor azul escura e estilo negrito
    "answer": "fg:#FF1493 bold",  # Modifica a resposta do usuário para cor rosa choque e estilo negrito
}

# Define a pergunta a ser feita ao usuário
pergunta = [
    {
        "type": "confirm",  # Tipo de pergunta: confirmação (Sim ou Não)
        "name": "salvar",  # Nome da variável onde será armazenada a resposta (resposta['salvar'])
        "message": "Deseja salvar as configurações?",  # Mensagem exibida ao usuário
    }
]

# Exibe a pergunta no terminal e armazena a resposta do usuário na variável 'resposta'
# O estilo personalizado será aplicado às mensagens exibidas
resposta = prompt(pergunta, style=custom_style)

# Exibe no terminal a resposta do usuário (se ele escolheu salvar ou não)
print(f"Configuração salva? {resposta['salvar']}")

# 7. Exemplo Completo: Sistema de Login
# Vamos criar um projeto mais completo e interativo para simular um sistema de login. O projeto incluirá:

# Login: O usuário insere nome de usuário e senha.

# Validação: Verifica se o nome de usuário e a senha estão corretos.

# Opção de permanecer logado: Pergunta ao usuário se deseja permanecer logado.

# Mensagens personalizadas: Exibe mensagens amigáveis e informativas.

# Repetição: Permite que o usuário tente fazer login novamente em caso de erro.

# Importa a função 'prompt' da biblioteca 'InquirerPy', que é usada para criar perguntas interativas no terminal.
from InquirerPy import prompt

# Dados de usuários válidos (simulando um banco de dados).
usuarios = {
    "admin": "senha123",  # Nome de usuário: admin, Senha: senha123
    "usuario": "123456",  # Nome de usuário: usuario, Senha: 123456
}

# Função para validar o login.
def validar_login(usuario, senha):
    # Verifica se o usuário existe no dicionário 'usuarios' e se a senha está correta.
    if usuario in usuarios and usuarios[usuario] == senha:
        # Se o usuário e a senha estiverem corretos, retorna True.
        return True
    # Caso contrário, retorna False.
    return False

# Função principal do programa.
def sistema_login():
    # Loop infinito para permitir que o usuário tente fazer login várias vezes.
    while True:
        # Pergunta ao usuário o nome de usuário e a senha.
        perguntas_login = [
            {
                "type": "input",  # Tipo de pergunta: entrada de texto.
                "name": "usuario",  # Nome da resposta (será armazenada em resposta['usuario']).
                "message": "Digite seu nome de usuário:",  # Mensagem exibida ao usuário.
            },
            {
                "type": "password",  # Tipo de pergunta: senha (o texto é oculto).
                "name": "senha",  # Nome da resposta (será armazenada em resposta['senha']).
                "message": "Digite sua senha:",  # Mensagem exibida ao usuário.
            },
        ]
        # Faz as perguntas ao usuário e armazena as respostas.
        resposta_login = prompt(perguntas_login)

        # Obtém o nome de usuário e a senha digitados pelo usuário.
        usuario = resposta_login["usuario"]
        senha = resposta_login["senha"]

        # Valida o login usando a função 'validar_login'.
        if validar_login(usuario, senha):
            # Se o login for bem-sucedido, exibe uma mensagem de boas-vindas.
            print(f"\nBem-vindo, {usuario}! 🎉\n")
            # Pergunta ao usuário se deseja permanecer logado.
            pergunta_manter_logado = [
                {
                    "type": "confirm",  # Tipo de pergunta: confirmação (sim/não).
                    "name": "manter_logado",  # Nome da resposta (será armazenada em resposta['manter_logado']).
                    "message": "Deseja permanecer logado?",  # Mensagem exibida ao usuário.
                    "default": True,  # Valor padrão (sim).
                }
            ]
            # Faz a pergunta ao usuário e armazena a resposta.
            resposta_manter_logado = prompt(pergunta_manter_logado)

            if resposta_manter_logado["manter_logado"]:
                # Se o usuário escolher permanecer logado, exibe uma mensagem.
                print("Você permanecerá logado. 🔒")
            else:
                # Se o usuário escolher não permanecer logado, exibe uma mensagem.
                print("Você será desconectado ao sair. 👋")
            break  # Sai do loop após o login bem-sucedido.
        else:
            # Se o login falhar, exibe uma mensagem de erro.
            print("\nNome de usuário ou senha incorretos. Tente novamente. ❌\n")

        # Pergunta ao usuário se deseja tentar fazer login novamente.
        pergunta_tentar_novamente = [
            {
                "type": "confirm",  # Tipo de pergunta: confirmação (sim/não).
                "name": "tentar_novamente",  # Nome da resposta (será armazenada em resposta['tentar_novamente']).
                "message": "Deseja tentar fazer login novamente?",  # Mensagem exibida ao usuário.
                "default": True,  # Valor padrão (sim).
            }
        ]
        # Faz a pergunta ao usuário e armazena a resposta.
        resposta_tentar_novamente = prompt(pergunta_tentar_novamente)
        if not resposta_tentar_novamente["tentar_novamente"]:
            # Se o usuário escolher não tentar novamente, exibe uma mensagem de agradecimento e encerra o programa.
            print("Obrigado por usar o sistema de login. Até mais! 👋")
            break

# Executa o programa.
if __name__ == "__main__":
    sistema_login()