import datetime

now=datetime.datetime.now()
Name=input("Enter Your Name :")

if now.hour<12 and now.hour >5 :
    print("Good Morning..!!!!!!",Name)
elif now.hour>12 and now.hour<16 :
    print('Goood AfterNoon....Have A goood Day',Name)
elif now.hour >=16 and now.hour<21:
    print("Good Evening...Sir!!!",Name)
elif now.hour >= 21 :
    print("Good Night....!!",Namesuraj)