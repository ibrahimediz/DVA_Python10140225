class Araba():
    tip = "Binek Otomobil"
    def __init__(self,plaka,marka,model,saseno):
        self.plaka = plaka
        self.marka = marka
        self.model = model
        self.__saseno = saseno
        self.__gizli = "Gizli Bilgi"
    def bilgiVer(self):
        print(self.marka,self.model)
        print("Plaka:",self.plaka)

    @property
    def gizli(self):
        if self.gizli == 1:
            return self.__gizli
        else:
            raise Exception("Yetki Hatası")
    
    @gizli.setter
    def gizli(self,param):
        if type(param) == int:
            if param in range(1,20):
                self.__gizli = param
            else:
                raise Exception("Limit Hatası")
        else:
            raise ValueError("Değer Hatası")

    @gizli.deleter
    def gizli(self):
        self.__gizli*=-1

obj1 = Araba("68ac68","volvo","s90",123456)
obj1.gizli = 2
print(obj1.gizli)


