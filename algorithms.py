
def iode_float_tick(iode):
    pass


def iode_int_tick(iode):
    # Get the amounts per input iode node
    input_amount_per_iode_node = []
    for iode_node in iode.input_nodes:
        input_amount_per_iode_node.append(min(iode_node.amount, iode.speed['input']))

    # Get the amounts per output iode node
    output_amount_per_iode_node = []
    for iode_node in iode.output_nodes:
        output_amount_per_iode_node.append(iode.speed['output'])

    # Get the maximum throughput
    max_thru_speed = int(iode.speed['throughput'])
    input_amount_total = sum(input_amount_per_iode_node)
    output_amount_total = sum(output_amount_per_iode_node)

    # Compare the maximum throughput
    diff_input_thru_max = int(input_amount_total - max_thru_speed)
    diff_output_thru_max = int(output_amount_total - max_thru_speed)

    # Lessen the input if the maximum throughput is smaller
    if diff_input_thru_max > 0:
        for i in xrange(len(iode.input_nodes)):
            pass  # TODO: figure out this

    # Lessen the output if the maximum throughput is smaller
    if diff_output_thru_max > 0:
        for i in xrange(len(iode.input_nodes)):
            pass  # TODO: figure out this

    # Move the numbers from the inputs
    for i, inode in enumerate(iode.input_nodes):
        inode.take(input_amount_per_iode_node[i])

    # Move the numbers into the outputs
    for i, inode in enumerate(iode.output_nodes):
        inode.give(output_amount_per_iode_node[i])
