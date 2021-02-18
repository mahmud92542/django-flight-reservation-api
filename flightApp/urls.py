from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('flights',FlightViewSet)
router.register('passenger',PassengerViewSet)
router.register('reservation',ReservationViewSet)

urlpatterns = [
    path('flightServices/',include(router.urls)),
    path('flightServices/findFlights/',find_flights,name='findFlights'),
    path('flightServices/saveReservation/',save_reservation,name='saveReservation'),
]