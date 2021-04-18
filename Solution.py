myFile = open("https://github.com/GayathriSK148/File-handling/blob/main/conv.txt","r")
file = myFile.readlines()
Characters = []                         #calling a list
for line in file:
    words = line.split()                #extracts the substring before the character ':'
    if words:
        char=words[0]
        if char not in Characters:      #checking if the character is already in the list
            Characters.append(char)     #adding the names of characters to the list
print(Characters)
print(len(Characters))

for i in Characters:
    o=str(i.replace(':',''))
    j=".".join([o,"txt"])
    file1 = open(j,"w")
    file = open("https://github.com/GayathriSK148/File-handling/blob/main/conv.txt")
    z=[]
    for line in file:
        list1=line.split()
        if list1 and i in list1[0]:
            for k in list1[1:]:
                k=str(k.replace('.',''))
                k=str(k.replace('?',''))
                k=str(k.replace('!',''))
                if k not in z:
                    file1.write(k + '\n')
                    z.append(k)
