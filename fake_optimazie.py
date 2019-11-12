import numpy as np
import math
import random

class nodes:
    def __init__(self, start_time, duration, cost, nodeIndex):
        self.start_time = start_time # start time of this node
        self.duration = duration # duration of this node
        self.cost = cost # node cost
        self.nodeIndex = nodeIndex # nodeIndex = (r, c)
        self.edgeCost = None # edgeCost = (nextNodeIndex, edgeCost)
    
    def set_startTime(self, start_time):
        self.start_time = start_time
        return 0
    
    def set_duration(self,duration):
        self.duration = duration
        return 0
    
    def set_cost(self,cost):
        self.cost = cost
        return 0
    
    def set_nodeIndex(self, nodeIndex):
        self.nodeIndex = nodeIndex
        return 0

    def set_edgeCost(self, edgeCost):
        self.edgeCost = edgeCost
        return 0

    def get_start_time(self):
        return self.start_time
    
    def get_duration(self):
        return self.duration
    
    def get_cost(self):
        return self.cost
    
    def get_nodeIndex(self):
        return self.nodeIndex
    
    def get_edgeCost(self):
        return self.edgeCost

    
def initial_seq_node(seq_len, seq_start, max_cost):
    nodes_number = int((seq_len-1)*(seq_len)/2 + 1)
    print(nodes_number)
    seq_start_time = [-1] # the first node has no duration and start time
    seq_duration = [0]
    # initial start time
    r = 0
    for i in range(1, nodes_number):
        for j in range(seq_len-1-r):
            seq_start_time.append(j)
            seq_duration.append(r+1)    
            i += 1
        r += 1

    assert nodes_number == len(seq_start_time), "seq_start_time initialize error"

    seq_nodes = []    
    for i in range(nodes_number):
        nodeIndex = (seq_start, seq_start_time[i], seq_duration[i])
        seq_nodes.append(nodes(seq_start_time[i], seq_duration[i], max_cost, nodeIndex))

    return seq_nodes

def initial_node_edgeCost(node, next_seq_len):
    next_nodes_number = int((next_seq_len-1)*(next_seq_len)/2 + 1)

    edgeCost = []
    for i in range(next_nodes_number):
        edgeCost.append(math.inf)

    node.set_edgeCost = edgeCost

def create_fake_node(full_time, seq_time):
    # initial_node
    seq_number = len(seq_time) # number of sequence
    max_cost = math.inf
    max_edgeCost = math.inf

    fake_nodes = []
    
    for i in range(seq_number):
        seq_nodes = initial_seq_node(seq_time[i], i, max_cost)
        if i == seq_number-1:
            pass
        else:
            for node in seq_nodes:
                initial_node_edgeCost(node, seq_time[i+1])
        fake_nodes.append(seq_nodes)

    
    return 0

if __name__ == "__main__":
    
    # a = initial_seq_node(5, 0, 10)
    # print (a)
    create_fake_node(20, [5, 6, 3, 2, 4])


    pass