from django.db.models.fields import json
from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from geopy.geocoders import Nominatim

from .models import Point


def show_map(request):
    points = Point.objects.all().values('latitude', 'longitude', 'adresse')
    return render(request, '../templates/map.html', {'points': list(points)})


@csrf_exempt
def save_point(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            lat = data['lat']
            lng = data['lng']

            geolocator = Nominatim(user_agent="myapp")
            location = geolocator.reverse(f"{lat}, {lng}", exactly_one=True)
            adresse = location.address if location else "Adresse inconnue"

            point = Point(latitude=lat, longitude=lng, adresse=adresse)
            point.save()

            return JsonResponse({'status': 'success', 'adresse': adresse})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée'})