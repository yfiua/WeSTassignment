import numpy as np
import matplotlib.pyplot as plt

# plots y=x^2
if __name__ == '__main__':
    x = np.linspace(-2, 2)
    y = np.power(x, 2)

    plt.plot(x, y)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title(r'$y=x^2$')

    plt.savefig('plot.png', format='png')
