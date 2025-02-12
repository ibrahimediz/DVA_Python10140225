
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


 class Sinif:
     sinifOzelligi = "Sınıf Özelliği"
     def __init__(self,KenarSayisi,AciToplami):
        self.KenarSayisi=KenarSayisi
        self.AciToplami=AciToplami

     def kenarSayisiAl(self):
         print(self.ornekOzellik)
     def sinifMethod(cls):
         print(cls.sinifOzelligi)# 