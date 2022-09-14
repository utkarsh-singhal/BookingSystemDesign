from dao.room import Room


class RoomService:

    def __init__(self):
        self.rooms = []

    def add_room(self, id, meta_data):
        room = Room(id, meta_data)
        self.rooms.append(room)
        return room

    """
        self.ids = []
        self.meta_data = None
        self.is_free = False
        self.timeSlot = None

        self.is_projector_present = False
        self.is_white_board_present = False
        
    """
    def search_room(self, bookings, search_room_request):
        potentials_rooms = {}
        if search_room_request.meta_data:
            meta_data = search_room_request.meta_data
            for room in self.rooms:
                is_valid = True
                if meta_data.capacity and meta_data.capacity > room.meta_data.capacity:
                    is_valid = False

                if meta_data.is_projector_present and not room.meta_data.is_projector_present:
                    is_valid = False

                if meta_data.is_white_board_present and not room.meta_data.is_white_board_present:
                    is_valid = False

                if is_valid:
                    potentials_rooms[room.id] = {
                        'is_valid': True,
                        'room': room
                    }

        for booking in bookings:
            if self.is_overlap(booking.timeSlot, search_room_request.timeSlot):
                if booking.room in potentials_rooms:
                    potentials_rooms[booking.room]['is_valid'] = False

        rooms = []
        for item in potentials_rooms.items():
            if item[1]['is_valid']:
                rooms.append(item[1]['room'])
        return rooms



    def is_overlap(self, firstSlot, secondSlot):
        return firstSlot.startTime > secondSlot.endTime or firstSlot.endTime > secondSlot.startTime
