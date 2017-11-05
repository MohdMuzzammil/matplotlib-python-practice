import matplotlib.pyplot as plt
import random

x1 = [random.randrange(1,100) for i in range(0,50)]
y1 = [random.randrange(1,100) for i in range(0,50)]

x2 = [random.randrange(1,100) for i in range(0,50)]
y2 = [random.randrange(1,100) for i in range(0,50)]

#marker is for styles
#s is for size of marker
plt.scatter(x1,y1,label="points 1", marker="*",s=10)
plt.scatter(x2,y2,label="points 2")
plt.legend()

plt.show()