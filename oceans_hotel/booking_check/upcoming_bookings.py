from datetime import datetime


def check_bookings(check_out):

    current_date = datetime.now().date()
    # check_out_date = datetime.strptime(check_out, "%Y-%m-%d")

    if check_out > current_date:
        return True