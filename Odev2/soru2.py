# 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

def mukSayi (sayi):
    bolenler = []

    for i in range(1,sayi):
        if sayi % i ==0:
            bolenler.append(i)

    bolenToplami = sum(bolenler)

    if sayi == bolenToplami :
        print("Girdiğiniz sayı mükemmel sayıdır.")
    else :
        print("Girdiğiniz sayı mükemmel sayı değildir.")

sayi = int(input("Lütfen bir sayı giriniz." ""))
mukSayi(sayi)
