#Install pyaudio first and SpeechRecognition

from googlesearch import search
import speech_recognition as sr

def action(srch):
    url=[i for i in search(srch,stop=10)]
    print(url)
    f=open("Last_Search_Result.txt","w+")
    for i in url:
        f.write(i+'\n')
    f.close()
print('''1.Search By KeyBoard 
2.Search by Voice ''')
choice=int(input("Choose :"))
if choice == 1:
    data=input("Type Something.....")
    action(data)
elif choice == 2:
    r=sr.Recognizer()
    mic=sr.Microphone()
    with mic as source:
        print("A moment of silence, please...")
        r.adjust_for_ambient_noise(source)
        print("Say Something :")
        audio = r.listen(source)
        text=r.recognize_google(audio)
        print("Thanks! You Said ",text)
    action(text)
