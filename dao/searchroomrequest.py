class SearchRoomRequest:
    def __init__(self):
        self.ids = []
        self.meta_data = None
        self.timeSlot = None

    def add_meta_data(self, meta_data):
        self.meta_data = meta_data
        return self


    def add_time_slot(self, timeslot):
        self.timeSlot = timeslot
        return self
