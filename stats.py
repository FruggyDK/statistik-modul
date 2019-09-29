import math
from prettytable import PrettyTable

class data:
    def __init__(self, data):
        self.data = data
        self.sum = sum(data)
        self.length = len(data) #hvis stikprøve,sel.length-1
        self.middel = self.sum / self.length
        self.obs = []
        self.hyppighed = {}
        self.varians = 0
        self.spredning = 0
        self.min = min(self.data)
        self.max = max(self.data)
        self.variationsbredde = self.max - self.min

    def printOut(self):
        self.data.sort()
        table = PrettyTable()

        table.field_names = ('#', 'n')
        table.add_row(['sum', self.sum])
        table.add_row(['n', self.length])
        table.add_row(['middel', self.middel])
        table.add_row(['obs', self.obs])
        table.add_row(['hyppighed', self.hyppighed])
        table.add_row(['varians', self.varians])
        table.add_row(['spredning', self.spredning])
        table.add_row(['min', self.min])
        table.add_row(['max', self.max])
        table.add_row(['variationsbredde', self.variationsbredde])
        print(table)

    def g_hyppighed(self):
        self.data.sort()
        for entry in self.data:
            if entry not in self.obs:
                #self.obs[entry] = 'unasigned'
                self.obs.append(entry)
        else:
            for obs in self.obs:
                self.hyppighed[obs] = self.data.count(obs)
            #else:
                #print(self.hyppighed)
                #for obs, hyppighed in self.hyppighed.items():
                    #print(obs, hyppighed)

    def g_varians(self):
        for entry in self.data:
            self.varians += math.pow((entry - self.middel),2)
        else:
            self.varians = self.varians / self.length
            #print(self.varians)


    def g_spredning(self):
        self.spredning = math.sqrt(self.varians)
        #print(self.spredning)




#obs.length -= 1
#obs.printOut()
#obs.g_hyppighed()
#print(obs.hyppighed)
#obs.g_varians()
#obs.g_spredning()
#print(obs.min, obs.max, obs.variationsbredde)
