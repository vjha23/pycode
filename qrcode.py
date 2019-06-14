from googlesearch import search
import os
data=input("Enter Your Search :")
n=1
for i in search(data,stop=3):
	cmd="qrencode -s 10 -m 2 -o ok"+str(n)+".png '"+i+"'"
	os.system(cmd)
	n=n+1
