import matplotlib.pyplot as plt
import itertools
import warnings

fontsizes = itertools.cycle([8, 16, 24, 32])


def example_plot(ax):
    ax.plot([1, 2])
    ax.set_xlabel('x-label', fontsize=next(fontsizes))
    ax.set_ylabel('y-label', fontsize=next(fontsizes))
    ax.set_title('Title', fontsize=next(fontsizes))


fig, axs = plt.subplots(nrows=2, ncols=2)
for ax in axs.flat:
    example_plot(ax)
plt.tight_layout()
plt.show()
