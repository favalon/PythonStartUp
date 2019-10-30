import numpy as np
import math
import random

class nodes:
    def __init__(self, start_time, duration, cost):
        self.start_time = start_time
        self.duration = duration
        self.cost = cost
    
    def set_startTime(self, start_time):
        self.start_time = start_time
        return 0
    
    def set_duration(self,duration):
        self.duration = duration
        return 0
    
    def set_cost(self,cost):
        self.cost = cost
        return 0

    def get_start_time(self):
        return self.start_time
    
    def get_duration(self):
        return self.duration
    
    def get_cost(self):
        return self.cost

    

def create_fake_node(full_time, sequence_time):
    max_seq_time = max(sequence_time)
    start_time = np.zeros((int((max_seq_time+1)*max_seq_time/2), len(sequence_time)))
    duration = np.zeros((int((max_seq_time+1)*max_seq_time/2), len(sequence_time)))
    node_cost = np.zeros((int((max_seq_time+1)*max_seq_time/2), len(sequence_time)))

    print(duration)
    # initial start time and duration
    sp = 0
    timer = 0
    # initial 0 duration:
    duration[0, :] = 0
    
    for i in range(len(sequence_time)):
        # intial zero duration sequence, start at start time and end at start time
        start_time[0, i] = sp
        for j in range(1, sequence_time[i]):
            col_start = (int(j*(j+1)/2))
            col_end = col_start - j - 1
            for p in range(col_start, col_end):
                start_time[j, col_start:col_start+p] = sp+p

            print(start_time)

        # update start time
        sp = sp + sequence_time[i]
    
    return 0

if __name__ == "__main__":
    
    create_fake_node(20, [5, 6, 3, 2, 4])


    pass