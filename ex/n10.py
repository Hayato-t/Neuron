#----------------------------------
# n10.py: Network Connection
#
import os
import copy
import numpy as np
import matplotlib.pyplot as plt
from neuron import h

#   class definition
class HHneuron():
    def __init__(self):
        self.soma = h.Section()
        self.ap_dend = h.Section()

        self.soma.L = 30.0
        self.soma.diam = 30.0
        self.soma.nseg = 1
        self.soma.insert('hh')

        self.ap_dend = h.Section()
        self.ap_dend.L = 500.0
        self.ap_dend.diam = 2
        self.ap_dend.nseg = 23
        self.ap_dend.insert('hh')
        self.ap_dend.gnabar_hh = 0.012
        self.ap_dend.gkbar_hh = 0.0036
        self.ap_dend.gl_hh = 0.00003
        self.ap_dend.connect(self.soma, 1.0, 0)

# synaptic input
        self.esyn = h.Exp2Syn(0.5, sec=self.ap_dend) #syn points to ap_dend,0.5
        self.esyn.tau1 = 0.5
        self.esyn.tau2 = 1.0
        self.esyn.e = 0
# end of class HHneuron

# cells
hh_neuron = [HHneuron() for i in range(2)]

# synapse
stim = h.NetStim(0.5)
stim.interval = 20.0
stim.number = 3
stim.start = 20.0
stim.noise = 0

# connections
nclist = []
nclist.append(h.NetCon(stim,hh_neuron[0].esyn, 0.0,0,0.2))
nclist.append(h.NetCon(hh_neuron[0].soma(0.5)._ref_v,hh_neuron[1].esyn,10,1,-0.02))

tstop = 100
dt = 0.01
v_init = -65

cvode = h.CVode()
cvode.active(1)
cvode.atol(1.0e-5)
a = []
b = np.zeros(3)

h.finitialize(v_init)

while h.t < tstop:
    cvode.solve() #cvode.solve() -> calculate by defalt steps | cvode.solve(h.t+dt) -> calculate by dt steps
    b[0] = h.t
    b[1] = hh_neuron[0].soma(0.5).v
    b[2] = hh_neuron[1].soma(0.5).v
    print '%lf,%lf,%lf' %(b[0],b[1],b[2])
    a.append(copy.deepcopy(b))
a=np.array(a)
print 'Calculation Complete.'
for i in range(1,3):
    plt.plot(a[:,0],a[:,i])

plt.xlim([0,tstop])
plt.ylim([-100,100])
plt.show()
#exit()
