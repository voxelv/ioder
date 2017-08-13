
from iode import Iode, IodeNode


def main():
    iode = Iode()

    input_nodes = []
    for node_amount in [23, 6]:
        node = IodeNode(node_amount)
        input_nodes.append(node)
        iode.add_input_node(node)

    output_nodes = []
    for node_amount in [4, 0]:
        node = IodeNode(node_amount)
        output_nodes.append(node)
        iode.add_output_node(node)

    iode.tick()

    print "Actual:   {}, {}".format(input_nodes, output_nodes)
    print "Expected: [19, 2], [8, 4]"

if __name__ == "__main__":
    main()
