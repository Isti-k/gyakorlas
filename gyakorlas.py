# 1. feladat:
# Írjuk ki 0-tól 150-ig a páros számokat!

def feladat1(szam):
    i = 0
    while(i <= szam):
        if i != szam:
            print(f"{i}", end="; ")
        else:
            print(f"{i}", end=" ")
        i += 2

# 2. feladat:
# Számold meg 10 bekért szám esetében a 3-mal osztható számokat!

def feladat2():
    i = 0
    harommal_oszthato_db = 0
    while(i <= 10):
        szam: int = int(input("Adjon meg egy számot!"))
        if szam % 3 == 0:
            harommal_oszthato_db += 1
        i += 1
    print("3-mal osztható számok száma:", harommal_oszthato_db)

# 3. feladat:
# Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!*

def feladat3():
    szam: int = int(input("Kérek egy 10-el osztható számot!"))
    while not(szam % 10 == 0):
        szam: int = int(input("Ez a szám nem osztható! Adj meg egy másikat!"))
    print("Gratula!")

# 4. feladat:
# Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!*
def feladat4():
    szam: int = int(input("Kérek egy számot!"))
    while not (szam < 100 and szam >= 10 and szam % 2 == 0):
        szam: int = int(input("Adj meg egy másik számot!"))
    print("Draculacula!")

# 5. feladat:
# Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.*

def feladat5():
    szam: int = int(input("Kérek egy számot!"))
    while not (szam < 100 and szam >= 10 and szam % 2 == 1):
        szam: int = int(input("Adj meg egy másik számot!"))
    print("Blablablaa!")

# 6. feladat:
# Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz.*
def feladat6():
    szam: int = int(input("Kérek egy számot!"))
    while not ((szam ** 0.5) and szam < 100 and szam % 3 == 0):
        szam: int = int(input("Adj meg egy másik számot!"))
    print("Blablablaa!")

# 7. feladat.
# Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk!

def feladat7():
    szam1: int = int(input("Kérek egy számot!"))
    szam2: int = int(input("Kérek egy számot!"))
    szam3: int = int(input("Kérek egy számot!"))
    while not((szam1 < szam2 + szam3) and (szam2 < szam1 + szam3) and (szam3 < szam1 + szam2)):
        print("Kérek 3-om másikat!")
        szam1: int = int(input("Kérek egy számot!"))
        szam2: int = int(input("Kérek egy számot!"))
        szam3: int = int(input("Kérek egy számot!"))

