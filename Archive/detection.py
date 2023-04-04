class Detection:
    _data = {}
    def __init__(self, id):
        self.id = id
        
    # this section addeds new data to the dection object
    def add_data(self, data, key):
        if not self._data.setdefault(key):
            self._data[key] = data
        else:
            self._data[key] += data
        print(self._data)