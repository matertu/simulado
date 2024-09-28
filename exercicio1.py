import random
p = 'q'
min = int(input('Digite um número minimo = '))
max = int(input('Digite um número maximo com pelo menos 100 algarismos de intervalo = '))
min1 = max - min
l1 = []
l2 = []
n = 0

while max < min+100:
    print('Valor não aceito')
    max = int(input('Digite um número maximo com pelo menos 100 algarismos de intervalo = '))
else:
    while min <= max:
        l1.append(min)
        min += 1
sort = random.choice(l1)

print(f'Min: {max-min1}     Max: {max}       Número sorteado: {sort}')
print('Começa o jogo:'

while p != sort:
    n += 1
    p = int(input(f'Palpite {n} = '))
    l2.append(p)
    if p > sort:
        print('errado: seu palpite deve ser menor')
    elif p < sort:
        print('errado: seu palpite deve ser maior')
    else:
        print('Acertou!!!')
print(f'Resultado:\nForam {n} palpites até você acertar! \nE seus palpites foram esses: {l2}')