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
from .booking_check.upcoming_bookings import check_bookings
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
        total_price = 0

        # Finding all available rooms in the selected category
        try:

            room_category = list(filter(lambda x: r[x]=="on", r))[0]
            rooms = Rooms.objects.filter(category=room_category)
            for room in rooms:
                available = check_availability(room, check_in_date, check_out_date)
                if available:
                    self.avail_rooms_list.append(room.room_no)

            # Total price based on selected category and number of days
            room_price = rooms[0].price
            days_spent = abs((datetime.datetime.strptime(check_out_date, "%Y-%m-%d") - datetime.datetime.strptime(check_in_date, "%Y-%m-%d")).days)
            total_price = room_price * days_spent
            print(total_price)

        except IndexError:

            room_category = ""
        
        # Assigning the form and initial values
        booking_form = BookRoomForm()
        booking_form.initial = {
            'check_in': check_in_date,
            'check_out': check_out_date,
            'total_cost': total_price,
            }

        context = {
            "check_in": datetime.datetime.strptime(check_in_date, "%Y-%m-%d"),
            "check_out": datetime.datetime.strptime(check_out_date, "%Y-%m-%d"),
            "avail_rooms": self.avail_rooms_list,
            'form': booking_form,
            'category': room_category,
            'total_cost': total_price
        }


        return render(request, 'book_rooms.html', context)

    
    def post(self, request, *args, **kwargs):

        select_room = random.choice(self.avail_rooms_list)
        queryset = Rooms.objects.get(room_no=select_room)
        room_form = BookRoomForm(request.POST)
        # print(room_form)
        # print(self.avail_rooms_list)
        if room_form.is_valid():
            room_book = room_form.save(commit=False)
            room_book.guest = request.user
            room_book.room_booked = queryset
            print(room_book)
            room_book.save()

        else:
            print(room_form.errors)
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

class ProfileView(View):

    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        user_info = get_object_or_404(queryset, username=request.user)

        room_queryset = Bookings.objects.filter(guest=request.user)
        rooms = []

        if room_queryset:
            for room in room_queryset:
                current = check_bookings(room.check_out)
                if current:
                    rooms.append(room)

        context = {
            "user": user_info,
            "room_list": rooms
        }

        return render(request, 'profile.html', context)