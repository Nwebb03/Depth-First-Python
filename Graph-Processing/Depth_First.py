import Graph_Reading as GR
import copy
import pandas as pd

#Basic Load Graph
graph = GR.Read("Graph-Data\Graph1")
startingpoint = input("Starting Node? ")
endpoint = input("End node? ")

#Create a processing queue
#Every item on the queue is a candidate path (Possible path to the goal, another list)
queue = pd.DataFrame(columns= ["To_Extend"])
queue.loc[1, "To_Extend"]= [startingpoint]
print (queue)


#loop conditional
finished = False
while((queue.shape[0] != 0) & (finished == False)):
    #Candidate path taken from the queue for processing
    to_extend = queue.loc[1, "To_Extend"]
    print(to_extend)
    #
    queue = queue.drop(index=1)
    #Main loop that "searches"

    for node in graph[to_extend[0]]:
        extended = np.copy(to_extend)
        extended = np.append(extended, node)
        x = np.ndarray((2,2,), [extended])
        queue = np.append(x, queue)


        
    print(queue)
    finished = True