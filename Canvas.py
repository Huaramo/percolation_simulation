import numpy as np
from matplotlib import pyplot as plt
from Selector import selector
from Simulator import simulator

#import selector
#import simulator
class canvas:

    def __init__(self, selector:selector, simulator:simulator):
        self.selector = selector
        self.simulator = simulator

    def get_selector(self):
        return self.selector

    def get_simulator(self):
        return self.simulator

    def line_plot(self):
        plt.figure(figsize=(10, 10))
        ax = plt.subplot()
        ax.plot(self.simulator.get_counts(), self.selector.get_rate_list(self.simulator), 'b-')
        ax.set_xlabel("Time lapse")
        ax.set_ylabel("The fraction of percolated area %")
        ax.set_title("The fraction of percolated area: {}%".format(self.selector.get_rate(self.simulator)))
        plt.show()

    def color_map(self):
        points_selected_already = np.asarray(self.selector.get_points_selected_already())
        plt.figure(figsize=(10, 10))
        ax = plt.subplot()
        xs = np.linspace(0, self.simulator.get_side_length() - 1, self.simulator.get_side_length())
        zone = [[x, y] for x in xs for y in xs]
        zone = np.asarray(zone)
        ax.plot(zone[:, 0], zone[:, 1], 'g.')
        ax.plot(points_selected_already[:, 0], points_selected_already[:, 1], 'r.')

        ax.set_xlabel("grid x position")
        ax.set_ylabel("grid y position")
        ax.set_title("The fraction of percolated area: {:.3f}%".format(self.selector.get_rate(self.simulator)))
        plt.show()


