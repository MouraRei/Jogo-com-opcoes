import Adivinhacao
import Forca

print("Escolha qual jogo quer jogar.")
jogo = int(input("(1) Forca, (2) Adivinhacao : " ))

if(jogo ==1):
    Forca.jogar()
elif(jogo ==2):
    Adivinhacao.jogar()