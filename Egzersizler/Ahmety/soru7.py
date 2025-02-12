
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

class Araba():
    tip = "Binek Otomobil"
    
    def __init__(self, plaka, marka, model, saseno):
        self.plaka = plaka
        self.marka = marka
        self.model = model
        self.__saseno = saseno  # __saseno, private (özel) bir özellik
    
    # Araba bilgilerini verir
    def bilgiVer(self):
        print(f"Marka: {self.marka}, Model: {self.model}")
        print(f"Plaka: {self.plaka}")
    
    # Saseno'yu alabilmek için getter metodunu ekleyelim
    def get_saseno(self):
        return self.__saseno
    
    # Saseno'yu değiştirebilmek için setter metodunu ekleyelim
    def set_saseno(self, yeni_saseno):
        self.__saseno = yeni_saseno

# Kullanıcıdan bilgi al
plaka = input("Arabanın plakasını girin: ")
marka = input("Arabanın markasını girin: ")
model = input("Arabanın modelini girin: ")
saseno = input("Arabanın şase numarasını girin: ")

# Araba nesnesini oluştur
araba = Araba(plaka, marka, model, saseno)

# Araba bilgilerini göster
araba.bilgiVer()

# Saseno'yu almak için getter metodunu kullanabiliriz
print("Şase No:", araba.get_saseno())

# Saseno'yu değiştirebiliriz
yeni_saseno = input("Yeni şase numarasını girin: ")
araba.set_saseno(yeni_saseno)
print("Yeni Şase No:", araba.get_saseno())


