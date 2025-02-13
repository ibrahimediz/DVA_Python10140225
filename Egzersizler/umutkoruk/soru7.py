
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
    # Sınıf Özelliği
    tip = "Binek Otomobil"
    
    def __init__(self, plaka, marka, model, saseno, yetki):
        # Araba nesnesinin temel özelliklerini atıyoruz.
        self.plaka = plaka
        self.marka = marka
        self.model = model
        self.yetki = yetki
        
        # Private (özel) şase numarası, dışarıdan erişilemez.
        self.__saseno = saseno
    
    # getter (şase numarasına erişim): Yetki kontrolü yapılıyor.
    @property
    def saseno(self):
        if self.yetki == 1:  # Yetki 1 ise şase numarasına erişim sağlanır.
            return self.__saseno
        else:
            raise Exception("Yetki Hatası")  # Yetki hatası verilir.
    
    # setter (şase numarasını güncelleme): Şase numarasının geçerliliği kontrol edilir.
    @saseno.setter
    def saseno(self, yeni_saseno):
        if type(yeni_saseno) == str and len(yeni_saseno) == 12:  # Şase numarası 12 karakter uzunluğunda olmalı.
            self.__saseno = yeni_saseno  # Şase numarasını günceller.
        else:
            raise ValueError("Geçersiz Şase Numarası")  # Hatalı şase numarası girilirse hata verir.
    
    # deleter (şase numarasını silme): Şase numarasını silme işlemi yapar.
    @saseno.deleter
    def saseno(self):
        self.__saseno = None  # Şase numarasını siler.
    
    # Araba bilgilerini yazdıran metod
    def bilgiVer(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Plaka: {self.plaka}")
        try:
            print(f"Şase Numarası: {self.saseno}")  # Getter kullanarak şase numarasına erişim
        except Exception as e:
            print(str(e))  # Yetki hatası mesajını yazdırır.


# Nesne oluşturma (yetki 1, şase numarası veriliyor)
araba1 = Araba("34ABC34", "Toyota", "Corolla", "SASE123456789", 1)

# Araba bilgilerini gösterme
araba1.bilgiVer()

# Şase numarasını değiştirme (setter)
araba1.saseno = "SASE987654321"  # Yeni şase numarası
araba1.bilgiVer()

# Şase numarasını silme (deleter)
del araba1.saseno
araba1.bilgiVer()

# Yetki hatası ile şase numarasına erişim (yetki 0 olursa hata verir)
araba2 = Araba("35XYZ35", "Honda", "Civic", "SASE987654321", 0)
araba2.bilgiVer()




araba = "honda"


sayı = int("9")