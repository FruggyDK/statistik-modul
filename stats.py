import math

'''todo
     n
     total
     min
     max
     middel

     q1
     median
     q3

     variationsbredde
     kvartilvariation

     øvre grænse
     nedre grænse

     stikprøve
        varians
        spredning
     population
        varians
        spredning'''

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
        print("data: ",self.data)
        print("sum: ",self.sum)
        print("n: ",self.length)
        print("middel: ",self.middel)
        print("obs: ",self.obs)
        print("hyppighed: ",self.hyppighed)
        print("varians: ",self.varians)
        print("spredning: ",self.spredning)
        print("min: ",self.min)
        print("max: ",self.max)
        print("variationsbredde: ",self.variationsbredde)


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
