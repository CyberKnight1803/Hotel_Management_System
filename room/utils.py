from booking.models import Reservation
from .models import Room

def CheckIN(form_input):

    query = 'SELECT * FROM room_room WHERE '


def availableRooms(Date):
    R = {'Single' : 1, 'Double' : 2, 'Suite' : 3, 'Luxury' : 4}

    query = 'SELECT * FROM booking_reservation WHERE CAST(roomtype as integer) = %s AND "checkout" > %s AND "checkin" <= %s'
    single = Reservation.objects.raw(query, [R['Single'], Date, Date])
    double = Reservation.objects.raw(query, [R['Double'], Date, Date])
    suite = Reservation.objects.raw(query, [R['Suite'], Date, Date])
    luxury = Reservation.objects.raw(query, [R['Luxury'], Date, Date])
    Availability = {
        'single' : 5 - len(single),
        'double' : 5 - len(double),
        'suite' : 5 - len(suite),
        'luxury' : 5 - len(luxury),
    }
    
    return Availability

def insertRoom(reservationID):
    pass
