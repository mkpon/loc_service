import googlemaps

# https://googlemaps.github.io/google-maps-services-python/docs/

class LANDMARKS_ENUM(Enum):
	PARKS = 'parks'
	RESTAURANTS = 'restaurants'

def extract_places_from_json(places_json):
	# Extract
	# Reformat
	a_list_of_places = [('a','b','c')]
	return a_list_of_places


class GoogleMapsWrapper():
	# we wrap the googlemapsClient so that later on we can build reliability around it.
	#  These methods won't work as written, but this is pseudo code.

	def __init__(google_api_key, search_distance):
		""" GoogleMapsWrapper object constructor"""

		self.api_key = google_api_key
		""" google api key for accessing Google map services"""

		self._gmaps = googlemapsClient(key=google_api_key)
		""" google maps client """

		self.search_distance = search_distance

	def geocode(address):
		""" Given an address return Lat,Long tuple """
		return self._gmaps.geocode(address)

	def nearby_list(lat_long_tuple):
		""" returns list of nearby landmarks and their locations"""
		landmarks = ['park', 'restaurant']
		places_list = extract_places_from_json(
						self._gmaps.places(latitude=lat_long_tuple[0], 
										   longitude=lat_long_tuple[1], 
										   landmarks))
		return places_list

	def reverse_geocode(lat_long_tuple):
		return self._gmaps.reverse_geocode(lat_long_tuple)






