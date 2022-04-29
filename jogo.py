from random import randint
from time import sleep


print('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)
numero_computador = randint(0, 10)
print(numero_computador)
sleep(2)

tentativas_falhas = 0
acertou = False

while not acertou:
    numero_jogador = int(input('Tente um número: '))
    print('PROCESSANDO...')
    sleep(1)
    
    if numero_jogador < 0 or numero_jogador > 10:
        print('Não entendi, tente novamente!')
    elif numero_jogador != numero_computador:
        tentativas_falhas += 1
        if numero_jogador < numero_computador:
            palpite = 'Mais... '
        else:
            palpite = 'Menos... '
        print('{} Tente mais uma vez.'.format(palpite))
    else:
        acertou = True
    sleep(1)
    
print('Parabéns! Você acertou com {} tentativas falhas'.format(tentativas_falhas))