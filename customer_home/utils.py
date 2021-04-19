from booking.models import Reservation


def rList(email):
    query = 'SELECT * FROM booking_reservation WHERE "email" = %s'
    bookings = Reservation.objects.raw(query, [email])
    return bookings

