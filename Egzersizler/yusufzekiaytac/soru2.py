
# Soru 2:
# liste = [23,45,65,78,90,12] 
# a. Liste sonuna 1000 sayısını ekleyiniz
# b. Liste 0. indisine 500 sayısını ekleyiniz
# c. Listenin 3. indisinde yer alan sayıyı 2 katı ile değiştiriniz
# d. Listeyi ekrana yazdırınız
# Beklenen Çıktı
# [500,23,45,130,78,90,12,1000] 

#liste = [23, 45, 65, 78, 90, 12]
#liste.append(1000)
#liste.insert(0, 500)
#liste[3] = liste[3] * 2
#print(liste)

soru = """
# Soru 3:
# gsymh = input("GSYMH Bilgisi Giriniz:")
# if gsymh.isdigit():
#     gsymh = int(gsymh)
#     if gsymh <= 1000:
#         print("Yoksulsunuz")
#     else:
#         print("Şanslısınız")
# else:
#     print("Yanlış Giriş")
# Yukarıda yer alan kod bloğundan faydalanarak 
# oy kullanma yaşınının 16 olduğu bir ülkede 
# kullanıcıdan alınan yaş bilgisi ile kontrol gerçekleştiriniz
# ve ekrana oy kullanabilirsin yazınız
"""
yas = input("Yas Bilgisi Giriniz:")
if yas.isdigit():
    yas = int(yas)
    if yas >= 16:
        print("Oy kullanabilir")
    else:
        print("Oy kullanamaz")
else:
    print("Yanlis giris")
