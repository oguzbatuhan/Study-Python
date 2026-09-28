import random

gizli_sayi = random.randint(1, 100)
deneme = 0

print("1 ile 100 arasında bir sayı tuttum. Bul bakalım!")

while True:
    try:
        tahmin = int(input("Tahminin: "))
    except ValueError:
        print("Lütfen geçerli bir sayı gir.")
        continue

    deneme += 1

    if tahmin < gizli_sayi:
        print("Daha büyük bir sayı dene.")
    elif tahmin > gizli_sayi:
        print("Daha küçük bir sayı dene.")
    else:
        print(f"Tebrikler! {deneme} denemede buldun.")
        break