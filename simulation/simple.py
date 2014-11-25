#!/usr/bin/env python

"""
simple.py

Simple simulation of distributed computation
of trapezoidal integration.

# mpiexec -n 5 python simple.py
"""


from mpi4py import MPI
import math


comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # Process number
size = comm.Get_size()  # Number of processes


if rank == 0:
    values = {
        'start_x': 0.0,   # Range of x values
        'end_x': 10.0,
        'segments': 1000 # Number of slices
    }
    
    values['segment_size'] = (values['end_x'] - values['start_x'])/values['segments']
else:
    values = None


def f(x):   # Function to integrate
    return x*x + 3*x - 1


# Broadcast info from root to all processes
values = comm.bcast(values)



if rank == 0:   # We are the coordinator process
    print "Coordinator started."
    
    total = 0
    
    for i in range(size-1):
        total += comm.recv(source=MPI.ANY_SOURCE)
    
    print "TOTAL VALUE = %d." % total


if rank > 0:    # We are a worker process
    print "Process %d started." % rank
    
    # Work out range of values to calculate
    # based on process number
    
    proc = rank-1
    n_proc = size-1
    p_proc = int(math.ceil(values['segments']/n_proc))
    x = values['start_x'] + (proc * values['segment_size'] * p_proc)
    
    total = 0
    
    for i in range(p_proc):
        total += ((f(x) + f(x + values['segment_size'])) / 2) * values['segment_size']
        
        x += values['segment_size']
        
        if x == values['end_x']:
            break
    
    comm.send(total, 0)
    print "Process %d sent total %d." % (rank, total)
    
    

