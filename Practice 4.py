import matplotlib.pyplot as plt
import random

population_ages = [random.randrange(1,100) for i in range(1,50)]
bins = list(range(0,101,10))

plt.hist(population_ages, bins, histtype="bar", rwidth=0.9)

plt.show()
