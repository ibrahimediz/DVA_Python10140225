
# Soru 1:
# input fonksiyonu ile kullanıcıdan ismini isteyiniz. 

#isim = input("İsminizi Giriniz:")
#print(isim[0:2])
#print(isim[:2])

#soru = """
# Soru 2:
# liste = [23,45,65,78,90,12] 
# a. Liste sonuna 1000 sayısını ekleyiniz
# b. Liste 0. indisine 500 sayısını ekleyiniz
# c. Listenin 3. indisinde yer alan sayıyı 2 katı ile değiştiriniz
# d. Listeyi ekrana yazdırınız
# Beklenen Çıktı
# [500,23,45,130,78,90,12,1000] 


# l1 = [1,2,3]
# l2 = l1.copy()
# l2.append(500)
# print(l1,l2)


# a = 1
# for i in range(10,0,-2):
#     print(" " * int(i / 2) + "*"*a) 
#     a += 2
# for i in range(0,10,+2):
#     print(" " * int(i / 2) + "*"*a) 
#     a -= 2
# print("     *")


# a = 1
# for i in range(10,0,-2):
#     print(" " * int(i / 2) + "*"*a) 
#     a += 2
# for i in range(0,10,+2):
#     print(" " * int(i / 2) + "*"*a) 
#     a -= 2


a = 1
for i in range(10, 0, -2):
    print(" " * int(i / 2) + "*" * a)
    a += 2
for i in range(0, 10, +2):
    print(" " * int(i / 2) + "*" * a)
    a -= 2
    
print(" " * 5 + "*")