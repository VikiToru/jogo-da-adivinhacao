from random import randint


borda = '-=-'*20
print(borda + '\nVAMOS JOGAR PAR OU ÍMPAR!\n' + borda)

TEXTO_GANHOU = 'VOCÊ GANHOU! Vamos jogar de novo...'
TEXTO_ERRO = 'Não entendi. Reiniciando o jogo...'
borda2 = '-'*40
ganhou_vezes = 0

while True:
    valor_jogador = int(input('Digite um valor: '))
    valor_computador = randint(1, 10)
    par_impar = str(input('Par ou ímpar? [P/I] ')).strip().lower()[0]
    
    print(borda2)
    print(f'Você jogou {valor_jogador} e eu joguei {valor_computador}.', end=' ')
    
    if (valor_jogador + valor_computador) % 2:
        print('DEU ÍMPAR!')
        if par_impar == 'i':
            print(TEXTO_GANHOU)
            print(borda2)
            
            ganhou_vezes += 1
        elif par_impar == 'p':
            break
        else:
            print(TEXTO_ERRO)
    else:
        print('DEU PAR!')
        if par_impar == 'p':
            print(TEXTO_GANHOU)
            print(borda2)
            
            ganhou_vezes += 1
        elif par_impar == 'i':
            break
        else:
            print(TEXTO_ERRO)

print(f'VOCÊ PERDEU!\nVocê ganhou {ganhou_vezes} vezes')