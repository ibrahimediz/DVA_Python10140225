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
# class Sinif:
#     sinifOzelligi = "Sınıf Özelliği"
#     def __init__(self,a):
#        self.ornekOzellik = a
    
#     def ornekMethod(self):
#         print(self.ornekOzellik)

#     def sinifMethod(cls):
#         print(cls.sinifOzelligi)

# yukarıda yer alan örnekten faydalanarak Cokgen adında bir sınıf üretiniz
# bu sınıf üzerinden üçgen ve kare adında iki nesne üretip 
# bu nesnelere ait kenar sayısı ve iç açı toplamını ekrana yazdırınız
"""
dosyaismi = "soru6.py"
# print(len(liste))
for item in liste:
    if not os.path.exists(f"Egzersizler/{item}"):
        os.mkdir(f"Egzersizler/{item}")
    with open(f"Egzersizler/{item}/{dosyaismi}","w+",encoding="UTF-8") as d:
        d.write(soru)
    
