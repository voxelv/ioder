
from multiprocessing import Lock
from config import config


class Lockable(object):
    def __init__(self):
        self.lock_obj = Lock()

    def lock(self):
        self.lock_obj.acquire()

    def unlock(self):
        self.lock_obj.release()

    @staticmethod
    def lock_wrapper(original_function):
        def new_function(lockable, *args, **kwargs):
            lockable.lock()
            original_function(lockable, *args, **kwargs)
            lockable.unlock()
        return new_function


class IodeNode(Lockable):
    def __init__(self, typ="", amt=0, ):
        super(IodeNode, self).__init__()
        self.typ = str(typ)
        self.amt = amt # TODO: FIX


class Iode(Lockable):
    """
    An Iode is a connection object. 
    It connects 'from' nodes to 'into' nodes and knows how to distribute the flow.
    """

    def __init__(self, typ=""):
        super(Iode, self).__init__()

        self.from_nodes = []
        self.into_nodes = []

        self.speed = config['default_iode_speed']

    @Lockable.lock_wrapper
    def add_from_node(self, node):
        self.from_nodes.append(node)

    @Lockable.lock_wrapper
    def add_into_node(self, node):
        self.into_nodes.append(node)

    @Lockable.lock_wrapper
    def tick(self):
        from_buffer = 0 # TODO: FIX
