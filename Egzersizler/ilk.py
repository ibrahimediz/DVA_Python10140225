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
# Soru 1:
# input fonksiyonu ile kullanıcıdan ismini isteyiniz. 
# kullanıcının girmiş olduğu veririnin ilk 2 karakterini ekrana yazdıran python kodunu yazınız
"""

# print(len(liste))
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
        os.mkdir(f"Egzersizler/{item}")
    with open(f"Egzersizler/{item}/Merhaba.py","w+",encoding="UTF-8") as d:
        d.write(soru)
    