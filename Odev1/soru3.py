# 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
sayı1 = int(input("1.sayıyı giriniz"))
sayı2 = int(input("2.sayıyı giriniz"))
sayı3 = int(input("3.sayıyı giriniz"))

if sayı1 > sayı2 and sayı1 > sayı3: 
    print("Girdiğiniz en büyük sayı" , sayı1)
elif sayı2>sayı1 and sayı2>sayı3:
    print("Girdiğiniz en büyük sayı" , sayı2)
else:
    print("Girdiğiniz en büyük sayı" ,sayı3)
