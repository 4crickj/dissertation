"""
node.py

A spinnaker node containing 16 usable cores.
"""

from simulation.core import Core
from simulation.router import Router


id_map = {
	1: (4,3),
	2: (3,3),
	3: (4,4),
	4: (5,4),
	5: (5,3),
	6: (4,2),
	7: (3,2),
	8: (2,2),
	9: (2,3),
	10: (3,4),
	11: (4,5),
	12: (5,5),
	13: (6,5),
	14: (6,4),
	15: (6,3),
	16: (5,2),
	17: (4,1),
	18: (3,1),
	19: (2,1),
	20: (1,1),
	21: (1,2),
	22: (1,3),
	23: (2,4),
	24: (3,5),
	25: (4,6),
	26: (5,6),
	27: (6,6),
	28: (7,6),
	29: (7,5),
	30: (7,4),
	31: (7,3),
	32: (6,2),
	33: (5,1),
	34: (4,0),
	35: (3,0),
	36: (2,0),
	37: (1,0),
	38: (0,0),
	39: (0,1),
	40: (0,2),
	41: (0,3),
	42: (1,4),
	43: (2,5),
	44: (3,6),
	45: (4,7),
	46: (5,7),
	47: (6,7),
	48: (7,7),
}


class Node(object):
	
	def __init__(self, id, cls):
		self.cores = []
		self.router = Router(self)
		self.id = id
		self.x, self.y = id_map[id]
		
		for i in range(18):
			self.cores.append(cls(self, i))
			self.cores[i].start()
	
	def getCore(self, n):
		return self.core[n]

	def getRouter(self):
		return self.router

	def nodeID(self):
		return self.x, self.y
	
	def wait(self):
	    for c in self.cores:
	        c.thread.join()




