from django.template import Context, loader
from django.shortcuts import render_to_response
import discogs_client as discogs

# Create your views here.
def home(request):
	discogs.user_agent = 'TimeLP/0.1'
	collection = discogs.User('neutralino1').collection(sort='year', order='desc')#, per_page=40)
	years = []
	for y in range(collection[0].year, collection[-1].year, -1):
		years.append({'year': y, 'releases': [r for r in collection if r.year == y]})
	return render_to_response('home.html', {'years':years})