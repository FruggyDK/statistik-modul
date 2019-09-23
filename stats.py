import math

class data:
    def __init__(self, data):
        self.data = data
        self.sum = sum(data)
        self.length = len(data)
        self.middel = self.sum / self.length
        self.obs = {}

    def printOut(self):
        self.data.sort()
        print(self.data)
        print(self.sum)
        print(self.length)
        print(self.middel)

    def hyppighed(self):
        self.data.sort()
        for entry in self.data:
            print(entry)
            if entry not in self.obs:
                self.obs[entry] = 'unasigned'
        else:
            for obs in self.obs:
                self.obs[obs] = self.data.count(obs)
            else:
                print(self.obs)



obs = data([1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3, 20])
#obs.printOut()
obs.hyppighed()


