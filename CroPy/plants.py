class Plant(object):

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Carbon(Plant):

    def __init__(self, name=''):
        Plant.__init__(self)
        self.name = name
        self._carbon = 10
        self._length = 10
        # self.photo = 3

    @property
    def carbon(self):
        return self._carbon

    @carbon.setter
    def carbon(self, value):
        self._carbon = value
        self.notify()

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value
        self.notify()

class CarbView:

    def update(self, plant):
        print('%s has %d carbon' % (plant.name, plant.carbon))
        print('%s has %d length' % (plant.name, plant.length))
        # print('%s has %d photo' % (plant.name, plant.photo))
