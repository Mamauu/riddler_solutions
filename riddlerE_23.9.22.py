import numpy as np
import random
import matplotlib.pyplot as plt

#Riddler Express 23.9.2022

shirts = 20
sample_size = 10000
ratio = list()

for i in np.arange(1,shirts+1):
    richtig = 0
    falsch = 0
    
    shirts = i
    
    for i in range(sample_size):
        wanted  = random.randint(1, shirts)
        got     = random.sample(range(1,shirts+1), shirts)      
        
        for k in got:
            if wanted == k:
                richtig += 1
                break
            if wanted != k:
                falsch += 1
    returned = 1-(richtig/(richtig+falsch))
    ratio.append(round(returned, 4))
    print("kind of shirts", shirts, "returned:", returned)

plt.plot(np.arange(1,shirts+1), ratio)
plt.axhline(0.8,c="black")

plt.xticks(np.arange(1,shirts+1))

plt.xlabel("kind of shirts")
plt.ylabel("Percentage returned")

# with 9 shirts around 80% are returned
