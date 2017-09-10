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
        self.edges = {}
        # Adding the fixed/short edges
        for i in self.nodes:
            self.edges[i] = self.get_closest(i)

        self.add_rand_shortcuts()  # This adds the random shortcuts according to what the book says


    # Truly random shortcuts given probability p
    # This is not what the book asks but it's fun to play with :)
    def random_shortcuts(self):
        """
        This method adds truly random connections/edges according to the value of p. This is just for fun.
        :return: None
        """
        # Adding random shortcuts
        for i in self.nodes:
            for j in range(i + 1, max(self.nodes) + 1):
                if np.random.uniform() <= self.p:
                    self.add_edge(i, j)

    def add_rand_shortcuts(self):
        """
        Adds random shortcuts up to p*L*Z/2 as the book suggests
        :return: None
        """
        num_shortcuts = np.int(np.round(self.p * self.L * 0.5 * self.Z)) # Number of shortcuts p*L*Z/2
        for i in range(num_shortcuts):
            node1 = np.int(np.round(np.random.uniform() * (len(self.nodes)-1)))
            node2 = np.int(np.round(np.random.uniform() * (len(self.nodes)-1)))
            self.add_edge(node1, node2)

    def has_node(self, node):
        """
        Function which checks to see if a node is already in the network
        :param node: Node to check if exists in the network
        :return: True if the node exists, False otherwise.
        """
        assert type(node) is int, "Node %r is not an integer" % node  # Type should be int
        if node in self.nodes:
            return True
        else:
            return False

    def add_node(self, node):
        """
        Adds a new arbitrary node to the system (if it is not already there)
        :return: None
        """
        assert type(node) is int, "Node %r is not an integer" % node  # Type should be int
        if not self.has_node(node):
            self.nodes.append(node)
            self.L += 1  # Increase number of nodes L by an unit
            self.edges[node] = []  # Initialize edges of node as empty
            print("Added node %r." % node)
        else:
            print("Node is already on the network. Nothing to do.")

    def add_node_ordered(self):
        """
        Adds a new ordered node. Static way depending on size
        :return:
        """
        self.nodes.append(len(self.nodes))  # Append the next consecutive integer as a node
        self.L += 1  # Increase number of nodes L by an unit

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

    def get_closest(self, node):
        """
        Returns the closest nodes to the given node. These are the neighbors attached only by short edges.
        :param node: Node to get neighbors from
        :return: List of neighbors of node
        """
        if self.has_node(node):
            low_closest = int((node - 0.5 * self.Z) % self.L)
            closest = []
            for i in range(self.Z + 1):
                neighbor = (low_closest + i) % self.L
                # print(neighbor, node)
                if neighbor == node:
                    pass
                else:
                    closest.append(neighbor)
        else:
            raise ValueError("Node %r is not part of the network" % node)
        return closest

    def get_neighbors(self, node):
        """
        Return the neighbors of an existing node by returning its edges.
        """
        assert type(node) is int, "Node represented by %r is not an integer" % node  # Type should be int
        return self.edges[node]
