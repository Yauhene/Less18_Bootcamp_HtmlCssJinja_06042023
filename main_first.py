file = open('file.txt','r', encoding = 'utf-8')
list_1 = list()
resultData = list()
#print(file.read())
#print(file.readlines()) #функция поместит информацию в список построчно
#print(file.readline()) #данная функция выведет только первую строку

#--------------------------------

for line in file.readlines():
    resultData.append((tuple(line.split('\n')[0].split(';'))))
   
#--------------------------------
#print(line)
# list_1 = list(file.readlines())
#print(list_1)


file.close()

print(resultData)