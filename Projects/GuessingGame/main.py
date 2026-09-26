import random

mode = 0
game_mode = 0

if True:
    print('tahmin oyununa hos geldin!!!')
    game_mode = input('seviyeni sec kolay, orta, zor : ')
else: print('lutfen gecerli deger girin')

random_number = 0
chancess = 5
guess = 0
if game_mode == 'kolay':
    random_number = random.randint(1, 10)
    print(random_number)
    while chancess > 0:
        if chancess == 5:
            print('oyun basladi 5 hakkin var!')
            guess = input('Tahmin et: ')
            if int(guess) == int(random_number):
                print(f'bildin.  {random_number}')
                break
            elif int(guess) < int(random_number):
                print('daha buyuk')
            else: print('daha kucuk')
            chancess -= 1
        elif chancess == 4:
            print('oyun basladi 4 hakkin var!')
            guess = input('Tahmin et: ')
            if int(guess) == int(random_number):
                print(f'bildin.  {random_number}')
                break
            elif int(guess) < int(random_number):
                print('daha buyuk')
            else: print('daha kucuk')
            chancess -= 1
        elif chancess == 3:
            print('oyun basladi 3 hakkin var!')
            guess = input('Tahmin et: ')
            if int(guess) == int(random_number):
                print(f'bildin.  {random_number}')
                break
            elif int(guess) < int(random_number):
                print('daha buyuk')
            else: print('daha kucuk')
            chancess -= 1
        elif chancess == 2:
            print('oyun basladi 2 hakkin var!')
            guess = input('Tahmin et: ')
            if int(guess) == int(random_number):
                print(f'bildin.  {random_number}')
                break
            elif int(guess) < int(random_number):
                print('daha buyuk')
            else: print('daha kucuk')
            chancess -= 1
        elif chancess == 1:
            print('oyun basladi 1 hakkin var!')
            guess = input('Tahmin et: ')
            if int(guess) == int(random_number):
                print(f'bildin.  {random_number}')
                break
            elif int(guess) < int(random_number):
                print('daha buyuk')
            else: print('daha kucuk')
            chancess -= 1
        else: print('hakkin bitti.')
else: print('')