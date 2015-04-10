
from simulation.core import Core
from simulation.machine import Machine

class T(Core):
    
    def startup(self):
        x, y = self.getNode().nodeID()
        print 'Node %d, %d, core %d' % (x, y, self.coreID())


m = Machine(T)


