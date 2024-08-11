from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View, generic
from django.template.response import TemplateResponse
from .models import *
from .forms import *
from .booking_check.availability import check_availability
import random
import datetime
# Create your views here.

class Home(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'index.html')


class BookSearch(View):

    avail_rooms_list = []

    def get(self, request, *args, **kwargs):

        r = self.request.GET.dict()
        
        check_in_date = r["check_in"]
        check_out_date = r["check_out"]
        self.avail_rooms_list.clear()
        
        try:

            room_category = list(filter(lambda x: r[x]=="on", r))[0]
            rooms = Rooms.objects.filter(category=room_category)
            for room in rooms:
                available = check_availability(room, check_in_date, check_out_date)
                if available:
                    self.avail_rooms_list.append(room.room_no)


            print("*"*15)
            print(self.avail_rooms_list)

        except IndexError:

            room_category = ""
            pass

        booking_form = BookRoomForm()
        booking_form.initial = {
            'check_in': check_in_date,
            'check_out': check_out_date,
            }

        context = {
            "check_in": datetime.datetime.strptime(check_in_date, "%Y-%m-%d"),
            "check_out": datetime.datetime.strptime(check_out_date, "%Y-%m-%d"),
            "avail_rooms": self.avail_rooms_list,
            'form': booking_form,
            'category': room_category
        }


        return render(request, 'book_rooms.html', context)

    
    def post(self, request, *args, **kwargs):

        select_room = random.choice(self.avail_rooms_list)
        queryset = Rooms.objects.get(room_no=select_room)
        room_form = BookRoomForm(request.POST)
        print(room_form)
        # print(self.avail_rooms_list)
        if room_form.is_valid():
            room_book = room_form.save(commit=False)
            room_book.guest = request.user
            room_book.room_booked = queryset
            print(room_book)
            room_book.save()

        else:
            room_form = BookRoomForm()

        # print(self.avail_rooms_list)
        # print(room_form)
        return redirect('home')


class UserSignUp(View):

    def get(self, request, *args, **kwargs):
        signup_form = SignUpForm()
        context = {
            'form': signup_form,
        }

        return render(request, 'authentication/signup.html', context)

    def post(self, request, *args, **kwargs):
        signup_form = SignUpForm(request.POST)

        if signup_form.is_valid():
            signup_form.save()
            return render(request, "authentication/login.html")
        else:
            signup_form = SignUpForm()
            return redirect(reverse('signup'))


class UserLogin(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'authentication/login.html')

    def post(self, request, *args, **kwargs):
        
        login_form = self.request.POST.dict()
        username = login_form["username"]
        password = login_form["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # users = User.objects.all()
            # user_id = get_object_or_404(users, username=username)
            # print(user_id.id)
            login(request, user)
            return redirect('home')
        else:
            return redirect(reverse('login'))

class UserLogout(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')