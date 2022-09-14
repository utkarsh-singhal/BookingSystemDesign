from dao.booking import Booking
from dao.room import Room
from service.roomservice import RoomService


class BookingService:
    def __init__(self):
        self.bookings = []
        self.room_service = RoomService()

    def add_booking(self, booking_request):
        is_valid_booking = self.validate_booking_request(booking_request)
        if not is_valid_booking:
            return [False, "Room is already booked"]

        self.bookings.append(booking_request)
        return [True, "Room is booked"]

    """
        All the bookings and if any overlap returns false
    """
    def validate_booking_request(self, booking_request):
        for booking in self.bookings:
            if booking.room == booking_request.room and self.is_overlap(booking.timeSlot, booking_request.timeSlot):
                return False
        return True

    def is_overlap(self, firstSlot, secondSlot):
        print(firstSlot, secondSlot)
        return firstSlot.startTime > secondSlot.endTime or firstSlot.endTime > secondSlot.startTime

    def search_room(self, searchRoomRequest):
        return self.room_service.search_room(self.bookings, searchRoomRequest)

