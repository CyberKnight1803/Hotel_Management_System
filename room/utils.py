from booking.models import Reservation
from .models import Room
from django.db import connection

def availableRooms(Date):
    R = {'Single' : 1, 'Double' : 2, 'Luxury' : 3, 'Suite' : 4}

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

def checkInRoom(reservationID, roomNo):
    ROOM = {
        1 : 'SINGLE',
        2 : 'DOUBLE',
        3 : 'LUXURY',
        4 : 'SUITE',
    }
    c = connection.cursor()
    booking = Reservation.objects.raw('SELECT * FROM booking_reservation WHERE "reservationID"=%s', [reservationID])
    room_type = ROOM[booking.roomtype]
    try:
        c.execute('UPDATE room_room SET "reservationID_id" = %s, "status" = %s WHERE "room_no" = %s', [reservationID, 'OCCUPIED', roomNo])
        c.execute('UPDATE booking_reservation SET "checkin_status"= %s WHERE "reservationID" = %s', [True, reservationID])
    finally:
        c.close()

def checkOutRoom(room_no):
    c = connection.cursor()
    room_details = Room.objects.raw('SELECT * FROM room_room WHERE "room_no" = %s', [room_no])
    reservationID = room_details.reservationID
    
    try:
        c.execute('UPDATE room_room SET "reservationID_id" = %s, "status" = %s WHERE "room_no" = %s', [None, 'VACANT',room_no])
        c.execute('UPDATE booking_reservation SET "checkout_status"= %s WHERE "reservationID" = %s', [True, reservationID])

    finally:
        c.close()
    
    return reservationID


def liveRoomStats():
    query = 'SELECT * FROM room_room WHERE "status" = %s'
    rooms = Room.objects.raw('SELECT * FROM room_room')
    room_status = rooms[:]['status']
    liveStats = [1 if status == 'OCCUPIED' else 0 for status in room_status]
    occ_rooms = Room.objects.raw(query, ['OCCUPIED'])
    vac_rooms = Room.objects.raw(query, ['VACANT'])

    return liveStats
