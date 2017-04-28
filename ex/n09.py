#----------------------------------
# n09.py: soma + dendrite synaptic input
#
import os
import copy
import numpy as np
import matplotlib.pyplot as plt
from neuron import h

soma = h.Section()
ap_dend = h.Section()

soma.L = 30.0
soma.diam = 30.0
soma.nseg = 1
soma.insert('hh') 

ap_dend.L = 500.0
ap_dend.diam = 2
ap_dend.nseg = 23
ap_dend.insert('hh')

ap_dend.gnabar_hh = 0.012
ap_dend.gkbar_hh = 0.0036
ap_dend.gl_hh = 0.00003

ap_dend.connect(soma, 1.0, 0)

# synaptic input

syn = h.AlphaSynapse(0.5, sec=ap_dend) #syn points to ap_dend,0.5
syn.onset = 5.0
syn.tau = 0.1
syn.gmax = 0.05

cvode = h.CVode()
cvode.active(1)
cvode.atol(1.0e-5)


a = []
b = np.zeros(4)
dt = 0.01
tstop = 20
v_init = -65

h.finitialize(v_init)
while h.t < tstop:
    cvode.solve() #cvode.solve() -> calculate by defalt steps | cvode.solve(h.t+dt) -> calculate by dt steps
    b[0] = h.t
    b[1] = soma(0.5).v
    b[2] = ap_dend(0.1).v
    b[3] = ap_dend(0.9).v
    print '%lf,%lf,%lf,%lf' %(b[0],b[1],b[2],b[3])
    a.append(copy.deepcopy(b))
a=np.array(a)
print 'Calculation Complete.'
for i in range(1,4):
    plt.plot(a[:,0],a[:,i])

plt.xlim([0,tstop])
plt.ylim([-100,100])
plt.show()
#exit()
