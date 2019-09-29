from stats import data
from prettytable import PrettyTable
table = PrettyTable()

class input:
    def __init__(self, input):
        self.input = input

obs = data([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,5,1,1])
obs.g_hyppighed()
obs.g_varians()
obs.g_spredning()
obs.printOut()

table.field_names = ["#", "n"]

table.add_row(["sum", obs.sum])
table.add_row(["n", obs.length])
table.add_row(["middel", obs.middel])
print(table)

