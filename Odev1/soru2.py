#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

maas = int(input("Lütfen maaşınızı giriniz" " "))
zam = int(input("Zam oranınızı giriniz" " "))
zamOranı = zam /100
 

yenıMaas = (maas * zamOranı) + maas

print("Yeni maaşınız" , yenıMaas)

