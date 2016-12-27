#!/usr/bin/python3
# coding: utf-8
# Base code for exercise 1.7 on Sethna's book on Stat. Mech. regarding small networks

import numpy as np


class SmallNetwork(object):
    """
    Main class for creating a small network object. Nodes will be represented by integers and the network consists of
    consecutive integers.
    """
    def __init__(self, L, Z, p):
        """
        Constructor of class SmallNetwork
        :param L: Number of nodes of the network
        :param Z: Short edges, fixed minimum of connection to closest neighbors
        :param p: Probability of having extra random connection added to the network (shortcut)
        """
        self.L = L
        self.Z = Z
        self.p = p

        self.nodes = list(range(L))  # Node list from 0 to L-1

        # Make list of edges (list of lists), index is node
        self.edges = []
        # Adding the fixed neighbors
        for i in self.nodes:
            self.edges.append(self.get_neighbors(i))
        # Adding random shortcuts
        for i in self.nodes:
            for j in range(i+1,max(self.nodes)+1):
                if np.random.uniform() <= self.p:
                    self.add_edge(i,j)


    def has_node(self, node):
        """
        Function which checks to see if a node is already in the network
        :param node: Node to check if exists in the network
        :return: True if the node exists, False otherwise.
        """
        assert type(node) is int, "Node %r is not a integer" % node  # Type should be int
        if node in self.nodes:
            return True
        else:
            return False
        # assert node in self.nodes, "node %r is not in the list of nodes" % node

    def add_node(self):
        """
        Adds a new node to the system (if it is not already there)
        :return: None
        """
        tmp_nodes.append(len(self.nodes))  # Append the next consecutive integer as a node
        self.L += 1  # Increase number of nodes L by an unit
        self.nodes = tmp_nodes

    def add_edge(self, node1, node2):
        """
        Adds a new edge/connection between two nodes to the system
        :param node1: First node to add edge
        :param node2: Second node to add edge
        :return: None
        """
        if node2 not in self.edges[node1] and node1 not in self.edges[node2]:
            self.edges[node1].append(node2)
            self.edges[node2].append(node1)
        else:
            pass

    def get_nodes(self):
        """
        Returns a list of existing nodes
        :return: List of existing nodes
        """
        return self.nodes

    def get_neighbors(self, node):
        """
        Returns the neighbors of an existing node
        :param node: Node to get neighbors from
        :return: List of neighbors of node
        """
        if self.has_node(node):
            low_neighbor = int((node - 0.5 * self.Z) % self.L)
            neighbors = []
            for i in range(self.Z + 1):
                neighbor = (low_neighbor + i) % self.L
                # print(neighbor, node)
                if neighbor == node:
                    pass
                else:
                    neighbors.append(neighbor)
        else:
            raise ValueError("Node %r is not part of the network" % node)
        return neighbors