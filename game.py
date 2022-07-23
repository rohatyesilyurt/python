import random

print("********Sayı Tahmin Oyunu********")
print("Sayı aralığı için iki sayı belirleyin.")
x = int(input("Birinci Sayı : "))
y = int(input("İkinci Sayı : "))
hak_belirle = int(input("Kaç Hakkınız olsun? : "))
aralik = [x,y]
aralik.sort()

while True:

    sayi = random.randint(aralik[0],aralik[1])
    hak = hak_belirle
    bitir = hak + 1 
    while (bitir > 0):
    
        bitir -= 1
    
        tahmin = int(input((f"{hak} hakkınız var.Tahminde bulunun({aralik[0]}-{aralik[1]}): ")))   
    
        if bitir == 1 and tahmin != sayi:
            print(f"Hakkınız kalmadı. Sayı {sayi}.")
            break
        else:
            if tahmin == sayi:
                print("DOĞRU BİLDİNİZ, TEBRİKLER!!")
                break
            elif tahmin < sayi:
                print("-\nArtırın\n-")
            elif tahmin > sayi:
                print("-\nAzaltın\n-")
        hak -= 1
    input("***********Yeni oyun için Enter'a basın***********")
    print("*\n*\n*\n*\n*\n*")

