import numpy as np
from Simulator import simulator

#import simulator
class selector:

    def __init__(self, prob_selected: float, prob_unselected: float, simulator: simulator):
        self.points_selected_already=[[simulator.get_side_length()//2, simulator.get_side_length()//2]]
        self.points_selected_temporarily = self.points_selected_already.copy()
        self.num_accumulated = []
        self.prob_selected = prob_selected
        self.prob_unselected = prob_unselected


    def get_points_selected_already(self):
        return self.points_selected_already

    def get_points_selected_temporarily(self):
        return self.points_selected_temporarily

    def get_num_accumulated(self):
        return self.num_accumulated

    def new_point(self):
        return list(np.random.randint(0, n, 2))

    def not_selected_already(self, point: list):
        return not(point in self.points_selected_already) #Probably, it will not work.



    def add_point(self, point: list):
        self.points_selected_temporarily.append(point)
        self.points_selected_already.append(point)

    def find_neighbours(self, point: list):
        return {0:[point[0]-1, point[1]-1], 1:[point[0], point[1]-1], 2:[point[0]+1, point[1]-1], 3:[point[0]-1, point[1]],
                4:[point[0]+1, point[1]], 5:[point[0]-1, point[1]+1], 6:[point[0], point[1]+1],
                7:[point[0]+1, point[1]+1]}

    def check_within_boundary(self, point: list, simulator: simulator):
        return ((point[0] >= 0) and (point[0] <=simulator.get_side_length() -1)) or ((point[1] >= 0) and (point[1] <= simulator.get_side_length()-1))

    def can_select(self):
        return (np.random.uniform(0,1,1) <= self.prob_selected)


    def update_num_accumulated(self):
        self.num_accumulated.append(len(self.get_points_selected_already()))

    def can_remove(self):
        return np.random.uniform(0, 1, 1) <= self.prob_unselected

    def remove_point_from_temp(self):
        self.points_selected_temporarily.pop(np.random.randint(0, len(self.get_points_selected_temporarily()), 1)[0])

    def get_rate(self, simulator: simulator):
        return 100 * len( self.get_points_selected_already() ) / simulator.get_number_total()

    def get_rate_list(self, simulator: simulator):
        return (100 * np.asarray(self.get_num_accumulated())  / simulator.get_number_total()).tolist()




