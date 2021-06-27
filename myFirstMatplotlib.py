from matplotlib import pyplot as plt
import numpy as np
styles = plt.style.available
plt.style.use(styles[8])

x = [26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
y = [42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

plt.figure(facecolor=('#2f3136')) #set the outside face color
axes = plt.gca()
axes.set_facecolor('#2f3136') #set the inside face color
axes.yaxis.grid() #Set horizontal gridlines only

plt.plot(x, y, color = '#5865f2', linestyle='-', marker = 'o', label = 'All Devs') #plot the data
plt.tick_params(axis = "x", which = "both", bottom = True, top = False)#only want ticks on the bottem not the top
plt.tick_params(axis = "y", which = "both", left = True, right = False) #only want ticks on the left not the right
plt.xticks(np.arange(x[2], x[-1]+1, 3.0)) ##How often I want a tick on the x axis

i = 0
for spine in plt.gca().spines.values():
    if i == 2:
        spine.set_visible(True)
    else:
        spine.set_visible(False)
    i += 1

plt.axis(xmin=26, xmax=35, ymin=40000, ymax=80000)
plt.show()