
# Internal modules
from config import config as cfg
from algorithms import iode_int_tick


class IodeNode:
    def __init__(self):
        self.stack = None

    def set_stack(self, stack):
        self.stack = stack

    def take(self, amt):
        amt_to_take = min(amt, self.stack.amt)
        self.stack.amt -= amt_to_take
        return amt_to_take

    def give(self, amt):
        amt_to_give = amt
        self.stack.amt += amt_to_give
        return amt_to_give


class Iode:
    """
    An Iode is a connection object. 
    It connects 'from' nodes to 'into' nodes and knows how to distribute the flow.
    """

    def __init__(self, typ=""):

        self.typ = str(typ)

        # Node lists
        self.from_nodes = []
        self.into_nodes = []

        self.speed = {
            'from': cfg['default_iode_speed_from'],
            'thru': cfg['default_iode_speed_thru'],
            'into': cfg['default_iode_speed_into'],
        }

    def add_from_node(self, node):
        self.from_nodes.append(node)

    def add_into_node(self, node):
        self.into_nodes.append(node)

    def tick(self):
        iode_int_tick(self)
