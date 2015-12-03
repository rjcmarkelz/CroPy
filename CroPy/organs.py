
class Organ(object):
    '''
    This class makes an organ with X, Y, Z coordinates in a 3D space,
    it will calculate C, N, and P demand based on the size and 
    developmental stage of the organ.
    '''

    def __init__(self, name, X=0, Y=0, Z=0):
        self.name = name
        self.X = X
        self.Y = Y
        self.Z = Z

    def get_coord(self):
        return [self.X, self.Y, self.Y]

    def c_demand(self):
        print("C demand")

    def n_demand(self):
        print("N demand")

    def p_demand(self):
        print("P demand")

    def space(self):
        print("Space")

    



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
    def __init__(self, name='', shape='rect', area=1, photo_dt=10, resp_dt=2):
        Organ().__init__(self, name, X=0, Y=0, Z=0)
        self.area = area
        self.photo_dt = photo_dt
        self.resp_dt = resp_dt
        self.shape = shape
        self.id = Leaf.class_counter
        Leaf.class_counter += 1

    def photosynthesis(self):
        return (self.area * self.photo_dt)

    def respiration(self):
        return (self.area * self.resp_dt) / 2



