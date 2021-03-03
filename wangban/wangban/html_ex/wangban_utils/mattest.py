import time
import matplotlib.pyplot as plt 

import numpy as np 

x = np.linspace(0,10,30)
#plt.plot(x,np.sin(x))
#plt.plot(x,np.sin(x),'-o')
#plt.scatter(x,np.sin(x))
#
#rng = np.random.RandomState(0)
#x = rng.randn(100)
#y = rng.randn(100)
#colors = rng.rand(100)
#sizes  = 1000*rng.rand(100)
#plt.scatter(x,y,c=colors,s=sizes,alpha=0.3,cmap='viridis')
#plt.colorbar()
#
#x = np.linspace(0,10,50)
#dy = 0.8
#y = np.sin(x) + dy*np.random.randn(50)
#plt.errorbar(x,y,yerr=dy,fmt=".k")
#
#x = [1,2,3,4,5,6,7,8]
#y = [3,1,4,5,8,9,7,2]
#label = ['A','B','C','D','E','F','G','H']
#plt.bar(x,y,tick_label=label)
#plt.barh(x,y,tick_label=label)
#data = np.random.randn(1000)
#plt.hist(data)
#plt.hist(data, bins=30,histtype='stepfilled')
#
#x1 = np.random.normal(0,0.8,1000)
#x2 = np.random.normal(-2,1,1000)
#x3 = np.random.normal(3,2,1000)
#
#kwargs = dict(alpha=0.3,bins=40)
#
#plt.hist(x1,**kwargs)
#plt.hist(x2,**kwargs)
#plt.hist(x3,**kwargs)

#mean = [0,0]
#cov = [[1,1],[1,2]]
#x,y = np.random.multivariate_normal(mean,cov,10000).T
##plt.hist2d(x,y,bins=30)
#plt.hexbin(x,y,gridsize=30)
#
#x = np.linspace(0,10,100)
#plt.plot(x,np.sin(x),'--')
#
#x = np.linspace(0,10,100)
#plt.plot(x,np.sin(x))
#plt.ylim(-1.5,1.5)
#
#x = np.linspace(0.05,10,100)
#y = np.sin(x)
#plt.plot(x,y,label='sin(x)')
#plt.xlabel('variable x')
#plt.ylabel('value y')
#
#x = np.linspace(0.05,10,100)
#y = np.sin(x)
#plt.plot(x,y,label="sin(x)")
#plt.title("三角函数")
#
#x = np.linspace(0.05,10,100)
#y = np.sin(x)
#plt.plot(x,y)
#plt.grid()
#
#x = np.linspace(0.05,10,100)
#y = np.sin(x)
#plt.plot(x,y)
#plt.axhline(y=0.8,ls='--',c='r')

#x = np.linspace(0.05,10,100)
#y = np.sin(x)
#plt.plot(x,y)
#plt.axvspan(xmin=4,xmax=6,facecolor='r',alpha=0.3)
#plt.axhspan(ymin=-0.2,ymax=0.2,facecolor='y',alpha=0.3)
#
#x = np.linspace(0.05,10,100)
#y = np.sin(x)
#plt.plot(x,y)
#plt.text(3.2,0,'sin(x)',weight='bold',color='r')
#
#x = np.linspace(0.05,10,100)
#y = np.sin(x)
#plt.plot(x,y)
#plt.annotate('maximum',xy=(np.pi/2,1),
#   weight='bold',
#   color='r',
#   arrowprops=dict(arrowstyle='->',connectionstyle='arc3',color='r'))
#
#x = np.linspace(0,10,1000)
#fig,ax = plt.subplots()
#ax.plot(x,np.sin(x),label='sin')
#ax.plot(x,np.cos(x),'--',label='cos')
#ax.legend()
#ax.legend(loc='upper left',frameon=False)
#ax.legend(frameon=False,loc='lower center',ncol=2)
#y = np.sin(x[:,np.newaxis]+np.pi*np.arange(0,2,0.5))
#print(x[:,np.newaxis]+np.pi*np.arange(0,2,0.5))
#lines = plt.plot(x,y[:,1])
#print(len(lines))
#plt.legend(lines[:2],['first','second'])
#
fig,ax = plt.subplots()
lines = []
styles = ['-','--','-.',':']
x = np.linspace(0,10,1000)
for i in range(4):
    lines += ax.plot(x,np.sin(x-i*np.pi/2),styles[i],color='black')
ax.axis('equal')




plt.show()
