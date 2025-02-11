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
"EnesAydemir",
"Sorular_Cevaplar"]

import os 

soru = """
# Soru 4:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# yukarıda yer alan şekli elde edebilmek için gerekli python
# kodunu yazınız
"""
dosyaismi = "soru4.py"
# print(len(liste))
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
        os.mkdir(f"Egzersizler/{item}")
    with open(f"Egzersizler/{item}/{dosyaismi}","w+",encoding="UTF-8") as d:
        d.write(soru)
    