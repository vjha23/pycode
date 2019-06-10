#!usr/bin/env python3
import os
com=input("Enter a command ")
cm=com.split()[0]
cmd='which '+cm+' &>output.txt'
path=os.system(cmd)
f=open('History.txt','a+')
r=open('History.txt')
txt=r.read().strip().split()
r.close()
boo=os.path.exists(path)
if boo:
      if cm in txt:
           os.system("echo 'Not Do This Again' | festival --tts")
           print("Not Do This Again")
      else:
           os.system(com)
else:
      print("Command Not Found")

f.write(com+"\n")
f.close()
