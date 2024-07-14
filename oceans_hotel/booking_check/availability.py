from oceans_hotel.models import Bookings
import datetime

def check_availability(room, check_in, check_out):

    bookings = Bookings.objects.all().filter(room_booked=room)
    check_in_date = datetime.datetime.strptime(check_in, '%Y-%m-%d')
    check_out_date = datetime.datetime.strptime(check_out, '%Y-%m-%d')

    # print(room, bookings)

    for booking in bookings:

        booking_check_in = datetime.datetime.strptime(str(booking.check_in), '%Y-%m-%d')
        booking_check_out = datetime.datetime.strptime(str(booking.check_out), '%Y-%m-%d')

        if booking_check_out < check_in_date or booking_check_in > check_out_date:
            pass
        else:
            return False

    return True