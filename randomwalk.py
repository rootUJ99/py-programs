import matplotlib.pyplot as plt
import numpy as np



n = 10000

x = np.zeros(n)
y = np.zeros(n)
z = np.zeros(n)

for i in range(n):
    random_int = np.random.randint(1,7)
    if random_int == 1:
        x[i] = x[i-1]+2
        y[i] = y[i-1]
        z[i] = z[i-1]
    elif random_int == 2:
        x[i] = x[i-1]-2
        y[i] = y[i-1]
        z[i] = z[i-1]
    elif random_int == 3:
        x[i] = x[i-1]
        y[i] = y[i-1]+2
        z[i] = z[i-1]
    elif random_int ==4:
        x[i] = x[i-1]
        y[i] = y[i-1]-2
        z[i] = z[i-1]
    elif random_int == 5:
        x[i] = x[i-1]
        y[i] = y[i-1]
        z[i] = z[i-1]+2
    else:
        x[i] = x[i-1]
        y[i] = y[i-1]
        z[i] = z[i-1]-2


    print(x[i], y[i])
                
    
ax=plt.axes(projection="3d")

ax.plot3D(x, y, z, c='xkcd:baby poop green')
plt.show()
