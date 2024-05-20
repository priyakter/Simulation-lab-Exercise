import random
import matplotlib.pyplot as plt
#signal generation block
def x(n):
 return random.randint(-20,20)
n= range(0,10) #number of sample
x=[x(i) for i in n] #signal
plt.stem(x)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Discrete Time Signal")
plt.grid(True)
plt.show(x)
