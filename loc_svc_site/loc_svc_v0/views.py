from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Location
from serializers import LocationSerializer

@api_view('POST')
def location(request):
	""" Get all pertinant location data

	post (latitude, longitude) or address
 	returns: location json including nearby places list.
	"""
	req_latitude = request.data.latitude
	req_longitude = request.data.longitude
	req_address = request.data.address
	if req_latitude and req_longitude:
		requested_location = Location.objects.filter(latitude=req_latitude).filter(longitude=req_longitude).first()
	elif req_address:
		requested_location = Location.objects.filter(street_address=req_address).first()
	else:
		raise Exception

	if !requested_location:
		requested_location = Location()
		requested_location.latitude = req_latitude
		requested_location.longitude = req_longitude
		requested_location.street_address = req_address
		requested_location.save()

	serializer = LocationSerializer(requested_location)
	return Response(serializer.data)
