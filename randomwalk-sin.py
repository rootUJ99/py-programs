import matplotlib.pyplot as plt
import numpy as np



n = 1000

x = np.zeros(n)
y = np.zeros(n)

for i in range(n):
    random_int = np.random.randint(1,3)
    if random_int == 1:
        x[i] = x[i-1]+2
        y[i] = y[i-1]+2
    elif random_int == 2:
        x[i] = x[i-1]+2
        y[i] = y[i-1]-2
    elif random_int == 3:
        x[i] = x[i-1]
        y[i] = y[i-1]-2
    elif random_int ==4:
        x[i] = x[i-1]+1
        y[i] = y[i-1]-2


    print(x[i], y[i])
                
    

plt.plot(x, y, c='xkcd:baby poop green')
plt.show()
