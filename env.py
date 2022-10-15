import main
import code
import cl

def get_env(name:str, ext:str, starts:str,mode:str):
    fileName = name + ext
    delimiter = ':'

    file = open(fileName, 'r')


    def findValue(fullstring):
        fullstring = fullstring.rstrip('\n')
        value = fullstring[fullstring.index(delimiter)+1:]
        value = value.replace(" "," ")
        return value


    for line in file:
        if line.startswith(starts):
            env = findValue(line)

    
    if mode == 't':
        print(env)
        s = str(input(""))



def goto(file:str, funct:str):
    complete = file + "." + funct + "()"
    exec(complete)


def reload():
    main.main()