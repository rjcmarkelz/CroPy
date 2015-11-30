class Organ(object):
    '''
    doc tests are up next
    '''

    def __init__(self, name='', shape=[]):
        self.name = name
        self.shape = shape
    # size
    # X
    # Y
    # Z
    # C
    # N

class Leaf(Organ):
    '''
    '''
    class_counter = 0
    def __init__(self, name='', shape='', area=1):
        Organ.__init__(self, name, shape)
        self.area = area
        self.rate = 10
        self.id = Leaf.class_counter
        Leaf.class_counter += 1

    def photosynthesis(self):
        return (self.area * self.rate)

    def respiration(self):
        return (self.area * self.rate) / 2
