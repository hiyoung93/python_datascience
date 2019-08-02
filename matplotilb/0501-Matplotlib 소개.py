

import matplotlib as mpl
import matplotlib.pylab as plt
plt.title("Plot")
plt.plot([1, 4, 9, 16])
plt.show()

plt.title("x축의 tick 위치를 명시")
plt.plot([10,20,30,40],[1,4,9,16])
plt.show()

plt.title("'rs--' 스타일의 plot")
plt.plot([10,20,30,40], [1,4,9,16], 'rs--')
plt.show()
