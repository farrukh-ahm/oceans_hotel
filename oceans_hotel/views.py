from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View, generic
from django.template.response import TemplateResponse
from .models import *

# Create your views here.

class Home(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'index.html')


class BookSearch(View):

    def get(self, request, *args, **kwargs):

        # r =self.request.GET.keys()
        r = self.request.GET.dict()
        check_in_date = r["check_in"]
        check_out_date = r["check_out"]
        room_array = list(filter(lambda x: r[x]=="on", r))
        avail_rooms_list = []
        

        if room_array:
            # bookings = Bookings.objects.all().filter(check_out<check_in_date).filter(check_in>check_out_date)
            # print(bookings)
            for room_cat in room_array:
                avail_rooms = Rooms.objects.all().filter(category=room_cat)
                # print(len(avail_rooms))
                for room in avail_rooms:
                    try:
                        booking = Bookings.objects.all().filter(room_booked=room)
                        print(booking)
                        # for book in booking:
                        #     if book.check_out >= 
                    except:
                        print("pass")
                    # avail_rooms_list.append(room)

        print("*"*15)
        # print(room_array)
        print(r)
        # print(check_in, check_out, r)

        context = {
            "check_in": check_in_date,
            "check_out": check_out_date,
            "avail_rooms": avail_rooms_list
        }


        return render(request, 'book_rooms.html', context)