import random
letters = int(input("Enter number of LETTERS you want in your password: "))
symbols = int(input("Enter number of SYMBOLS you want in your password: "))
num = int(input("Enter number of NUMBERS you want in your password: "))


temp_password = ""
for i in range(letters):
    randletter = random.randint(65, 122)
    if randletter in (91,92,93,94,95,96):
        randletter+= 6
    genletter = chr(randletter)
    temp_password+= genletter

for j in range(symbols):
    randsymbol = random.randint(33, 47)
    gensymbol = chr(randsymbol)
    temp_password+= gensymbol


for k in range(num):
    randnum = random.randint(48, 57)
    gennum = str(chr(randnum))
    temp_password+= gennum

print(f"TEMP PASSWORD : {temp_password}")
password_list = list(temp_password)
random.shuffle(password_list)

password="".join(password_list)

print(f"Your Generated Password is : \n{password}")






