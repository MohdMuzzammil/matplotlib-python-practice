import matplotlib.pyplot as plt

x1 = [2,4,6,8,10]
y1 = [1,4,2,7,4]

x2 = [1,3,5,7,9]
y2 = [2,6,1,8,5]

plt.bar(x1,y1,label="bar1",color="black")
plt.bar(x2,y2,label="bar2",color="red")

plt.legend()

plt.show()

