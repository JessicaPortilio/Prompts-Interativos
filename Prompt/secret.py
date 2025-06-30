# O que é o prompt secret?
# O prompt secret funciona como o text, mas oculta a entrada do usuário no terminal.
# Ele é útil para coletar senhas ou informações sensíveis, garantindo que ninguém veja o que foi digitado.

# 2. Como usar o secret prompt?
# Vamos fazer um exemplo simples de como solicitar uma senha sem exibi-la no terminal:

# Importa a biblioteca InquirerPy, que permite criar interações no terminal de forma amigável
from InquirerPy import prompt

# Define uma pergunta para o usuário digitar a senha
pergunta = [
    {
        "type": "password",  # Define o tipo da entrada como "password" (a senha ficará oculta ao ser digitada)
        "name": "senha",  # Nome da variável que armazenará a resposta
        "message": "Digite sua senha:",  # Mensagem exibida ao usuário
    }
]

# Exibe a pergunta no terminal e armazena a resposta digitada pelo usuário
resposta = prompt(pergunta)

# Exibe uma mensagem confirmando que a senha foi recebida (sem mostrar a senha digitada por segurança)
print("Senha recebida com sucesso!")


# "type": "password" → Especifica que o input será oculto.
# A senha digitada não aparece no terminal, apenas asteriscos ou nada (dependendo do terminal).

# 3. Validação de Senha
# Podemos exigir que a senha tenha um tamanho mínimo:

# Importa a biblioteca InquirerPy, que permite criar perguntas interativas no terminal
from InquirerPy import prompt

# Importa o validador de senha da biblioteca InquirerPy para definir regras de validação
from InquirerPy.validator import PasswordValidator

# Define a pergunta para o usuário criar uma senha
pergunta = [
    {
        "type": "password",  # Define que a entrada será uma senha (os caracteres digitados ficarão ocultos)
        "name": "senha",  # Nome do campo onde a senha será armazenada na resposta
        "message": "Crie uma senha:",  # Mensagem que será exibida no terminal para o usuário
        "validate": PasswordValidator(  # Adiciona um validador para garantir que a senha siga as regras definidas
            length=6,  # Define que a senha deve ter no mínimo 6 caracteres
            message="A senha deve ter pelo menos 6 caracteres."  # Mensagem exibida caso a senha seja inválida
        ),
    }
]

# Exibe a pergunta no terminal e armazena a senha digitada pelo usuário (validando antes de aceitar)
resposta = prompt(pergunta)

# Exibe uma mensagem confirmando que a senha foi cadastrada com sucesso
print("Senha cadastrada com sucesso!")


#  O que foi adicionado?

# "validate": PasswordValidator(length=6, message="A senha deve ter pelo menos 6 caracteres.")
# → Exibe um erro se a senha tiver menos de 6 caracteres.

# 4. Confirmando a Senha
# Se quisermos que o usuário digite a senha duas vezes, podemos comparar as respostas:

# Importa a biblioteca InquirerPy, que permite criar perguntas interativas no terminal
from InquirerPy import prompt

# Cria uma lista de perguntas para solicitar a senha e sua confirmação
perguntas = [
    {
        "type": "password",  # Define que a entrada será do tipo "password" (os caracteres digitados ficarão ocultos)
        "name": "senha",  # Nome do campo onde a senha será armazenada
        "message": "Crie uma senha:",  # Mensagem exibida para o usuário ao solicitar a senha
    },
    {
        "type": "password",  # Define que a entrada será do tipo "password" novamente
        "name": "confirmacao",  # Nome do campo onde a confirmação da senha será armazenada
        "message": "Confirme sua senha:",  # Mensagem exibida para o usuário ao solicitar a confirmação da senha
    }
]

# Exibe as perguntas no terminal e armazena as respostas digitadas pelo usuário
respostas = prompt(perguntas)

# Verifica se a senha digitada e a confirmação são iguais
if respostas["senha"] == respostas["confirmacao"]:
    print("Senha confirmada com sucesso!")  # Exibe mensagem de sucesso se as senhas coincidirem
else:
    print("As senhas não coincidem. Tente novamente.")  # Exibe mensagem de erro caso sejam diferentes



#  O que acontece aqui?

# O usuário digita a senha duas vezes.
# Se forem diferentes, um alerta é exibido.

# 5. Customizando o Estilo do secret
# Podemos aplicar estilos ao prompt secreto da mesma forma que no text:

# Importa a biblioteca InquirerPy, que permite criar perguntas interativas no terminal
from InquirerPy import prompt

