#3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

sayi1 = int(input("Lütfen 0'dan büyük bir sayı giriniz"))
sayi2 = int(input("Lütfen 0'dan büyük, ikinci bir sayı giriniz"))

if (sayi1>sayi2):
    kucukSayi = sayi2
else:
    kucukSayi = sayi1
for i in range(1,kucukSayi+1):
    if (sayi1 % i==0) and (sayi2%i ==0):
        ebob = i

print("Ebob = ",ebob)
print("Ekok = ", (sayi1*sayi2)//ebob)