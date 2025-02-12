
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
    sinifOzelligi = "Çokgen Özelliği"
    
    def __init__(self, kenarSayisi):
        self.kenarSayisi = kenarSayisi
    
    def icAcilarToplami(self):
        return (self.kenarSayisi - 2) * 180
    
    @classmethod
    def sinifMethod(cls):
        print(cls.sinifOzelligi)

class Ucgen(Cokgen):
    def __init__(self):
        super().__init__(3)
        
class Kare(Cokgen):
    def __init__(self):
        super().__init__(4)

ucgen = Ucgen()
kare = Kare()

print("Üçgen Kenar Sayısı:", ucgen.kenarSayisi)
print("Üçgen İç Açılar Toplamı:", ucgen.icAcilarToplami())

print("Kare Kenar Sayısı:", kare.kenarSayisi)
print("Kare İç Açılar Toplamı:", kare.icAcilarToplami())