# Definindo um estilo personalizado para personalizar as cores e o formato das mensagens no terminal
custom_style = {
    "questionmark": "fg:#4B0082 bold",  # Define a cor roxa escura e negrito para o ponto de interrogação "?"
    "question": "fg:#191970 bold",  # Define a cor azul escura e negrito para a pergunta exibida ao usuário
    "answer": "fg:#FF1493 bold",  # Define a cor rosa choque e negrito para a resposta digitada pelo usuário
}

# Criando uma pergunta para solicitar a senha ao usuário
pergunta = [
    {
        "type": "password",  # Define que a entrada será do tipo "password" (os caracteres digitados ficarão ocultos)
        "name": "senha",  # Nome do campo onde a senha será armazenada
        "message": "Digite sua senha:",  # Mensagem exibida para o usuário ao solicitar a senha
    }
]

# Exibe a pergunta no terminal com o estilo personalizado e armazena a resposta digitada pelo usuário
resposta = prompt(pergunta, style=custom_style)

# Exibe uma mensagem confirmando que a senha foi recebida (sem mostrar a senha por segurança)
print("Senha recebida!")



# 6. Armazenando a Senha com Hash (Segurança Avançada)
# Se você quiser armazenar senhas de forma segura, nunca salve a senha em texto puro.
# Use hashing com bcrypt para segurança:

# Importa a biblioteca bcrypt, que permite criptografar senhas de forma segura
import bcrypt

# Importa a biblioteca InquirerPy, que permite criar perguntas interativas no terminal
from InquirerPy import prompt

# Solicita ao usuário que crie uma senha segura
pergunta_criacao = [
    {
        "type": "password",  # Define que a entrada será do tipo "password" (os caracteres digitados ficarão ocultos)
        "name": "senha",  # Nome do campo onde a senha será armazenada
        "message": "Crie uma senha segura:",  # Mensagem exibida para o usuário ao solicitar a senha
    }
]

# Exibe a pergunta no terminal e armazena a resposta digitada pelo usuário
resposta_criacao = prompt(pergunta_criacao)

# Converte a senha digitada pelo usuário em bytes para ser processada pelo bcrypt
senha_bytes = resposta_criacao["senha"].encode("utf-8")

# Gera um hash seguro da senha usando bcrypt (adicionando um "sal" aleatório para segurança extra)
hash_senha = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())

# Exibe a senha criptografada (apenas para fins ilustrativos; na prática, essa informação não deve ser exibida)
print(f"Senha criptografada: {hash_senha.decode('utf-8')}")

# Solicita ao usuário que digite a senha novamente para verificar se está correta
pergunta_verificacao = [
    {
        "type": "password",  # Define que a entrada será do tipo "password" novamente
        "name": "senha_verificacao",  # Nome do campo onde a senha digitada será armazenada
        "message": "Digite a senha novamente para verificar:",  # Mensagem exibida ao solicitar a verificação da senha
    }
]

# Exibe a pergunta no terminal e armazena a senha digitada para verificação
resposta_verificacao = prompt(pergunta_verificacao)

# Verifica se a senha digitada na segunda vez corresponde ao hash da senha original
if bcrypt.checkpw(resposta_verificacao["senha_verificacao"].encode("utf-8"), hash_senha):
    print("Senha correta! A verificação foi bem-sucedida.")  # Exibe mensagem de sucesso caso a senha esteja correta
else:
    print("Senha incorreta! Tente novamente.")  # Exibe mensagem de erro caso a senha não corresponda ao hash


# # Tem como voltar a senha no formato original que foi digitado pelo usuário?
# Não, não é possível reverter o hash para obter a senha original. 
# O bcrypt usa um processo de hashing unidirecional, o que significa que, uma vez criptografada, 
# a senha não pode ser descriptografada.

# O que podemos fazer é comparar a senha digitada com o hash para saber se está correta, 
# mas nunca recuperar a senha original a partir do hash.

#  Por que isso é importante?

# O bcrypt transforma a senha em um hash seguro.
# Mesmo se alguém acessar o banco de dados, não conseguirá ver a senha real.

# Resumo da Aula
# ✅ O prompt secret oculta a entrada do usuário no terminal.
# ✅ Podemos validar a senha com PasswordValidator.
# ✅ É possível confirmar a senha comparando as respostas.
# ✅ Podemos customizar o estilo do prompt.
# ✅ Para segurança, podemos armazenar a senha com bcrypt.