import Graph_Reading as GR
import copy
import numpy as np
#Basic Load Graph
finished = False
graph = GR.Read("Graph1")
startingpoint = input("Starting Node? ")
endpoint = input("End node? ")
#Creates a queue
#Array of Arrays
#Every item on the queue is a candidate path (Possible path to the goal, another list)
queue = np.ndarray((1,), [startingpoint])
print(queue.shape[0])
print((queue.shape[0] != 0) & (finished == False))
while((queue.shape[0] != 0) & (finished == False)):
    #Candidate path taken from the queue for processing
    to_extend = np.ndarray([queue[0]])
    #
    queue = np.delete(queue,0)
    #Main loop that "searches"

    for node in graph[to_extend[0]]:
        extended = np.copy(to_extend)
        extended = np.append(extended, node)
        x = np.ndarray((2,2,), [extended])
        queue = np.append(x, queue)


        
    print(queue)
    finished = True