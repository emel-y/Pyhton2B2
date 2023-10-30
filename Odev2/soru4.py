#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
#Kendisinden ve 1’den başka pozitif böleni olmayan 2 ve 2’den büyük sayılara asal sayı denir. 

sayi = int(input("Lütfen bir sayı giriniz"))



def asal (sayı):
    if sayi>1:
        for i in range(2,sayi):
            kalan = sayi%i
            if  kalan==0:
                print("Asal sayı değildir")
                break
            
        else:
            print("Asal sayıdır")
            
    else:
        print("Asal sayı değildir.")

asal(sayi)




