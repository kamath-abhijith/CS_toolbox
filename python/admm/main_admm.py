import sys
sys.path.insert(1,'/Users/abijithjkamath/Desktop/TECHNOLOGIE/Research/CS_Toolbox/python/')

import numpy as np

from scipy.io import loadmat

from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import rcParams

from cs_pkg import *

## Load signal and dictionary
load_dict_f = loadmat('/Users/abijithjkamath/Desktop/TECHNOLOGIE/Research/CS_Toolbox/python/hw1problem3.mat')

A = load_dict_f['Psi']
b = load_dict_f['f']

x_admm1, loss1 = pursuit_admm(A,b,0.5,1.5)
b_rec_admm1 = A.dot(x_admm1)

eb_admm1 = b-b_rec_admm1
eb_admm1_norm = np.linalg.norm(eb_admm1)
eb_admm1_norm_db = 20*np.log10(eb_admm1_norm)
print("l2 norm of the error using 0.5 and 1.5: ",eb_admm1_norm_db,"dB")

x_admm2, loss2 = pursuit_admm(A,b,.1,1.8)
b_rec_admm2 = A.dot(x_admm2)

eb_admm2 = b-b_rec_admm2
eb_admm2_norm = np.linalg.norm(eb_admm2)
eb_admm2_norm_db = 20*np.log10(eb_admm2_norm)
print("l2 norm of the error using ADMM: 0.3 and 1.8",eb_admm2_norm_db,"dB")

## Plots
style.use('bmh')
# style.use('ggplot')
# style.use('dark_background')

rcParams['text.usetex'] = True
rcParams.update({'font.size': 24})

fig1 = plt.figure(1)
plt.plot(b,color='green',label='True')
plt.plot(b_rec_admm1,'--',color='blue',label=r'$\lambda=0.5,\rho=1.5$')
plt.plot(b_rec_admm2,'--',color='red',label=r'$\lambda=0.1,\rho=1.8$')
plt.xlabel(r'$m$')
plt.ylabel(r'$\mathbf{b}$')
plt.title(r'Reconstruction')
plt.legend()
fig1.savefig('/Users/abijithjkamath/Desktop/TECHNOLOGIE/Courses/RTP IISc/E9 203 Compressed Sensing/01_01.pdf',bbox_inches='tight')

fig2 = plt.figure(2)
plt.stem(x_admm1.real,'-b',markerfmt='bo',label=r'$\lambda=0.5,\rho=1.5$')
plt.stem(x_admm2.real,'-r',markerfmt='ro',label=r'$\lambda=0.1,\rho=1.8$')
plt.xlabel(r'$N$')
plt.ylabel(r'$\mathbf{x}$')
plt.title(r'Sparse Code')
# plt.legend()
fig2.savefig('/Users/abijithjkamath/Desktop/TECHNOLOGIE/Courses/RTP IISc/E9 203 Compressed Sensing/01_02.pdf',bbox_inches='tight')

fig3 = plt.figure(3)
plt.plot(loss1,color='blue',label=r'$\lambda=0.5,\rho=1.5$')
plt.plot(loss2,color='red',label=r'$\lambda=0.1,\rho=1.8$')
plt.xlabel(r'Iterations')
plt.ylabel(r'$\frac{1}{2}\Vert A\mathbf{x}-\mathbf{b} \Vert_{2}^2 + \lambda \Vert \mathbf{x} \Vert_{1}$')
plt.title(r'Convergence')
# plt.legend()
fig3.savefig('/Users/abijithjkamath/Desktop/TECHNOLOGIE/Courses/RTP IISc/E9 203 Compressed Sensing/01_03.pdf',bbox_inches='tight')

plt.show()