
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
    # Cokgen sınıfı, çokgenlerin genel özelliklerini taşıyor.
    def __init__(self, kenar_sayisi):
        self.kenar_sayisi = kenar_sayisi
    
    def ic_aci_toplami(self):
        # İç açı toplamını hesaplamak için genel formül: (kenar sayısı - 2) * 180
        return (self.kenar_sayisi - 2) * 180
    
    def __str__(self):
        return f"{self.kenar_sayisi} kenarlı çokgen"

class Ucgen(Cokgen):
    # Üçgen, Cokgen sınıfından türetiliyor ve kenar sayısı 3 olarak belirleniyor.
    def __init__(self):
        super().__init__(3)

class Kare(Cokgen):
    # Kare, Cokgen sınıfından türetiliyor ve kenar sayısı 4 olarak belirleniyor.
    def __init__(self):
        super().__init__(4)

# Üçgen ve Kare nesneleri oluşturuluyor
ucgen = Ucgen()
kare = Kare()

# Nesnelerin kenar sayısı ve iç açı toplamını yazdırıyoruz
print(f"{ucgen}: Kenar Sayısı = {ucgen.kenar_sayisi}, İç Açı Toplamı = {ucgen.ic_aci_toplami()}°")
print(f"{kare}: Kenar Sayısı = {kare.kenar_sayisi}, İç Açı Toplamı = {kare.ic_aci_toplami()}°")