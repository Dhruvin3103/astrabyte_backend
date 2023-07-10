from django.shortcuts import render
from .models import Portfolio,Contactus,Slave
from .serializer import PortfolioSerializer,ContactusSerializer,SlaveSerializer
from  rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class PortfolioAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()
    def get(self, request):
        return self.list(request)

class SlaveAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = SlaveSerializer
    queryset = Slave.objects.all()
    def get(self, request):
        return self.list(request)

class SearchAPI(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['project_type']
# /?project_type = current projects


class Search2API(ListAPIView):
    queryset = Slave.objects.all()
    serializer_class = SlaveSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slave_type']
# /?slave_type = Core


class ContactusAPI(GenericAPIView, CreateModelMixin):
    serializer_class = ContactusSerializer
    queryset = Contactus.objects.all()
    def post(self, request):
        try:
            subject = 'Some one contacted you!!'
            message = f"NAME:{request.data['name']}\nEMAIL:{request.data['email']}\nPHONE:{request.data['phone']}\nMESSAGE:{request.data['message']}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['dhruvinhemant5@gmail.com']
            send_mail( subject, message, email_from, recipient_list )
        except Exception as e:
            return Response({'status': 403, 'message': 'Sorry Some error has occured', 'error':str(e)})
        return self.create(request)