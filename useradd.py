#Please run this program with root permissions

import os


def checkDigit(name):
    return any(char.isdigit() for char in name )


name=input('Enter String :')
if not checkDigit(name):
    pas="hello"+name
    com="useradd -p $(openssl passwd -1 "+pas+") "+name
    os.system(com)

else:
    print("user Cannot be created")

