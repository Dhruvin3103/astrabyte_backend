from django.urls import path
from .views import PortfolioAPI,ContactusAPI,SlaveAPI,SearchAPI,Search2API,ImageAPI

urlpatterns = [
    path('portfolio/', PortfolioAPI.as_view()),
    path('contactus/',ContactusAPI.as_view()),
    path('slave/',SlaveAPI.as_view()),
    path('search/',SearchAPI.as_view()),
    path('images/',ImageAPI.as_view())
    # path('search2/',Search2API.as_view()),
]