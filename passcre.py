import random # random modülü
bh = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
kh = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
se = [".",":",";","_","-","=","+",",","/"]
Sifre = ""
sayı = int(input("kaç haneli şifre olsun >> "))
while(True):
    t = len(Sifre)
    if sayı != t:
        r = random.randint(1,4)
        if r == 1: 
            Sifre += random.choice(bh)
        elif r == 2:
            Sifre += random.choice(kh)
        elif r == 3:
            Sifre += str(random.randint(0,9))
        elif r == 4:
            Sifre += random.choice(se)
        else:
            continue
    elif sayı == t:
        print(Sifre)
        pause = input("DEVAM ETMEK İÇİN ENTER TUŞUNA BASIN")
        exit()
    else:
        exit()
