import random
a=random.randint(1,10)
print("basladi.")
b=input("tahmin sayiniz")
a2=int(a)
b2=int(b)
c=a2-b2
if c==0: print("dogru")
if c==0: exit()
if c<0: print("cok gittin geri al")
if c>0: print("daha buyuk dusun")
d=input("2. tahmin sayiniz")
d2=int(d)
d3=a2-d2
if d3==0: print("dogru")
if d3==0: exit()
if d3<0: print("cok gittin geri al")
if d3>0: print("daha buyuk dusun")
f=input("3. tahmin sayiniz")
f2=int(f)
f3=a2-f2
a3=str(a2)
if f3==0: print("dogru")
if f3==0: exit()
if f3<0: print("cok gittin geri al")
if f3>0: print("daha buyuk dusun")
if f3<0: print("kaybettin")
if f3>0: print("kaybettin")
if f3<0: print("sayi"+a3+"idi")
if f3>0: print("sayi"+a3+"idi")