

class Packet(object):
	
	def __init__(self, source, payload):
		self.source = source
		self.payload = payload
		self.hop = 0

	def getType(self):
		return 0

	def getSource32(self):
		return self.source

	def getPayload32(self):
		return self.payload

	def getHop(self):
		return self.hop
	
	def incHop(self):
		self.hop += 1

