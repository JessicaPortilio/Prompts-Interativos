# Importa a biblioteca InquirerPy para interagir com o usuário de forma simples
from InquirerPy import inquirer

# Importa a classe EmptyInputValidator para verificar se a entrada não está vazia
from InquirerPy.validator import EmptyInputValidator

# Importa a classe Validator e ValidationError para criar regras de validação personalizadas
from prompt_toolkit.validation import Validator, ValidationError


# Cria uma pergunta interativa que pede o nome do usuário
nome = inquirer.text(
    message="Qual é o seu nome?",  # Mensagem que será exibida na tela
    qmark="❓",  # Símbolo de pergunta
    amark="🖍️",  # Símbolo de resposta
    validate=EmptyInputValidator(message="O nome não pode ser vazio!")  # Valida se o nome não está vazio
).execute()  # Executa a interação com o usuário e armazena a resposta

# Exibe o nome que o usuário inseriu
print(f'Olá, {nome}')

# Cria uma classe personalizada para validar se o nome tem pelo menos 3 caracteres
class NomeValidator(Validator):
    def validate(self, document):  # Método que valida a entrada do usuário
        text = document.text.strip()  # Remove espaços extras do começo e do final do texto

        if len(text) < 3:  # Se o texto tiver menos de 3 caracteres
            # Levanta um erro de validação com uma mensagem e posiciona o cursor no final do texto
            raise ValidationError(
                message="O nome deve ter pelo menos 3 caracteres!",  # Mensagem de erro
                cursor_position=len(text)  # Posiciona o cursor após o texto digitado
            )

# Cria outra pergunta interativa, agora com a validação do comprimento do nome
nome2 = inquirer.text(
    message="Qual é o seu nome?",  # Mensagem que será exibida na tela
    qmark="❓",  # Símbolo de pergunta
    amark="🖍️",  # Símbolo de resposta
    validate=NomeValidator()  # Validação personalizada que verifica se o nome tem pelo menos 3 caracteres
).execute()  # Executa a interação com o usuário e armazena a resposta

# Exibe o nome que o usuário inseriu após a validação
print(f'Olá, {nome2}')
