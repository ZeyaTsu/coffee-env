import main
import math

def cal():
    x = True
    do = exec
    this = print
    while x:
        uinput = str(input(".cl > "))
       
        if uinput == "q":
            main.main()
            x = False
        do(uinput)