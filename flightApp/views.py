from django.shortcuts import render

#import models & serializers
from .models import *
from .serializers import *

#import necessary DRF Built in methods,functions,decorators
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



# Create your views here.
@api_view(['POST'])
def find_flights(request):
	flights = Flight.objects.filter(
		departureCity = request.data['departureCity'],
		arrivalCity = request.data['arrivalCity'],
		dateofDeparture = request.data['dateofDeparture']
		)
	serializer = FlightSerialier(flights,many=True)
	return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
	flight = Flight.objects.get(id=request.data['flightId'])
	
	passenger = Passenger()
	passenger.firstName = request.data['firstName']
	passenger.lastName = request.data['lastName']
	passenger.email = request.data['email']
	passenger.phoneNumber = request.data['phoneNumber']
	passenger.save()

	reservation = Reservation()
	reservation.flight = flight
	reservation.passenger = passenger
	reservation.save()
	
	return Response(status=status.HTTP_201_CREATED)

class FlightViewSet(viewsets.ModelViewSet):
	queryset = Flight.objects.all()
	serializer_class = FlightSerialier

class PassengerViewSet(viewsets.ModelViewSet):
	queryset = Passenger.objects.all()
	serializer_class = PassengerSerialier

class ReservationViewSet(viewsets.ModelViewSet):
	queryset = Reservation.objects.all()
	serializer_class = ReservationSerialier
