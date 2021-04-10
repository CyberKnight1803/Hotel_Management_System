from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Reservation

def renderPDF(template_path, context, outputfile):
    template = get_template(template_path)
    html  = template.render(context)
    pdf = open(outputfile, "w+b")
    pisa.CreatePDF(html, dest=pdf)
    pdf.close()

def isAvailable(booking):
    Check_In_clashQuery = 'SELECT * FROM booking_reservation WHERE CAST(roomtype as integer) = %s AND "checkout" > %s'
    Check_Out_clashQuery = 'SELECT * FROM booking_reservation WHERE CAST(roomtype as integer) = %s AND "checkin" < %s'

    IN = Reservation.objects.raw(Check_In_clashQuery, [booking.roomtype, booking.checkin])
    OUT = Reservation.objects.raw(Check_Out_clashQuery, [booking.roomtype, booking.checkout])

    if len(IN) <= 5 - booking.rooms and len(OUT) <= 5 - booking.rooms:
        return True
    else:
        return False

