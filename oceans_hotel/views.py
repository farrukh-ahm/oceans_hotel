from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View, generic
from django.template.response import TemplateResponse
from .models import *
from .forms import *
from .booking_check.availability import check_availability

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
        
        avail_rooms_list = []
        
        try:
            room_category = list(filter(lambda x: r[x]=="on", r))[0]
            
            rooms = Rooms.objects.filter(category=room_category)
            for room in rooms:
                available = check_availability(room, check_in_date, check_out_date)
                if available:
                    avail_rooms_list.append(room.room_no)


            print("*"*15)
            print(avail_rooms_list)

        except IndexError:
            pass

        context = {
            "check_in": check_in_date,
            "check_out": check_out_date,
            "avail_rooms": avail_rooms_list
        }


        return render(request, 'book_rooms.html', context)


class UserSignUp(View):

    def get(self, request, *args, **kwargs):
        signup_form = SignUpForm()
        context = {
            'form': signup_form,
        }

        return render(request, 'authentication/signup.html', context)