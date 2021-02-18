from rest_framework import serializers
from .models import *


class FlightSerialier(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = '__all__'



class PassengerSerialier(serializers.ModelSerializer):
	class Meta:
		model = Passenger
		fields = '__all__'



class ReservationSerialier(serializers.ModelSerializer):
	class Meta:
		model = Reservation
		fields = '__all__'