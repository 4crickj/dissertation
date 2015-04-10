


from simulation.multicast_table import MulticastTable



class Router(object):
	
	def __init__(self, node):
		self.node = node
		self.mt = MulticastTable()

	def getMulticastTable(self):
		return self.mt

	def recievePacket(self, link):
		pass

	def sendPacket(self, p):
		pass

	def getNode(self):
		return self.node





