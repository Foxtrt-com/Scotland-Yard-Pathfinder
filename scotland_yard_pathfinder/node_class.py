# node_class.py

class Node:
    def __init__(self, node_index, taxi_nodes, bus_nodes, underground_nodes):
        self.node_index = node_index
        self.taxi_nodes = taxi_nodes
        self.bus_nodes = bus_nodes
        self.underground_nodes = underground_nodes
