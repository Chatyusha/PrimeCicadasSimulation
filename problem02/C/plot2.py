import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ymax = 13000
time = 200
with open('output') as f:
    data = [i.strip() for i in f.readlines()]

elems = np.array([i.split(" ") for i in data])
x = elems[:,0]
y_10 = elems[:,1]
y_13 = elems[:,2]
x = np.array([int(i) for i in x.tolist()])
y_10 = np.array([int(i) for i in y_10.tolist()])
y_13 = np.array([int(i) for i in y_13.tolist()])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot(x,y_10,label="10year")
plt.plot(x,y_13,label="13year")
plt.legend(bbox_to_anchor=(0, 1), loc="upper left")

guid_10_x = [i for i in range(time) if i%10 == 0]
guid_13_x = [i for i in range(time) if i%13 == 0]

for i in guid_10_x:
    plt.plot([i]*ymax,np.array(range(ymax)),linestyle="--",color="cyan",linewidth=0.5)

for i in guid_13_x:
    plt.plot([i]*ymax,np.array(range(ymax)),linestyle="--",color="lime",linewidth=0.5)

plt.savefig('fig2.png')