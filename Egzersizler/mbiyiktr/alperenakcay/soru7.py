
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
    def __init__(self,plaka,marka,model,saseno):
        self.plaka = plaka
        self.marka = marka
        self.model = model
        self.__saseno = saseno
        
    @property
    def saseno(self):
        return self.__saseno

    @saseno.setter
    def saseno(self,deger):
        if type(deger) == int:
            if deger in range(1,200000):
                self.__saseno = deger
            else:
                raise Exception("yanlış şase numarası girildi")
        else:
            raise Exception("lütfen şase no giriniz.")

    @saseno.deleter
    def saseno(self):
        self.__saseno*=-1

    def bilgiVer(self):
        print(self.marka,self.model)
        print("Plaka:",self.plaka)



arabaBiglisi = Araba("06DZY289","RKS","FRECCIA",20214)

print(arabaBiglisi.saseno)

del arabaBiglisi.saseno


