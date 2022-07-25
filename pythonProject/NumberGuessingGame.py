import random
num = random.randint(0,10)
attempt = 5
msg = " "
while attempt > 0:
    userInput= int(input("Sayı Giriniz: "))
    if userInput == num:
        msg = "Tebrikler, kazandın!"
        break
    elif userInput > num:
        attempt -=1
        print(f"{userInput} Sayısından Daha Küçük Bir Sayı Girmelisin.\n{attempt} adet deneme hakkın kaldı.")
        continue
    elif userInput < num:
        attempt -=1
        print(f"{userInput}Sayısından Daha Büyük Bir Sayı Girmelisin.\n{attempt} adet deneme hakkın kaldı.")
        continue
else:
    msg = f'Kaybettin! Deneyecek hakkın Kalmadı.'
print(msg)
