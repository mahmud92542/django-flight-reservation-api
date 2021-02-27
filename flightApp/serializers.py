from rest_framework import serializers
from .models import *

#alpha numeric import
import re

class FlightSerialier(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = '__all__'

#1st custom validation
	def validate_flightNumber(self,flightNumber):
		if(re.match("[a-zA-Z0-9]*$",flightNumber)==None):
			raise serializers.ValidationError("Invalid! Make sure it is a alpha numeric.")
		return flightNumber

	

class PassengerSerialier(serializers.ModelSerializer):
	class Meta:
		model = Passenger
		fields = '__all__'



class ReservationSerialier(serializers.ModelSerializer):
	class Meta:
		model = Reservation
		fields = '__all__'