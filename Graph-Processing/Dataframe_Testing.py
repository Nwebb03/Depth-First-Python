import Graph_Reading as GR
import copy
import pandas as pd

#Basic Load Graph
graph = GR.Read("Graph-Data\Graph1")
startingpoint = input("Starting Node? ")
endpoint = input("End node? ")

#Create a processing queue
#Every item on the queue is a candidate path (Possible path to the goal, another list)
queue = pd.DataFrame(columns= ["To_Extend", "Extended"], index= ["1"])
queue.loc["1", "To_Extend"]= startingpoint
print (queue)