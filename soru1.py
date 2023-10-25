#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini 
#(VKİ = ağırlık/(boy*boy)) hesaplayınız.

weight = input("Lütfen kilonuzu(kg) giriniz.")
weightasInt = int(weight)

height= input("Lütfen boyunuzu(cm) giriniz.")
heightasInt = int(height)

vkı = weightasInt / (heightasInt * heightasInt)

print("Vücut kitle indeksiniz :" , vkı)




