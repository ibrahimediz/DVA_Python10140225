
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

#yukardaki örnek koddan yararlanarak şase numarası üzerinden property, setter ve deleter yapalım

class Araba:
    tip = "Binek Otomobil"
    
    def __init__(self, plaka, marka, model, saseno):
        self.plaka = plaka
        self.marka = marka
        self.model = model
        self.__saseno = saseno  # Özel (private) değişken

    def bilgiVer(self):
        print(f"Marka: {self.marka}, Model: {self.model}")
        print(f"Plaka: {self.plaka}")

    # Şase numarası için getter (property)
    @property
    def saseno(self):
        return f"****{self.__saseno[-4:]}"  # Son 4 haneyi göster, diğerlerini gizle

    # Şase numarası için setter (değiştirme)
    @saseno.setter
    def saseno(self, yeni_saseno):
        if len(yeni_saseno) == 17 and yeni_saseno.isalnum():  # Şase numarası 17 karakter olmalı
            self.__saseno = yeni_saseno
        else:
            print("Geçersiz şase numarası! 17 karakter olmalı ve harf/rakam içermeli.")

    # Şase numarası için deleter (silme)
    @saseno.deleter
    def saseno(self):
        print("Şase numarası silindi!")
        self.__saseno = None

# Örnek kullanım
araba1 = Araba("34ABC123", "Toyota", "Corolla", "1HGCM82633A123456")

# Bilgileri göster
araba1.bilgiVer()
print("Şase No:", araba1.saseno)  # Şase numarasının son 4 hanesini göster

# Yeni şase numarası atama
araba1.saseno = "2HGCM82633A654321"
print("Yeni Şase No:", araba1.saseno)

# Şase numarasını silme
del araba1.saseno
print("Silindikten Sonra Şase No:", araba1.saseno)  # None dönecek
