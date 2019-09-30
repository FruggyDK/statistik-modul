from stats import data
from prettytable import PrettyTable
table = PrettyTable()

class input:
    def __init__(self, input):
        self.input = input

obs = data([32,32,32,32,33,33,33,33,33,33,33,33,34,34,35,35,35,35,36,36,36,37,37,37,38,38,38,38,39,41])
obs.g_hyppighed()
obs.g_varians()
obs.g_spredning()
obs.print()
#obs.printOut()

