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
        self.__saseno = saseno  # private, dışarıdan erişilemiyor

    def bilgiVer(self):
        print("Marka:", self.marka)
        print("Model:", self.model)
        print("Plaka:", self.plaka)
    
    # Şasi numarasını güvenli bir şekilde almak için getter metodu
    def get_saseno(self):
        return self.__saseno
    
    # Şasi numarasını değiştirmek için setter metodu
    def set_saseno(self, saseno):
        self.__saseno = saseno

# Örnek kullanım:
araba1 = Araba("34ABC34", "Toyota", "Corolla", "12345ABC")
araba1.bilgiVer()

# Şasi numarasını güvenli şekilde alma
print("Şasi Numarası:", araba1.get_saseno())

# Şasi numarasını değiştirme
araba1.set_saseno("67890XYZ")
print("Yeni Şasi Numarası:", araba1.get_saseno())

