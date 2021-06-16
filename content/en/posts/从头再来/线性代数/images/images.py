import matplotlib.pyplot as plt

plt.arrow(x=0, y=0, dx=2, dy=-1,width=0.005,head_width=0.1,ec='r',fc='r')
plt.text(x=2.2,y=-1,s='(2,-1)')
plt.arrow(x=0, y=0, dx=-1, dy=2,width=0.005,head_width=0.1,ec='r',fc='r')
plt.text(x=-0.8,y=2,s='(-1,2)')

plt.arrow(x=0, y=0, dx=0, dy=3,width=0.005,head_width=0.1,ec='b',fc='b')
plt.text(x=0.2,y=3,s='(0,3)')


plt.xlim(xmin=-3,xmax=3)
plt.ylim(ymin=-1.5,ymax=3.5)
plt.grid(True)
plt.show()
