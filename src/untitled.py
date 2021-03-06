import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

x = np.loadtxt('1msd.file',delimiter=' ', skiprows=3) 
l = np.log10(x)
coff = np.polyfit(l[4:200,0], l[4:200,1], 1)
poly = np.poly1d(coff)
ys1 = poly(l[4:200,0])
funy1 = str(coff[0])+'x'+ str(coff[1]+4)
coeff = np.polyfit(l[5000:,0], l[5000:,1], 1)
polynomial = np.poly1d(coeff)
ys = polynomial(l[5000:,0])
funy = str(coeff[0])+'x'+ str(coeff[1])
sns.set_style()
plt.plot(l[4:200,0], ys1+0.5,'--b',label=funy1)
plt.plot(l[5000:,0], ys-0.5,'--g',label=funy)
plt.plot(l[:,0],l[:,1],label='MSD')
plt.legend()
plt.savefig('MSD*0',dpi= 250)
plt.show()
print(coeff) 
