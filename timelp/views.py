from django.template import Context, loader
from django.shortcuts import render_to_response
import discogs_client as discogs

# Create your views here.
def home(request):
	discogs.user_agent = 'TimeLP/0.1'
	collection = discogs.Collection('neutralino1').all(sort='year', sort_order='desc')
	return render_to_response('home.html', {'collection':collection})