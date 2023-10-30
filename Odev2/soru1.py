# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

fibonacci = [1,1]
n= 20

for i in range(2,20):
    next=  fibonacci[len(fibonacci)-2]+ fibonacci[len(fibonacci)-1]
    fibonacci.append(next)

print(fibonacci)

