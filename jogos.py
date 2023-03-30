import foca
import adivinhacao

print("*********************************")
print("*******Escolha o seu jogo********")
print("*********************************")

print("(1) jogo da adivinhação (2) jogo da foca")

jogo = int(input("Qual jogo?"))

if jogo == 1:
    print("Jogo da foca")
    adivinhacao.jogar()
    
elif jogo == 2:
    print("Jogo da adivinhação")
    foca.jogar()
