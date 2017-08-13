
from iode import Iode, IodeNode


def main():
    iode = Iode()

    input_nodes = []
    for node_amount in [23, 4]:
        node = IodeNode(node_amount)
        input_nodes.append(node)
        iode.add_input_node(node)

    output_nodes = []
    for node_amount in [4, 0]:
        node = IodeNode(node_amount)
        output_nodes.append(node)
        iode.add_output_node(node)

    iode.tick()

    print "Expected: [18, 0], [9, 5]"
    print "Actual:   {}, {}".format(input_nodes, output_nodes)

if __name__ == "__main__":
    main()
