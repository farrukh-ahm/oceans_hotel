from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View, generic
from django.template.response import TemplateResponse

# Create your views here.

class Home(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'base.html')
