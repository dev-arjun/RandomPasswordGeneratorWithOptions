import  random as rd 
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a1 = "abcdefghijklmnopqrstuvwxyz"
num = "1234567890"
sym = "!@#$%^&*()"
passwd = A + a1 + num + sym
option = int(input("Select the option \n 1. 8 \n 2. 12 \n 3. 16\n"))
if option == 1:
    length = 8
    password = "".join(rd.sample(passwd,length))
if option == 2:
    length = 12
    password = "".join(rd.sample(passwd,length))
if option == 3:
    length = 16
    password = "".join(rd.sample(passwd,length))
print(password)