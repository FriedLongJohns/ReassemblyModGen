from helpers import randfloat
from time import sleep
import keyboard as kb
import sys

# fn=input("File name: ")
fn=sys.argv[1]
waits = bool(int(sys.argv[2]))
with open(fn,"r") as file:
    print("reading "+fn)
    lines=file.readlines()
    print("start in 5 seconds!")
    sleep(5)
    for line in lines:
        if waits and .2>=randfloat(0.0,1.0):
            sleep(randfloat(0.25,.9))
        text=line[:line.index("\n")]
        kb.press_and_release("command+shift+left")#reset indents
        kb.write(text)
        print(text)
        kb.press_and_release("command+shift+down")#delete stray ) or ] autogenerated by IDE
        kb.press_and_release("enter")
