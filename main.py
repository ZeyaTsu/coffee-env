import time
import env

#ext = '.cfe'
#mode = 't'
cs = 't'
error = 0


def console():
    global error
    global cs

    if cs == 't':
        while cs == 't':
            uinput = str(input("> "))
            exec(uinput)
    elif cs != 't' and error == 0:
        error += 1 
        
        print("Nothing happened. Going back to main.. (0)")
        main()



def main(): 
    global error
    global cs
    
    
    print("... Coffe Env. ...")
    bar = '█'
    for i in range(1, 20):
        time.sleep(0.05)
        print(bar, end="")
    print("")

    console()
    if error == 1:
        print("Error (0) Did you mean 't' for cs line.6 ?")
        c = str(input("Do you want to replace 'f' to 't' for cs line.6 ? y/n "))
        if c == 'y':
            cs = 't'
            error = 0
            main()
        else:
            error = 0
            main()

launch = 0

if launch == 0:
    if __name__ == '__main__':
        main()