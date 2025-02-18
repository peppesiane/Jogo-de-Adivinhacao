print("*********************")
print("Bem vindo ao jogo de advinhação!")
print("*********************")

numero_secreto = 55

chute_str = input("Digite o seu número:")
print("Você digitou:", chute_str)
chute = int(chute_str)

if(numero_secreto == chute):
    print("VocÊ acertou!")
else:
    print("Você errou!")

print("Fim de jogo!")

