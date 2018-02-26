from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ('latitude', 'longitude', 'street_address', 'places_list')
