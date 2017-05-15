import pyttsx
import time
from Tkinter import *

engine = pyttsx.init()

for x in range(0,10):
    print x
    engine.say(x)
    engine.runAndWait()
    for y in range(0,10):
        xx=10+10
    

    root.after(1000)




