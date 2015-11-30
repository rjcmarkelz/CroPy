class Organ(object):
    '''
    This class makes an organ with X, Y, Z coordinates in a 3D space,
    it will calculate C, N, and P demand based on the size and 
    developmental stage of the organ.
    '''

    def __init__(self, name):
        self.name = name
        # self.size = 1
        # self.xcoord = 0
        # self.ycoord = 0
        # self.zcoord = 0

    def space(self):
        print("Space")

    def c_demand(self):
        print("C demand")

    def n_demand(self):
        print("N demand")

    def p_demand(self):
        print("P demand")
    # size
    # X
    # Y
    # Z

class Leaf(Organ):
    '''
    This class is a leaf. It has special methods to calculate photosynthesis
    and respiration. 
    '''
    class_counter = 0
    def __init__(self, name='', shape=10, area=1):
        # super().__init__(self, name)
        self.area = area
        self.rate = 10
        self.shape = shape
        self.id = Leaf.class_counter
        Leaf.class_counter += 1

    def photosynthesis(self):
        return (self.area * self.rate)

    def respiration(self):
        return (self.area * self.rate) / 2


