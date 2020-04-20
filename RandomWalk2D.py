import matplotlib.pyplot as plt
import numpy as np

"""RANDOM WALK IN FINITE SPACE"""

#Init
n_particle = 10 #Number of Particle
n_iteration = 100 #Number of Iteration

#Square
xmin = 0
xmax = 120
ymin = 0
ymax = 120
xrange = xmax - xmin
yrange = ymax - ymin

#Initial Position
posisi = []
pos = []
for i in range(n_particle):
    x_pos = 60
    y_pos = 60
    pos.append([x_pos,y_pos])
posisi.append(pos)

#Iteration
for i in range(n_iteration):
    updatePosition = []
    for j in range(n_particle):
        x = posisi[i][j][0]
        y = posisi[i][j][1]

        #Generate Random
        rand = np.random.rand()
        #Right
        if(rand<=0.25):
            x = x + 1
        #Down
        elif(rand<=0.50):
            y = y - 1
        #Left
        elif(rand<=0.75):
            x = x - 1
        #Up
        else:
            y = y + 1

        #Perform PBC Correction
        if (x > xmax): 
            x = x - xrange
        if (x < 0): 
            x = x + xrange
        if (y > ymax):
            y = y - yrange
        if (y < 0): 
            y = y + yrange
        updatePosition.append([x,y])
    posisi.append(updatePosition)

fig, ax = plt.subplots(figsize=(7,7))
for i in range(n_iteration):
  for j in range(n_particle):
    ax.scatter(posisi[i][j][0], posisi[i][j][1], s=50, alpha=0.75)

plt.title('Random Walk 2D - 4 Direction')
plt.xlabel('X')
plt.ylabel('Y')
plt.minorticks_on()
plt.grid(b=True, which='minor', linestyle='-')
plt.grid(b=True, which='major', linestyle='-')
plt.show()
