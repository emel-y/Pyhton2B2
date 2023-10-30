# 5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
sayı = input("Lütfen bir sayı giriniz. " "")
tersSayı = ''.join(reversed(sayı))

if sayı == tersSayı:
    print("Girilen sayı palindrom sayıdır." "")
else:
    print("Girilen sayı palindrom sayı değildir. "" ")