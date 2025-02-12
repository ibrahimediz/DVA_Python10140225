
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

    def bilgiVer(self):
        print(self.marka, self.model)
        print("Plaka:", self.plaka)
    
    @property
    def saseno(self):
        return self.__saseno
    
    @saseno.setter
    def saseno(self, value):
        if len(value) == 17:  # Saseno'nun 17 karakter uzunluğunda olması gerektiğini varsayalım
            self.__saseno = value
        else:
            print("Geçersiz şase numarası, 17 karakter olmalı.")
    
    @saseno.deleter
    def saseno(self):
        print("Şase numarası siliniyor.")
        del self.__saseno

        


