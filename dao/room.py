class Room:
    def __init__(self, id, meta_data):
        self.id = id
        self.meta_data = meta_data

    def __str__(self):
        return "Room No" + str(self.id)
