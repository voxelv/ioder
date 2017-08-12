
from multiprocessing import Lock


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
