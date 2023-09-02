import random
k=0
a=0
for i in range (0,100):
    udus=random.choice(["kapı1","kapı2", "kapı3"]) # araba koyulan kapı
    secim=random.choice(["kapı1","kapı2", "kapı3"]) #yarısmacının  secdiyi kapı
    acilan=list(frozenset(["kapı1","kapı2", "kapı3"])-frozenset([udus,secim]))[0] #sunucunun acdiği kapı
    diğeri=list(frozenset(["kapı1","kapı2", "kapı3"])-frozenset([secim,acilan]))[0] #deyişilen kapı
    print("araba koyulan kapı:"  ,udus,"1 ci  secilmiş kapı:", secim, "acılan kapı :" ,acilan, "2 ci secilen kapı:",  diğeri )
    if diğeri==udus:
        k+=1
    else:
        a+=1
print(a , "defe coat secilib."  , k , "defe car secilib.")


