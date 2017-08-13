
from iode import Iode, IodeNode


def main():
    iode = Iode()

    iode.add_from_node(IodeNode(23))
    iode.add_from_node(IodeNode(4))

    iode.add_into_node(IodeNode(4))
    iode.add_into_node(IodeNode(0))

    iode.tick()

if __name__ == "__main__":
    main()
