from random import randint
from time import sleep
itens=('pedra', 'papel','tesoura')
pc=randint(0, 2)
print(''' escolha um
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jg=int(input(' QUAL VOCE ESCOLHE '))
print('JOKER')
sleep(1)
print('HEN')
sleep(1)
print('PO!!!!')
sleep(1)
print('-=' * 10)
print('o computado jogou {} '.format(itens[pc]))
print('o jogador jogou {}'.format(itens[jg]))
print('-=' * 10)
if pc==0:
    if jg==0:
        print('emapte')
    elif jg==1: 
        print(' Jodador venceu')
    elif jg == 2:
        print( 'jogador perdeu')
    else:
        print('joga invalida')
elif pc==1:
    if jg == 0:
        print('jogador perdeu')
    elif jg == 1:
        print('empate')
    elif jg==2:
        print('jogador ganho')
    else:
        print('jogada invalida')
elif pc == 2:
    if jg == 0:
        print('jogador ganha')
    elif jg== 1:
        print('jogador perdeu')
    elif jg==2:
        print('empateu')
    else:
        print('Jogada invalida')
