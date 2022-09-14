class MetaData:
    def __init__(self, id=None):
        self.capacity = 0
        self.is_projector_present = False
        self.is_white_board_present = False
        self.id = id

    def add_capacity(self, capacity):
        self.capacity = capacity
        return self

    def add_projector(self, is_present):
        self.is_projector_present = is_present
        return self

    def add_white_board(self, is_present):
        self.is_white_board_present = is_present
        return self
