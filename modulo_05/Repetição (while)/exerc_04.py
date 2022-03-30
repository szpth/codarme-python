# O jogo “Acerte o número” funciona da seguinte maneira:
# a. Existe um certo número inteiro declarado dentro do programa que o usuário
# desconhece. Por exemplo: numero = 8
# b. O usuário tem 3 tentativas para acertar o número.
# c. A cada tentativa, é informado ao usuário se o número que ele digitou é maior,
# menor, ou igual ao número correto.
# d. O jogo termina quando o usuário erra 3 vezes (perdeu) ou quando o usuário
# acerta o número (ganhou).
# Implemente o jogo “Acerte o número”.

print("-------------------------------------------------------")
print("O JOGO - ACERTE O NÚMERO")
print("------------------------------------------------------- \n ")

n = 42

i = 1

print("Tente acertar o número secreto!")
value = int(input("Digite um número: "))

while i <= 3:
    if value == n:
        print("\nVocê acertou!")
        print("O número secreto é: ", n)
        print("-------------------------------------------------------")
        print("42.")
        print("Este número é a resposta para a Grande Pergunta sobre a Vida,")
        print("o Universo e Tudo o Mais, no livro Guia do Mochileiro da Galáxia,")
        print("de Douglas Adams.")
        break
    elif i == 3:
        print("Você errou!")
        break
    else:
        print("Você errou!")
        i += 1
        value = int(input("Digite um número: "))
