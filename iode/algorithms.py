from iode.iode import Iode, IodeNode
import multiprocessing


def iode_ticker(original_function):
    def new_function(iode, *args, **kwargs):
        if isinstance(iode, Iode):
            original_function(*args, **kwargs)

    return new_function


@iode_ticker
def iode_float_tick(iode):
    pass


@iode_ticker
def iode_int_tick(iode):
    from_amt_per_inode = []
    for inode in iode.from_nodes:
        from_amt_per_inode.append(min(inode.stack.amt, iode.speed['from']))

    into_amt_per_inode = []
    for inode in iode.into_nodes:
        into_amt_per_inode.append(min(inode.stack.amt, iode.speed['into']))

    max_thru_speed = int(iode.speed['thru'])
    from_amt_total = sum(from_amt_per_inode)
    into_amt_total = sum(into_amt_per_inode)
    diff_from_thru_max = int(from_amt_total - max_thru_speed)
    diff_into_thru_max = int(into_amt_total - max_thru_speed)

    if diff_from_thru_max > 0:
        for i in xrange(len(iode.from_nodes)):
            pass  # TODO: figure out this

    # if diff_into_thru_max... TODO

    for i, inode in enumerate(iode.from_nodes):
        inode.stack.take(from_amt_per_inode[i])

    for i, inode in enumerate(iode.into_nodes):
        inode.stack.give(into_amt_per_inode[i])
