import sys
graph = {}
def Read(File_Name): 
    f = open(File_Name , "r")
    lines = f.readlines()
    for i in range(1, len(lines)):        
        if i%2 == 1:
            key = lines[i].strip("\n")
        else:
            value = lines[i].strip("\n").split(",")
            graph[key] = value

    
     
    return(graph)
def main():
    if len(sys.argv) != 2:
        print("1 argument is required to run this as a script")
    else:
        print("Reading: " + str(sys.argv[1]))
        Read(sys.argv[1])
        

if __name__ == "__main__":
    main()
#If __name__ is run as a script, its name will always be __main__ if it is ran as a module, it will be the name of the file