import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from Selector import selector
from Canvas import canvas
from Simulator import simulator

if __name__ == "__main__":
    sim = simulator(300)
    sel = selector(prob_selected=0.325, prob_unselected=0.9, simulator=sim)
    while len(sel.get_points_selected_temporarily()):
        sel.update_num_accumulated()
        sim.add_counter()
        '''
        if sel.can_select():
            new_pt = sel.new_point()
            if sel.not_selected_already(new_pt):
                sel.add_point(new_pt)'''
        # Select new percolation point from the neighbours.
        for point in sel.get_points_selected_temporarily():
            for key, neighbour in sel.find_neighbours(point).items():
                if sel.not_selected_already(neighbour) and sel.check_within_boundary(neighbour, sim) and sel.can_select():
                    sel.add_point(neighbour)

            if sel.can_remove():
                sel.remove_point_from_temp()

        print(len(sel.get_points_selected_temporarily()))


    painter = canvas(sel, sim)
    painter.color_map()