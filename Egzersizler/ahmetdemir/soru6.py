
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

class Cokgen:
    cokgenOzelligi = "Çokgen Özelliği"
    
    def __init__(self, kenar_sayisi):
        self.kenarSayisi = kenar_sayisi
    
    def icAciToplami(self):
        return (self.kenarSayisi - 2) * 180
    
    def cokgenMethod(cls):
        print(cls.cokgenOzelligi)

kenar_ucgen = int(input("Çokgenin kenar sayısını girin: "))
ucgen = Cokgen(kenar_ucgen)
print("Çokgen Kenar Sayısı:", ucgen.kenarSayisi)
print("Çokgen İç Açı Toplamı:", ucgen.icAciToplami())

kenar_kare = int(input("Çokgenin kenar sayısını girin: "))
kare = Cokgen(kenar_kare)
print("Çokgen Kenar Sayısı:", kare.kenarSayisi)
print("Çokgen İç Açı Toplamı:", kare.icAciToplami())
