from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('book-room', views.BookSearch.as_view(), name="book_search"),
    path('signup', views.UserSignUp.as_view(), name='signup'),
]