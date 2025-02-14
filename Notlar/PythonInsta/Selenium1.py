import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# tarayici = webdriver.Firefox(executable_path="driver\geckodriver.exe")
# tarayici.get("http://www.instagram.com")
# time.sleep(3)

# vektorelpython20
# Vektorel2005
class InstaBotCore:
    def __init__(self,username,password,bekle=20):
        self.username = username
        self.password = password
        self.bekle = bekle
        self.tarayici = webdriver.Firefox(executable_path="driver\geckodriver.exe")
        self.tarayici.implicitly_wait(bekle)
        self.girisYap()

    def girisYap(self):
        self.tarayici.get("https://www.instagram.com/accounts/login/")
        usernamegiris = self.tarayici.find_element_by_name("username")
        usernamegiris.send_keys(self.username)
        sifregiris = self.tarayici.find_element_by_name("password")
        sifregiris.send_keys(self.password) 
        sifregiris.send_keys(Keys.ENTER)
        alternatif = self.tarayici.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        alternatif.click()
        giris = self.tarayici.find_element_by_css_selector("button.aOOlW:nth-child(2)")
        giris.click()

    def TakipEt(self,kullaniciAdi):
        self.tarayici.get(f"https://www.instagram.com/{kullaniciAdi}/")
        takipdugme = self.tarayici.find_element_by_css_selector("button._5f5mN:nth-child(1)")
        if (takipdugme.text != ""):
            takipdugme.click()
        self.tarayici.get(f"https://www.instagram.com")

    def TakipEtv2(self,adres):
        self.tarayici.get(adres)
        try:
            takipdugme = self.tarayici.find_element_by_css_selector("button._5f5mN:nth-child(1)")
            if (takipdugme.text != ""):
                takipdugme.click()
        except:
            takipdugme = self.tarayici.find_element_by_css_selector("button.sqdOP:nth-child(1)")
            if (takipdugme.text != ""):
                takipdugme.click()
        self.tarayici.get(f"https://www.instagram.com")   


    def TakipBirak(self,kullaniciAdi):
        self.tarayici.get(f"https://www.instagram.com/{kullaniciAdi}/")
        time.sleep(self.bekle)
        takipdugme = self.tarayici.find_element_by_css_selector("button._5f5mN:nth-child(1)")
        if (takipdugme.text == ""):
            takipdugme.click()
            dogrulamaDugme = self.tarayici.find_element_by_xpath('//button[text()= "Takibi Bırak"]')
            dogrulamaDugme.click()
        self.tarayici.get(f"https://www.instagram.com")

    def ilkFotoLike(self,kullaniciAdi):
        self.tarayici.get(f"https://www.instagram.com/{kullaniciAdi}/")
        resim = self.tarayici.find_element_by_class_name("_9AhH0")
        resim.click()
        like = self.tarayici.find_element_by_class_name("fr66n")
        like.click()

    def TakipciListeAl(self,kullanici,param):
        self.tarayici.get(f"https://www.instagram.com/{kullanici}/")
        takipciLink = self.tarayici.find_element_by_css_selector('ul li a')
        takipciLink.click()
        takipciListe = self.tarayici.find_element_by_css_selector('div[role="dialog"] ul')
        takipciListe.click()
        takipciSay = len(takipciListe.find_elements_by_css_selector('li'))

        hareketZincir = webdriver.ActionChains(self.tarayici)
        while takipciSay < param:
            hareketZincir.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            # self.tarayici.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            takipciSay = len(takipciListe.find_elements_by_css_selector('li'))


        takipciler = takipciListe.find_elements_by_css_selector('li')
        # print(len(takipciler))
        liste = []
        for takipci in takipciler:
            liste.append(takipci.find_element_by_css_selector('a').get_attribute('href'))
        return liste
    
    def topluTakip(self,liste):
        for item in liste:
            time.sleep(2)
            self.TakipEtv2(item)
    

    def Kayit(self,kullanici,takipcilerListe):
        import pymongo
        import datetime
        client = pymongo.MongoClient("")
        takipciler = client["takipciler"]
        col = takipciler["instagram3"]
        liste = []
        for item in takipcilerListe:
            liste.append({"hesap":kullanici,"takipciAdres":item,"tarih":str(datetime.datetime.now()),"ap":"1"})
        
        result = col.insert_many(liste)
        print(result.inserted_ids)


# bot1 = InstaBotCore("vektorelpython20","Vektorel2023")
# bot1.TakipEt("silagencoglu")
# bot1.ilkFotoLike("silagencoglu")
# bot1.ilkFotoLike2("silagencoglu",param=2)
# bot1.ilkFotoLike2("silagencoglu",param=4)
# bot1.ilkFotoLike2("silagencoglu",param=3)
# bot1.TakipBirak("silagencoglu")
# liste = bot1.TakipciListeAl("silagencoglu",300)
# bot1.Kayit("silagencoglu",liste)
# bot1.topluTakip(liste)







