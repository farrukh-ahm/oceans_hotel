from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('book-room', views.BookSearch.as_view(), name="book_search"),
    path('signup', views.UserSignUp.as_view(), name='signup'),
    path('login', views.UserLogin.as_view(), name='login'),
    path('logout', views.UserLogout.as_view(), name='logout'),
    path('confirm-booking', views.BookSearch.as_view(), name='confirmbooking'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('cancelbooking/<int:id>', views.CancelBooking.as_view(), name='cancel_booking'),
]