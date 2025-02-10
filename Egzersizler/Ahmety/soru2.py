
# Soru 2:
# liste = [23,45,65,78,90,12] 
# a. Liste sonuna 1000 sayısını ekleyiniz
# b. Liste 0. indisine 500 sayısını ekleyiniz
# c. Listenin 3. indisinde yer alan sayıyı 2 katı ile değiştiriniz
# d. Listeyi ekrana yazdırınız
# Beklenen Çıktı
# [500,23,45,130,78,90,12,1000] 

# Başlangıçtaki liste
liste = [23, 45, 65, 78, 90, 12]

# a. Liste sonuna 1000 sayısını ekleyelim
liste.append(1000)

# b. Liste 0. indisine 500 sayısını ekleyelim
liste.insert(0, 500)

# c. Listenin 3. indisindeki sayıyı 2 katı ile değiştirelim
liste[3] = liste[3] * 2

# d. Listeyi ekrana yazdıralım
print(liste)
