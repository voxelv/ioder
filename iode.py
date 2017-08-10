
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


class IodeItemStack(object):
        def __init__(self, typ):
            self.typ = typ


class IodeNode(Lockable):
    def __init__(self, typ="", amt=0, ):
        super(IodeNode, self).__init__()
        self.typ = str(typ)
        self.amt =


class Iode(Lockable):
    """
    An Iode is a connection object. 
    It connects 'from' nodes to 'into' nodes and knows how to distribute the flow.
    """

    def __init__(self, typ=""):
        super(Iode, self).__init__()

        self.from_nodes = []
        self.into_nodes = []

        self.from_node_speed = config['iode_from_node_speed']
        self.from_into_speed = config['iode_into_node_speed']

    @Lockable.lock_wrapper
    def add_from_node(self, node):
        self.from_nodes.append(node)

    @Lockable.lock_wrapper
    def add_into_node(self, node):
        self.into_nodes.append(node)

    @Lockable.lock_wrapper
    def tick(self):
        from_buffer =
