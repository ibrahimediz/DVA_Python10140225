
# Soru 7:
# class Araba():
#     tip = "Binek Otomobil"
#     def __init__(self,plaka,marka,model,saseno):
#         self.plaka = plaka
#         self.marka = marka
#         self.model = model
#         self.__saseno = saseno

#     def bilgiVer(self):
#         print(self.marka,self.model)
#         print("Plaka:",self.plaka)
class Araba:
    tip = "Binek Otomobil"  # Bu, tüm Araba nesneleri için ortak bir sınıf özelliği
    
    def __init__(self, plaka, marka, model, saseno):
        self.plaka = plaka         # Arabanın plaka numarasını atıyoruz
        self.marka = marka         # Arabanın markasını atıyoruz
        self.model = model         # Arabanın modelini atıyoruz
        self.__saseno = saseno     # Şasi numarasını özel bir değişken olarak saklıyoruz
    
    def bilgiVer(self):
        # Araba hakkında bilgileri ekrana yazdıran fonksiyon
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Plaka: {self.plaka}")
    
    def sasenoGoster(self):
        # Şasi numarasına dışarıdan erişim için bir getter metodu ekliyoruz
        return self.__saseno
    
    # Şasi numarasını değiştirebilmek için setter metodu ekliyoruz
    @property
    def saseno(self):
        return self.__saseno
    
    @saseno.setter
    def saseno(self, yeni_saseno):
        # Şasi numarasını değiştirme işlemi. Burada, geçerli bir şasi numarasını kabul edebiliriz.
        if isinstance(yeni_saseno, str) and len(yeni_saseno) > 0:
            self.__saseno = yeni_saseno
        else:
            print("Geçersiz şasi numarası!")
    
    # Şasi numarasını silme işlemi için deleter metodu ekliyoruz
    @saseno.deleter
    def saseno(self):
        print("Şasi numarası siliniyor...")
        del self.__saseno

# Araba sınıfından bir nesne oluşturuyoruz
araba1 = Araba("34ABC123", "Toyota", "Corolla", "12345XYZ")

# Araba hakkında bilgi veriyoruz
araba1.bilgiVer()

# Şasi numarasını değiştirelim
araba1.saseno = "98765ZYX"  # Setter metodu ile şasi numarasını değiştiriyoruz
print("Yeni Şasi Numarası:", araba1.sasenoGoster())

# Geçersiz bir şasi numarası atamayı deneyelim
araba1.saseno = ""  # Geçersiz bir şasi numarası

# Şasi numarasını silelim
del araba1.saseno  # Deleter metodu ile şasi numarasını siliyoruz

# haymanalı gerekeni yapıyor komutanım :D 


