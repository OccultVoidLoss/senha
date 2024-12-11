import random
def main():
    jogo = True
    cor = ["laranja", "azul", "vermelho", "rosa", "preto", "branco", "amarelo", "roxo", "marrom", "verde"]
    c = 0
    resposta = []
    while (c < 4):
        x = random.choice(cor)
        resposta.append(x) 
        c +=1
    print("As cores disponíveis são", *cor)
    j = list(input("Faça seu chute: "))
    a = 10
    while jogo:
        if (a == 0):
            jogo = False
        print("Você tem", a, "tentativas restantes")
        if (j[0] == resposta[0]):
            print("Primeira cor e posição certa")
        elif (j[0] in resposta):
            print("primeira cor certa posição errada")
        else:
            print("primeira cor errada posição errada")
        
        
        if (j[1] == resposta[1]):
            print("Segunda cor certa")
        elif (j[1] in resposta):
            print("segunda cor certa posição errada")
        else:
            print("segunda cor errada posição errada")
            
            
        if (j[2] == resposta[2]):
            print("Terceira cor certa")
        elif (j[2] in resposta):
            print("Terceira cor certa posição errada")
        else:
            print("Terceira cor errada posição errada")
            
            
        if (j[3] == resposta[3]):
            print("Quarta cor certa")
        elif (j[3] in resposta):
            print("Quarta cor certa posição errada")
        else:
            print("Quarta cor errada posição errada")
        if(j != resposta):
            a -=1
        else:
            print("Acertou!")
            jogo = False
        j = list(input("Faça seu chute: "))
        print(resposta)            
main()
         
    
    