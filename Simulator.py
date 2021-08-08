
class simulator:
    def __init__(self, side_length: int):
        self.counter = 0
        self.counts = []
        self.side_length = side_length

    def get_counter(self):
        return self.counter

    def get_counts(self):
        return self.counts

    def add_counter(self):
        self.counter += 1
        self.counts.append(self.counter)

    def get_number_total(self):
        return self.side_length**2

    def get_side_length(self):
        return self.side_length










    