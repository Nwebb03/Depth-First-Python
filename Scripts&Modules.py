import sys

def My_Function(File_Name): 
    f = open(File_Name , "r")
    lines = f.readlines() 
    for line in lines:
        line = line.split(",")
        for i in range (0, len(line)):
            x = float(line[i])
            print(x)
    return
def main():
    if len(sys.argv) != 2:
        print("1 argument is required to run this as a script")
    else:
        print("Reading: " + str(sys.argv[1]))
        My_Function(sys.argv[1])
        

if __name__ == "__main__":
    main()
#If __name__ is run as a script, its name will always be __main__ if it is ran as a module, it will be the name of the file