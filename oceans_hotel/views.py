from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View, generic
from django.template.response import TemplateResponse

# Create your views here.

class Home(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'index.html')


class BookSearch(View):

    def get(self, request, *args, **kwargs):

        r =self.request.GET.keys()
        room_array = list(filter(lambda x: x=="single" or x=="double" or x=="triple" or x=="deluxe" or x=="suite", r))
        

        print("*"*15)
        print(room_array)
        # print(check_in, check_out, r)

        return render(request, 'index.html')