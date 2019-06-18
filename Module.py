import sys
import datetime
import os
def add():

    data=sys.argv
    sum=0
    for i in data[1:]:
        sum=sum+ int(i)
    return sum

def srt(data):
    data.sort()
    return data
def hlp():
    return help('modules')

#Greeetings....!!!!!!!
os.system("echo 'Hello Suraj' | festival --tts")
time=datetime.datetime.now().hour
if time >= 5 and time <= 12:
    print("Good Morning.....!!!!!!!!!")
elif time > 12 and time <= 16:
    print("Good Afternoon......!!!!!!!!")
elif time > 16 and time <= 20:
    print("Good Evening....!!!!")
else:
    print("Good Night..........!!!!!!!!")