import time
import env


#ext = '.cfe'
#mode = 't'
cs = 't'
error = 0

prefix = None

r = ["reload"]

def console():
    global error
    global cs
    global prefix

    if cs == 't':
        while cs == 't':
            if prefix == None:
                prefix = str(input("P > "))
            if prefix == "leave":
                print("... Goodbye. ...")
                bar = '█'
                for i in range(1, 20):
                    time.sleep(0.02)
                    print(bar, end="")
                break

            uinput = str(input(f"{prefix} > "))

            if uinput in r:
                prefix = None
                main()
            

            finput = prefix + "." + uinput
            exec(finput)
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
        launch += 1