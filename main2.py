file = open('file.txt','r', encoding = 'utf-8')
#print(file.read())
list_1 = list()
resultData = list()
#print(file.readlines()) #функция поместит информацию в список построчно
#print(file.readline()) #данная функция выведет только первую строку

#--------------------------------

for line in file.readlines():
    
        #line(line[1:].split('\ufeff'))
        #resultData.append((tuple(line.split('\ufeff'))))
    
    print(line.split('\n')[0].split(';'))
    strDat = line
    strDat = strDat[0:]
    print("*******", strDat)

    resultData.append((tuple(strDat.split('\n')[0].split(';'))))
    #print("*******", resultData.append((tuple(strDat.split('\n')[0].split(';')))))
   
#--------------------------------
#print(line)
# list_1 = list(file.readlines())
#print(list_1)


file.close()

print(resultData)