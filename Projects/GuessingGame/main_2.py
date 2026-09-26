import random

print('Tahmin oyununa hos geldin!!!')
game_mode = input('Seviyeni sec (kolay, orta, zor): ')

chancess = 5
random_number = 0

if game_mode == 'kolay':
    random_number = random.randint(1, 10)
elif game_mode == 'orta':
    random_number = random.randint(1, 25)
elif game_mode == 'zor':
    random_number = random.randint(1, 50)
else:
    print('Gecersiz seçim yapildi, varsayilan olarak kolay mod baslatiliyor.')
    random_number = random.randint(1, 10)

print(f'\nOyun basladi, {chancess} hakkin var!')

while chancess > 0:
    guess = int(input('Tahmin et: '))
    
    if guess == random_number:
        print(f'Tebrikler! Bildin: {random_number}')
        break
    elif guess < random_number:
        print('Daha buyuk bir sayi girmelisin.')
    else:
        print('Daha kucuk bir sayi girmelisin.')
        
    chancess -= 1
    if chancess > 0:
        print(f'Kalan hakkin: {chancess}\n')
    else:
        print(f'Malesef hakkin bitti! Tuttugum sayi: {random_number} idi.')