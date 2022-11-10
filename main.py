import random

acertos1=0
acertos2=0

campoaliado=[[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]
             ]
campoinimigo=[[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]
             ]
campovisao=[[0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0,0]
             ]

for cont in range(5):
    linha=int(input("Digite em qual linha quer posicionar seu navio de 1 a 5:"))-1
    coluna=int(input("Digite em qual coluna quer posicionar seu navio de 1 a 10: "))-1
    campoaliado[linha][coluna]=1
    for conta in range(5):
        print(campoaliado[conta])

for contas in range(5):
    linha1=random.randint(0,4)
    coluna1=random.randint(0,9)
    campoinimigo[linha1][coluna1]=1

while acertos1<5 and acertos2<5:
    linha2=int(input("Digite a linha que deseja atacar de 1 a 5:")) - 1
    coluna2=int(input("Digite qual coluna deseja atacar de 1 a 10:")) - 1

    if campoinimigo[linha2][coluna2] == 1:
        acertos1=acertos1+1
        print("Você acertou!!!")
        campoinimigo[linha2][coluna2]=0
        campovisao[linha2][coluna2]=1
        for contad in range(5):
            print(campovisao[contad])
    else:
        print("Você errou.   :(")
        campovisao[linha2][linha2]="X"
        for contado in range(5):
            print(campovisao[contado])

    linha3=random.randint(0,4)
    coluna3=random.randint(0,9)

    if campoaliado[linha3][coluna3]==1:
        print("O inimigo abateu um de nossos navis.")
        acertos2 = acertos2 + 1
        campoaliado[linha3][coluna3] = 0
        for contados in range(5):
            print("Campo aliado:")
            print(campoaliado[contados])
    else:
        print("O inimigo errou!!!")

if acertos1 == 5:
    print("Parabens você ganhou")

elif acertos2 == 5:
    print("Você perdeu :(")
