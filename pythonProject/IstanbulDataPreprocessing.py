import string
filePath = 'istanbul_data.txt'
charToReplace= {'ş':'s','ğ':'g','ü':'u','ö':'o','ç':'c','ı':'i'}
with open(filePath, 'r',encoding="utf8") as file:
    fileLines = file.readlines()
    #set kullanılarak unique hale getirildi.
    fileLines=set(fileLines)
    #print(fileLines)
    newFile= open('newTxt.txt','w',encoding="utf8")
    for line in fileLines:
        #tüm satırlar küçük harf yapıldı
        line = line.lower()
        #noktalama işaretlerini silme
        for i in string.punctuation:
            line = line.translate(str.maketrans(i," "))
        #sadece sayıdan oluşan line silinir
        flag = 0
        for i in line.strip():
            if i in string.digits:
                pass
            else:
                flag = 1
                break
        if flag == 0:
            line= ''
            continue
        #türkçe karakterleri değiştirme
        line = line.translate(str.maketrans(charToReplace))
        
        newFile.write(line)
        #print(line)