import Graph_Reading as GR
graph = GR.Read("PF2")
print ("Provide a destination. Type 'quit' to quit" )
Current_Position = input ("Current Position?")
print("possible destination:", end=" ")
for print_func in graph[Current_Position]:
    print(print_func, end= " ")
print("")
CMD = input ("destination?")
while CMD != "quit": 
    try:
        move = False

        for Destination in graph[Current_Position]:
            if (CMD == Destination):
                move = True
                Current_Position = CMD
        if (not move): 
            print ("Invalid destination, try another." )
        print("possible destinations:", end=" ")
        for print_func in graph[Current_Position]:
            print(print_func, end= " ")
        print("")




    except:
        print ("invalid")
    print(f"Current Postion = {Current_Position}")
    CMD = input ("destination?")
    
    




#Goal is to make it so the program only shows & allows direct paths from current position whilst maintaining current postion# 