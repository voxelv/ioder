def iode_ticker(original_function):
    def new_function(iode, *args, **kwargs):
        if isinstance(iode, Iode):
            original_function(*args, **kwargs)
        else:
            print "[{}] {}".format("DBG", "error ticking object: {}".format(iode))
    return new_function


@iode_ticker
def iode_float_tick(iode):
    pass


@iode_ticker
def iode_int_tick(iode):
    input_amount_per_iode_node = []
    for iode_node in iode.input_nodes:
        input_amount_per_iode_node.append(min(iode_node.stack.amount, iode.speed['input']))

    output_amount_per_iode_node = []
    for iode_node in iode.output_nodes:
        output_amount_per_iode_node.append(min(iode_node.stack.amount, iode.speed['output']))

    max_thru_speed = int(iode.speed['thru'])
    input_amount_total = sum(input_amount_per_iode_node)
    output_amount_total = sum(output_amount_per_iode_node)
    diff_input_thru_max = int(input_amount_total - max_thru_speed)
    diff_output_thru_max = int(output_amount_total - max_thru_speed)

    if diff_input_thru_max > 0:
        for i in xrange(len(iode.input_nodes)):
            pass  # TODO: figure out this

    if diff_output_thru_max > 0:
        for i in xrange(len(iode.input_nodes)):
            pass  # TODO: figure out this

    for i, inode in enumerate(iode.input_nodes):
        inode.stack.take(input_amount_per_iode_node[i])

    for i, inode in enumerate(iode.output_nodes):
        inode.stack.give(output_amount_per_iode_node[i])
