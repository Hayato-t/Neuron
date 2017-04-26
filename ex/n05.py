#----------------------------------
# n05.py: a simple hh cell
#
import os
import copy
import numpy as np
import matplotlib.pyplot as plt
from neuron import h

soma = h.Section()
soma.insert('hh')

cvode = h.CVode()
cvode.active(1)
cvode.atol(1.0e-5)


a = []
b = np.zeros(2)
tstop = 200
v_init = -65

h.finitialize(v_init)
while h.t < tstop:
    cvode.solve()
    b[0] = h.t
    b[1] = soma(0.5).v
    print '%lf,%lf' %(b[0],b[1])
    a.append(copy.deepcopy(b))
a=np.array(a)
print 'Calculation Complete.'
plt.plot(a[:,0],a[:,1])
plt.show()
#exit()
