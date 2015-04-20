"""
core.py

A single CPU.
"""

from threading import Thread
from Queue import Queue


class CoreThread(Thread):
    
    def __init__(self, core, **args):
        Thread.__init__(self, **args)
        self.core = core
        self.stop = False
    
    def run(self):
        self.core.startup()
        
        if self.stop:
        	return
        
        while True:
            p = self.core.queue.get()
            self.core.interruptPacket(p)
            
            if self.stop:
                break


class Core(object):

	def __init__(self, node, id):
		self.node = node
		self.id = id
		self.thread = CoreThread(self)
		self.queue = Queue()
	
	def start(self):
	    self.thread.start()
    
    # The following methods are to be overidden by a subclass
    # in order to define the code on the core
	
	def startup(self):	# Overridden
		pass
	
	def interruptPacket(self, source, payload):	# Overridden
		pass
	
	def interruptTimer(self):	# Overridden
		pass
	
	# The following methods are only to be called from within the overidden
	# methods above

	def setPeriod(self, p):
		pass
	
	def sendPacket(self, payload):
		self.node.getRouter().sendPacket(0, payload)
	
	def stopCPU(self):
		self.thread.stop = True
	
	# General munge can be called from anywhere

	def coreID(self):
		return self.id

	def getNode(self):
		return self.node





