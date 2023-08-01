    # 1
string = input("Введите строку: ")
string2 = ""
for i in range (len(string)):
    string2 += string[len(string)-i-1]
print(string2)

    # 2
value = input("Введите строку: ")
c = 0 # счетчик букв
n = 0 # счетчик цифр
for i in range (len(value)):
    if (value[i].isdigit()==True):
        n+=1
    elif(value[i].isalpha()==True):
        c+=1
print("Цифр: ", n, "\nБукв:", c)

    # 3
value1 = input("Введите строку: ")
value2 = input("Введите символ: ")
d = 0
for i in range(len(value1)):
    if(value1[i]==value2):
        d+=1
print("Колличество вхождений: ", d)

    # 4
string = input("Введите строку: ")
qwe = input("Введите слово для поиска в строке: ")
c = string.count(qwe) # поиск слова в строке
print(c)

    # 5
string = input("Введите строку: ")
s = input("Введите слово для поиска: ")
z = input("Введите слово для замены: ")
c = string.replace(s,z)
print(c)