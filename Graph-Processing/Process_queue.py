import pandas as pd
class pipeline (object):
    def __init__ (self, name):
        self.queue = pd.DataFrame(columns= ["To_Extend"],)
        self.x = name
    def printname (self):
        print(self.x)
