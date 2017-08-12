
# Python modules
from fractions import Fraction

# Internal modules
from util import Lockable
from config import config as cfg
from algorithms import iode_float_tick, iode_int_tick


class IodeTransportableStack(object):

    def __init__(self, typ="", amt=0):
        self.typ = str(typ)
        self.amt = Fraction(str(amt)).limit_denominator(cfg['max_denominator'])


class IodeNode(Lockable):
    def __init__(self):
        super(IodeNode, self).__init__()
        self.stack = None

    @Lockable.lock_wrapper
    def set_stack(self, stack):
        self.stack = stack

    @Lockable.lock_wrapper
    def take(self, amt):
        amt_to_take = min(amt, self.stack.amt)
        self.stack.amt -= amt_to_take
        return amt_to_take

    @Lockable.lock_wrapper
    def give(self, amt):
        amt_to_give = amt
        self.stack.amt += amt_to_give
        return amt_to_give


class Iode(Lockable):
    """
    An Iode is a connection object. 
    It connects 'from' nodes to 'into' nodes and knows how to distribute the flow.
    """

    def __init__(self, typ=""):
        super(Iode, self).__init__()

        self.typ = str(typ)

        # Node lists
        self.from_nodes = []
        self.into_nodes = []

        self.speed = {
            'from': cfg['default_iode_speed_from'],
            'thru': cfg['default_iode_speed_thru'],
            'into': cfg['default_iode_speed_into'],
        }

    @Lockable.lock_wrapper
    def add_from_node(self, node):
        self.from_nodes.append(node)

    @Lockable.lock_wrapper
    def add_into_node(self, node):
        self.into_nodes.append(node)

    @Lockable.lock_wrapper
    def tick(self):
        if self.typ in cfg['iodenode_float_types']:
            iode_float_tick(self)
        else:
            iode_int_tick(self)
