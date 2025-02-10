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
"yasinerboga"
"Sorular_Cevaplar"]

import os 

# print(len(liste))
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
        os.mkdir(f"Egzersizler/{item}")
    open(f"Egzersizler/{item}/Merhaba.py","a+",encoding="UTF-8")
    