
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
    def __init__(self, kenar_sayisi):
        self.kenar_sayisi = kenar_sayisi
        self.ic_aci_toplami = (kenar_sayisi - 2) * 180  # İç açı toplamı formülü
    
    def bilgileri_goster(self):
        print(f"Kenar Sayısı: {self.kenar_sayisi}, İç Açı Toplamı: {self.ic_aci_toplami}°")

# Kullanıcıdan giriş al
kenar_sayisi = int(input("Lütfen çokgenin kenar sayısını girin: "))

# Çokgen nesnesini oluştur
cokgen = Cokgen(kenar_sayisi)

# Bilgileri ekrana yazdır
cokgen.bilgileri_goster()