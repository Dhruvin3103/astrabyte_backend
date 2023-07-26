from django.urls import path
from .views import PortfolioAPI,ContactusAPI,FounderAPI,SearchAPI,Search2API,ImageAPI

urlpatterns = [
    path('portfolio/', PortfolioAPI.as_view()),
    path('contactus/',ContactusAPI.as_view()),
    path('founder/',FounderAPI.as_view()),
    path('search/',SearchAPI.as_view()),
    path('images/',ImageAPI.as_view())
    # path('search2/',Search2API.as_view()),
]