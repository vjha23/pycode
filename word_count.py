#!/usr/bin/python3
import random
def count(data):
	dic={}
	lt=[]
	ln=len(ch)
	for i in range(ln):
		count=0
		for j in range(ln-1):
			if ch[i]==ch[j]and i!=j:			
				count=count+1
		if ch[i]!=' ':
			dic[ch[i]]=count
	dic1=sorted(dic, key=dic.get, reverse=True)
	for i in dic1 :
		if dic[i]!=0:
			print (i,"--->",dic[i])
	return dic

def Print_string(lt):
	print("New String--->",end=" ")
	for i in lt:
		print(i," ",end='')
	print()

def rm_words(dat,lt):
	rm=[]
	rm=[word for word,num in dat.items() if num > 5]
	for l in rm:
		while l in lt:
			lt.remove(l)
	Print_string(lt)
	
def add_words(wordc,lt):
	rm=[]
	new=""
	rm=[word for word,num in wordc.items() if num==1]
	for l in rm:
		lt.append(l)
	while len(lt)>500:
		ran=random.random(len(lt))
		lt.remove(lt[ran])
	Print_string(lt)
		
data=input("Enter data :")
if len(data) > 500:
	print('Limit exceeds.....!!!')
	exit()
#Count Chaaracters
print("Characters Count :")
ch=[ch for ch in data]
x=count(ch)
#Count Words
print("Words Count :")
ch=data.split()
x=count(ch)
#Remove Words More than 5 time repeated
print("After Removing Words :")
rm_words(x,ch)
print("After adding word Which is repeated 1 times")
add_words(x,ch)
