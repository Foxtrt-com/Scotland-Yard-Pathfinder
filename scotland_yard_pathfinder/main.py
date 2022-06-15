# main.py
from nodes import nodes


def main():
    for node in nodes:
        print(node.node_index)


if __name__ == '__main__':
    main()
