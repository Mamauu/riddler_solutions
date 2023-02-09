import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import random

#99 verses
#1% chance to forget and restart
#total verses in the song

#average song length for 99 verses is 170.45276 verses

sample_size = 1000  # number of repetitions
sample_size2 = 200 # number of verses
#start_verse = 99
N = list()
verse_list_perN = list()

#for k in [100]:
for k in range(1,sample_size2+1):
    start_verse = k
    verse_list = list()
    for i in range(sample_size):
        current_verse = start_verse
        total_verse = 0
        
        while current_verse > 0:
            current_verse -= 1
            total_verse += 1
            
            if random.random() >= 0.99:
                current_verse = start_verse
            
        verse_list.append(total_verse)
        #print(current_verse, total_verse)
        
    average_verses = np.average(verse_list)
    verse_list_perN.append(average_verses)
    N.append(k)

print(verse_list_perN)

plt.plot(N, verse_list_perN, label = "data")
plt.xlabel("Number of verses")
plt.ylabel("Number of verses sang")

#polyfit
coeffs = np.polyfit(N, verse_list_perN, 2)
fit = np.poly1d(coeffs)
plt.plot(N, fit(N), label = "quadratic fit")

#expotential fit
def exp_func(x, a):
    return np.exp(a * x)

# Perform the fit
params, covariance = curve_fit(exp_func, N, verse_list_perN, maxfev=1000)
a = params

# Plot the data and the fit
fit = exp_func(N, a)
plt.plot(N, fit, label = "expotentiell fit")

plt.legend()
plt.show()








