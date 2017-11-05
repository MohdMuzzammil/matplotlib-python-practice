import matplotlib.pyplot as plt

#points for line 1
x1 = [1,2,3]
y1 = [4,3,6]

#points for line 2
x2 = [1,2,3]
y2 = [1,7,4]


#title, xlabel and ylabel
plt.title("Practice 2")
plt.xlabel("xlabel")
plt.ylabel("ylabel")

#plotting two lines
plt.plot(x1,y1,label="first line")
plt.plot(x2,y2,label="second line")

#calling legend
#plt.legend()

plt.show()