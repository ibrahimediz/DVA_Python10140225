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
"yusufzekiaytac",
"Sorular_Cevaplar"]

import os 

soru = """
# Soru 6:
# 1- SQL Injection Tespiti
# Bir SQL sorgusunda zararlı bir giriş olup olmadığını kontrol eden bir fonksiyon yazın.
# 2- IP Adresi Doğrulama
Kullanıcıdan bir IP adresi alarak geçerli bir IPv4 adresi olup olmadığını kontrol edin.
# 3- IBAN Doğrulama
Kullanıcıdan bir IBAN adresi alarak geçerli bir IBAN adresi olup olmadığını kontrol edin.
"""
dosyaismi = "soru6.py"
# print(len(liste))
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
        os.mkdir(f"Egzersizler/{item}")
    with open(f"Egzersizler/{item}/{dosyaismi}","w+",encoding="UTF-8") as d:
        d.write(soru)
    
