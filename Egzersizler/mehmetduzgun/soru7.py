
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

#örnekten faydalanarak property e çevir setter ve deletter ayarla yukarıdaki kodu


class Araba():
    tip = "Binek Otomobil"
    def __init__(self,plaka,marka,model,saseno):
        self.plaka = plaka
        self.marka = marka
        self.model = model
        self.__saseno = saseno

        @property
        def gizli(self):
            if self.plaka == 60:
                return self.__plaka
            else:
                    raise Exception("Hatalı Plaka")
                    if self.marka == VW:
                        return self.__marka
                else:
                    raise Exception("Hatalı Marka")
                    

    def bilgiVer(self):
        print(self.marka,self.model)
        print("Plaka:",self.plaka)