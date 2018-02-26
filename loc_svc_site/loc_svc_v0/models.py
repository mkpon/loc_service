from django.db import models
from google_apis import GoogleMapsWrapper


GAPI_KEY = 'ABCDEFG'

class Location(models.Model):
	latitude = models.FloatField()
	longitude = models.FloatField()
	street_address = models.CharField(max_length=500)
	places_list = models.CharField(max_length=500)

	def save(self, *args, **kwargs):
		# Before we save to the database, get the places_list
		gapi = GoogleMapsWrapper(GAPI_KEY)
		if self.latitude and self.longitude:
			lat_long = (self.latitude, self.longitude)
			self.street_address = gapi.reverse_geocode(lat_long)
		elif self.street_address:
			lat_long = gapi.geocode(self.street_address)
			self.latitude = lat_long[0]
			self.longitude = lat_long[1]
		else:
			# no lat/long or address provided
			raise Exception
		self.places_list = gapi(latitude, longitude)

		super().save *args, **kwargs)




