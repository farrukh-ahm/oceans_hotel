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
        check_in = self.request.GET.get("check_in")
        check_out = self.request.GET.get("check_out")
        rooms = self.request.GET.get("room")
        r =self.request.GET.items()

        for room in r:
            print(room)

        print("*"*15)
        print(check_in, check_out, r)

        return render(request, 'index.html')