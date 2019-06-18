import speech_recognition as sr 
from googlesearch import search

print('''1.Search By KeyBoard 
2.Search by Voice ''')
choice=int(input("Choose :"))
if choice == 1:
    data=input("Type Something.....")
    url=[i for i in search(data,stop=10)]
    print(url)
    f=open("Links.txt","w+")
    for i in url:
        f.write(i+'\n')
    f.close()
elif choice == 2:
    r=sr.Recognizer()
    mic=sr.Microphone()
    with mic as source:
        print("Say Something :")
        audio = r.listen(source)
        print("Time Over...Thanks")

    text=r.recognize_google(audio)
    url=[i for i in search(text,stop=10)]
    print(url)
    f=open("Links.txt","w+")
    for i in url:
        f.write(i+'\n')
    f.close()