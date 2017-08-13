
# Internal modules
from config import config as cfg
from algorithms import iode_int_tick


class IodeNode:
    def __init__(self, amount=0):
        self.stack = None
        self.amount = amount

    def take(self, amount):
        amount_to_take = min(amount, self.amount)
        self.amount -= amount_to_take
        return amount_to_take

    def give(self, amount):
        amount_to_give = amount
        self.amount += amount_to_give
        return amount_to_give

    def __repr__(self):
        return str(self.amount)


class Iode:
    """
    An Iode is a connection object. 
    It connects 'input' nodes to 'output' nodes and knows how to distribute the flow.
    """

    def __init__(self, typ=""):

        self.typ = str(typ)

        # Node lists
        self.input_nodes = []
        self.output_nodes = []

        self.speed = {
            'input': cfg['default_iode_speed_input'],
            'throughput': cfg['default_iode_speed_throughput'],
            'output': cfg['default_iode_speed_output'],
        }

    def add_input_node(self, node):
        self.input_nodes.append(node)

    def add_output_node(self, node):
        self.output_nodes.append(node)

    def tick(self):
        iode_int_tick(self)
