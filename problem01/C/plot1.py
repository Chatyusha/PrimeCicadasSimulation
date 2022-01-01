import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

with open('output') as f:
    data = [i.strip() for i in f.readlines()]

elems = np.array([i.split(" ") for i in data])
x = elems[:,0]
y = elems[:,1]
x = np.array([int(i) for i in x.tolist()])
y = np.array([int(i) for i in y.tolist()])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot(x,y)

for i in [i for i in range(100) if i%10==0]:
    plt.plot(np.array([i]*600),np.array(range(600)),linestyle='--',color="#000000", linewidth=0.5)

ax.set_xticks([1]+[i for i in range(1,100+1) if i%10==0])
ax.set_xticklabels([1]+[i for i in range(1,100+1) if i%10==0])
ax.set_xlabel('t')

plt.ylim([1, 600])
ax.set_yticks([i for i in range(600) if i%50==0])
plt.savefig('fig1.png')