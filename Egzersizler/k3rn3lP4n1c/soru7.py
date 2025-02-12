
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
        self.__saseno = saseno

    @property
    def saseno(self):
        return self.__saseno

    @saseno.setter
    def saseno(self, value):
        if len(value) == 17:  
            self.__saseno = value
        else:
            print("Geçersiz şase numarası!")

    @saseno.deleter
    def saseno(self):
        print("Şase numarası silindi.")
        del self.__saseno

    def bilgiVer(self):
        print(self.marka, self.model)
        print("Plaka:", self.plaka)
        print("Şase Numarası:", self.saseno)