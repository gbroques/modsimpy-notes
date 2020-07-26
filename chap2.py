"""
Imagine a bike share system for students traveling between Olin College and
Wellesley College, which are about 3 miles apart in eastern Massachusetts.

Suppose the system contains 12 bikes and two bike racks, one at Olin and one
at Wellesley, each with the capacity to hold 12 bikes.

As students arrive, check out a bike, and ride to the other campus, the number
of bikes in each location changes. In the simulation, we’ll need to keep track
of where the bikes are.
"""
import numpy as np

from pandas import Series
import matplotlib.pyplot as plt


def main() -> None:
    """Run bike-share simulation."""
    bikeshare = Series([10, 2], ['olin', 'wellesley'])

    results = [bikeshare.olin]

    for i in range(10):
        step(bikeshare, 0.3, 0.2)
        results.append(bikeshare.olin)
    series = Series(results)
    plot(series, label='Olin')
    decorate(title='Olin-Wellesley Bikeshare',
            xlabel='Time step (min)', 
            ylabel='Number of bikes')
    plt.show()

def step(bikeshare: Series, p1: float, p2: float) -> None:
    # np.random.random() generates a random number between 0 and 1
    if np.random.random() < p1:
        bike_to_wellesley(bikeshare)
    
    if np.random.random() < p2:
        bike_to_olin(bikeshare)

def bike_to_wellesley(bikeshare: Series):
    bikeshare.olin -= 1
    bikeshare.wellesley += 1

def bike_to_olin(bikeshare: Series):
    bikeshare.olin += 1
    bikeshare.wellesley -= 1

def plot(self, *args, **kwargs):
    """Plot a Series.
    :param args: arguments passed to plt.plot
    :param kwargs: keyword argumentspassed to plt.plot
    :return:
    """
    x = self.index
    y = self.values

    underride(kwargs, linewidth=2)
    if self.name:
        underride(kwargs, label=self.name)
    plt.plot(x, y, *args, **kwargs)

def underride(d, **options):
    """Add key-value pairs to d only if key is not in d.
    If d is None, create a new dictionary.
    d: dictionary
    options: keyword args to add to d
    """
    if d is None:
        d = {}

    for key, val in options.items():
        d.setdefault(key, val)

    return d

def decorate(**options):
    """Decorate the current axes.
    Call decorate with keyword arguments like
    decorate(title='Title',
             xlabel='x',
             ylabel='y')
    The keyword arguments can be any of the axis properties
    https://matplotlib.org/api/axes_api.html
    In addition, you can use `legend=False` to suppress the legend.
    And you can use `loc` to indicate the location of the legend
    (the default value is 'best')
    """
    loc = options.pop("loc", "best")
    if options.pop("legend", True):
        legend(loc=loc)

    plt.gca().set(**options)
    plt.tight_layout()

def legend(**options):
    """Draws a legend only if there is at least one labeled item.
    options are passed to plt.legend()
    https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
    """
    underride(options, loc="best", frameon=False)

    ax = plt.gca()
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(handles, labels, **options)

if __name__ == '__main__':
    main()
