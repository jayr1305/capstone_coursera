from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView,DestroyAPIView,RetrieveUpdateAPIView
from .models import Menu,TableBook
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import MenuSerializer,BookingSerializer,UserSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticated

def index(request):
    return render(request,'index.html')
class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleItemView(RetrieveUpdateAPIView, DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class GetBookingView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TableBook.objects.all()
    serializer_class = BookingSerializer

class BookingAPICrud(RetrieveUpdateAPIView):
    queryset = TableBook.objects.all()
    serializer_class = BookingSerializer
        

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 