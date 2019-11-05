"""User URLs."""

# Django
from django.urls import path

# Views
from user.views import LoginView, LogoutView

urlpatterns = [
    # Login URLs
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
