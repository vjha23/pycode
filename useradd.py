import os


def checkDigit(name):
    return any(char.isdigit() for char in name )


name=input('Enter String :')
if not checkDigit(name):
    pas="hello"+name
    os.system("useradd -m -p" + pas +" "+name)

else:
    print("user Cannot be created")

