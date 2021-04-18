from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Reservation
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

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
    
def checkoutEmail(user):
    details = {
        'name' : user.username,
    }
    template = render_to_string('booking/checkout_email.html', details)

    email = EmailMessage(
    'Thanks for your stay at RadissonInn. Would you share oyur experience', 
    template,
    settings.EMAIL_HOST_USER,
    [user.email]
    )
    email.fail_silently=False
    email.send()