import matplotlib.pyplot as plt

slices = [7, 2, 2, 5, 13]
labels = ["a", "b", "c", "d", "e"]

# slices = data
# labels = names for values
# autopct = show percentage
# explode = drag a piece out
plt.pie(slices, labels=labels, colors=['red', 'blue', 'green', 'white', 'yellow'], shadow=True, startangle=0,
        counterclock=False,
        autopct='%1.1f%%', explode=[0, 0, 0.1, 0, 0])

plt.show()
