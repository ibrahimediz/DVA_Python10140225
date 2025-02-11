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
# Soru 5:
# from random import choice
# from string import ascii_lowercase,ascii_uppercase,punctuation,digits

# yukarıda yer alan kütüphanelerden faydalanarak
# 1. En az 8 karakter uzunluğunda
# 2. En az 1 Rakam 
# 3. En az 1 Küçük Harf 
# 4. En az 1 Büyük Harf
# 5. En az 1 Noktalama
# 6. Kharf ve Bharf yan yana gelmesin Numara ve kHarf yan yana gelmesin

"""
dosyaismi = "soru5.py"
# print(len(liste))
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
        os.mkdir(f"Egzersizler/{item}")
    with open(f"Egzersizler/{item}/{dosyaismi}","w+",encoding="UTF-8") as d:
        d.write(soru)
    