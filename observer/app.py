class GloabalWealth(object):
    def __init__(self):
        self._global_wealth = 10.0
        self._observer = []
    def set_wealth(self, value):
        self._global_wealth = value
        for callback in self._observer:
            print 'anouncing change'
            callback(self._global_wealth)
    
    def bind_to(self, callback):
        print 'binded'
        self._observer.append(callback)
