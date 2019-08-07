import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

x = np.linspace(0,14,100)
y1 = np.sin(x)
y2 = 2 * np.sin(x + 0.5)
y3 = 3 * np.sin(x + 1.0)
y4 = 4 * np.sin(x + 1.5)

plt.figure(figsize=(10,6))
plt.plot(x, y1, x,y2, x,y3, x,y4)
plt.show()

sns.set_style('whitegrid') # 격자무늬 세겨주는 스타일
plt.figure(figsize=(10,6))
plt.plot(x,y1, x,y2, x,y3, x,y4)
plt.show()
