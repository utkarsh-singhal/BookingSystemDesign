from service.bookingservice import BookingService
from dao.metaData import MetaData
from dao.searchroomrequest import SearchRoomRequest
from dao.bookingrequest import  BookingRequest
from dao.timeslot import TimeSlot
bookingService = BookingService()

meta_data_first = MetaData(1).add_capacity(5).add_projector(True).add_white_board(True)
meta_data_second = MetaData(2).add_capacity(7).add_projector(False).add_white_board(False)

bookingService.room_service.add_room(
    1,
    meta_data_first
)

bookingService.room_service.add_room(
    2,
    meta_data_second
)

searchRequest = SearchRoomRequest()

meta_data = MetaData().add_capacity(3).add_projector(True).add_white_board(True)

searchRequest = searchRequest.add_meta_data(meta_data)
rooms = bookingService.search_room(searchRequest)
for room in rooms:
    print(room.id)


"""
        self.room = room
        self.timeSlot = timeSlot
        self.noOfPeople = noOfPeople
"""
timeSlot = TimeSlot("10:00", "11:00")
booking_request = BookingRequest(1, timeSlot, 2)

print(bookingService.add_booking(booking_request))


timeSlot = TimeSlot("10:00", "11:00")
booking_request = BookingRequest(2, timeSlot, 2)

print(bookingService.add_booking(booking_request))

searchRequest = SearchRoomRequest()

timeSlot = TimeSlot("12:00", "13:00")
meta_data = MetaData().add_capacity(3)
searchRequest = searchRequest.add_meta_data(meta_data).add_time_slot(timeSlot)
rooms = bookingService.search_room(searchRequest)
for room in rooms:
    print(room.id)