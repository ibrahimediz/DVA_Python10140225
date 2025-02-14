
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


class cokgen:
    def __init__(self,kenarSayisi):
        self.kenarSayisi = kenarSayisi

    def icAciHesapla(self):
        return (int(self.kenarSayisi) -2)*180


cokgenBilglsi = cokgen(input("Kenar sayısı giriniz : "))

print(" iç açıları toplamı : " , cokgenBilglsi.icAciHesapla())