import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10,100)
print(x.shape)
fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')


#pycharm 은 show를 써야 그림이 보여짐

