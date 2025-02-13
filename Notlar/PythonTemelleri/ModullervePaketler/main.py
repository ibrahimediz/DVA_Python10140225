# ## from import 
# import os
# print(os.path.abspath(".")) # /workspace/DVA_Python10140225
# print(os.sep)
# os.walk
# from os import path as pt
# print(pt.abspath(".")) # /workspace/DVA_Python10140225
# import sys
# print(*sys.path,sep="\n")
# from sys import path
# print(*path,sep="\n")

# import paket
# objPaket = paket.Sinif1("üretilen nesne")
# objPaket.soylePaket1()
# import paket.modul1
# objModul = paket.modul1.Sinif2("üretilen nesne")
# objModul.soyleModul1()


from paket import Sinif1
from paket.modul1 import Sinif2

objPaket = Sinif1("üretilen nesne")
objPaket.soylePaket1()
objModul = Sinif2("üretilen nesne")
objModul.soyleModul1()