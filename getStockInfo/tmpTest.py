import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0., np.e, 0.01)
y1 = np.exp(-x)
y2 = np.log(x)

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax1.plot(x, y1)
ax1.set_ylabel('Y values for exp(-x)')

ax1.set_title("Double Y axis")

ax2 = ax1.twinx()  # this is the important function
ax2.plot(x, y2, 'r')
ax2.set_xlim([0, np.e])
ax2.set_ylabel('Y values for ln(x)')
ax2.set_xlabel('Same X for both exp(-x) and ln(x)')


ax3 = fig.add_subplot(212)
ax3.plot(x, y1)
ax3.set_ylabel('Y values for exp(-x)')

ax3.set_title("Double Y axis")

ax4 = ax3.twinx()  # this is the important function
ax4.plot(x, y2, 'r')
ax4.set_xlim([0, np.e])
ax4.set_ylabel('Y values for ln(x)')
ax4.set_xlabel('Same X for both exp(-x) and ln(x)')

plt.show()