
# Soru 1:
# input fonksiyonu ile kullanıcıdan ismini isteyiniz. 
# kullanıcının girmiş olduğu veririnin ilk 2 karakterini ekrana yazdıran python kodunu yazınız

#isim = input ("Lütfen isminizi girin:")
#print(isim[0:2])


# Soru 2:
# liste = [23,45,65,78,90,12] 
# a. Liste sonuna 1000 sayısını ekleyiniz
# b. Liste 0. indisine 500 sayısını ekleyiniz
# c. Listenin 3. indisinde yer alan sayıyı 2 katı ile değiştiriniz
# d. Listeyi ekrana yazdırınız
# Beklenen Çıktı
# [500,23,45,130,78,90,12,1000] 


liste = [23, 45, 65, 78, 90, 12]
liste.append(1000)
liste.insert(0, 500)
liste[3] = liste[3] * 2
print(liste)