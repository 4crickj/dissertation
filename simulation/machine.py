

from node import Node


class Machine(object):
	
	def __init__(self, core_class, nodes=48):
		self.nodes = []
		self.core_class = core_class
		
		for i in range(48):
			self.nodes.append(Node(i+1, core_class))



