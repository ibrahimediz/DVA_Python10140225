
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

class cokgen():
    tip = "Çokgenler"
    def __init__(self,kenar,icacı):
        self.kenar = kenar
        self.icacı = icacı

x = int(input("Çokgenin kenar sayısını giriniz: "))
cokgen1 = cokgen(x,(x-2)*180)
print(cokgen1)
print(x, "gen' in iç açıları toplamı", (x-2)*180)