import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

# make data
np.random.seed(1)
x = np.linspace(0, 12, 16)
y1 = 3 + 4*x/12 + np.random.uniform(0.0, 0.5, len(x))
y2 = 1 + 2*x/12 + np.random.uniform(0.0, 0.5, len(x))
y3 = 1 + 16*x/12 + np.random.uniform(0.0, 0.5, len(x))

# plot
fig, ax = plt.subplots()

ax.fill_between(x, y1, y2, alpha=.1, linewidth=0)
ax.plot(x, (y1 + y2)/2, linewidth=2)
ax.plot(x, (y1 + y3)/2, linewidth=2)

ax.set(xlim=(0, 12), xticks=np.arange(1, 12),
       ylim=(0, 12), yticks=np.arange(1, 12))

plt.axis('on')
plt.show() #выложить в гитхаб