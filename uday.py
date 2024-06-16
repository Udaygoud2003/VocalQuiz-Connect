import os
import time
from gtts import gTTS
import speech_recognition as sr

def op(words):
    tts=gTTS(text=words,lang="en")
    fn="voice.mp3"
    tts.save(fn)
    os.system("start voice.mp3")
    
    
def ip():
    r=sr.Recognizer()
    with sr.Microphone() as s:
        audio=r.listen(s)
        said=""
        try:
            said=r.recognize_google(audio)
            said.lower()
            print(said)
        except Exception as e:
            print("exception " + str(e))
    return said  

def name():
    op("Welcome to Voice Quiz:,what is your name? ")
    time.sleep(4)
    n1=ip()
    op(f"Hello{n1}  Your Quiz will start in 3:, 2:, 1:,")
    time.sleep(4)
    return n1 

def Qn1():
    op("what is the capital city of india? Option A: Delhi,Option B: Mumbai,Option C:Hyderabad,Option D:Kolkata")
    time.sleep(12)
    score=0
    q1=ip()
    if "Delhi" in q1:
        op("Correct answer, Score increased by one ")
        score=1   
    else:
        op("Wrong answer, Correct answer is Delhi")
        score=0
    return score    
      
def Qn2():
    op("India lies in which continent? Option A:Africa,Option B:Asia,Option C:Australia,option D:North America")
    time.sleep(12)
    score=0
    q2=ip()
    if "Asia" in q2:
        op("Correct answer, Score increased by one ")
        score=1
    else:
        op("Wrong answer, Correct answer is Asia")
        score=0
    return score

def Qn3():
    op("who is our current prime minister?Option A: Modi ,Option B: sarojini naidu,Option C:Indira gandhi,Option D:Lal bahadur sastri")
    time.sleep(13)
    score=0
    q3=ip()
    if "Modi" in q3:
        op("Correct answer, Score increased by one ")
        score=1
    else:
        op("Wrong answer, Correct answer is Modi") 
        score=0
    return score
    
def Qn4():
    op("which animal is known as ship of desert?Option A:deer,Option B: camel,Option C:elephant,Option D:crocodile")
    time.sleep(10)
    score=0
    q3=ip()
    if "camel" in q3:
        op("Correct answer, Score increased by one ")
        score=1
    else:
        op("Wrong answer, Correct answer is camel") 
        score=0
    return score 
   
def Qn5():
    op("Who is known as Father of Our Nation?Option A: Modi ,Option B: sarojini naidu,Option C:Gandhi,Option D:Lal bahadur sastri")
    time.sleep(13)
    score=0
    q3=ip()
    if "Gandhi" in q3:
        op("Correct answer, Score increased by one ")
        score=1
    else:
        op("Wrong answer, Correct answer is Gandhi") 
        score=0
    return score 
   
def Qn6():
    op("Smallest state of india is?Option A:Goa,Option B:Kerala,Option C:Delhi,Option D:Punjab")
    time.sleep(10)
    score=0
    q3=ip()
    if "Goa" in q3:
        op("Correct answer, Score increased by one ")
        score=1
    else:
        op("Wrong answer, Correct answer is Goa") 
        score=0
    return score 

def Qn7():
    op("Which is the longest river on the earth?Option A: Sindu,Option B:Narmada,Option C:Ganga,Option D:Nile")
    time.sleep(11)
    score=0
    q3=ip()
    if "Nile" in q3:
        op("Correct answer, Score increased by one ")
        score=1
    else:
        op("Wrong answer, Correct answer is Nile") 
        score=0
    return score 

def Qn8():
    op("The total distance around a figure is called its?Option A: Area ,Option B: perimeter,Option C:Volume ,Option D:circumference")
    time.sleep(12)
    score=0
    q3=ip()
    if "perimeter" in q3:
        op("Correct answer, Score increased by one ")
        score=1
    else:
        op("Wrong answer, Correct answer is perimeter") 
        score=0
    return score

def Qn9():
    op("National Animal of india ?Option A: Lion,Option B: Tiger,Option C:Peacock,Option D:Deer")
    time.sleep(9)
    score=0
    q3=ip()
    if "tiger" in q3:
        op("Correct answer, Score increased by one ")
        score=1
    else:
        op("Wrong answer, Correct answer is Tiger") 
        score=0
    return score
 
def Qn10():
    op("Which planet is nearest to Earth?Option A: Mars ,Option B: saturn,Option C:venus,Option D:jupiter")
    time.sleep(10)
    score=0
    q3=ip()
    if "Venus" in q3:
        op("Correct answer, Score increased by one ")
        score=1
    else:
        op("Wrong answer, Correct answer is venus") 
        score=0
    return score                                             

n1=name()
x=Qn1()
time.sleep(4)
y=Qn2()
time.sleep(4)
z=Qn3()
time.sleep(4)
a=Qn4()
time.sleep(4)
b=Qn5()
time.sleep(3)
c=Qn6()
time.sleep(4)
d=Qn7()
time.sleep(4)
e=Qn8()
time.sleep(3)
f=Qn9()
time.sleep(4)
g=Qn10()
time.sleep(4)


def result():
    m=int(x)
    n=int(y)
    o=int(z)
    q=int(a)
    r=int(b)
    s=int(c)
    t=int(d)
    u=int(e)
    v=int(f)
    w=int(g)
    l=m+n+o+q+r+s+t+u+v+w
    name=n1
    op(f"{name}Your score is{str(l)}")
    time.sleep(4)
    
    op("Thank you for participating!")
    
result()           
        
