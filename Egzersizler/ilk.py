liste = ["mehmetduzgun",
"ismailyalvac",
"kaganfidan",
"resatkorkmaz",
"ramazanortasoz",
"hasanberkaykoyuncu",
"alierenavluklu",
"ahmetgayrim",
"umutkoruk",
"alperenakcay",
"ahmetdemir",
"HuseyinTOKTAS",
"ercana",
"Ahmety",
"Nihat",
"ceyhunaksoz",
"metehantas",
"k3rn3lP4n1c",
"mbiyiktr",
"omeraksoy",
"gokselgok",
"alicebe",
"yasinerboga",
"Mehmet",
"Sorular_Cevaplar"]

import os 

soru = """
# Soru 2:
# liste = [23,45,65,78,90,12] 
# a. Liste sonuna 1000 sayısını ekleyiniz
# b. Liste 0. indisine 500 sayısını ekleyiniz
# c. Listenin 3. indisinde yer alan sayıyı 2 katı ile değiştiriniz
# d. Listeyi ekrana yazdırınız
# Beklenen Çıktı
# [500,23,45,130,78,90,12,1000] 
"""
dosyaismi = "soru2.py"
# print(len(liste))
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
        os.mkdir(f"Egzersizler/{item}")
    with open(f"Egzersizler/{item}/{dosyaismi}","w+",encoding="UTF-8") as d:
        d.write(soru)
    