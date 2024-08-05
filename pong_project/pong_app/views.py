# pong_app/views.py
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from .models import Player
import json

@csrf_exempt
def create_player(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        alias = data.get('alias')
        password = data.get('password')
        if alias and password:
            hashed_password = make_password(password)
            player, created = Player.objects.get_or_create(alias=alias, defaults={'password': hashed_password})
            if created:
                return JsonResponse({'alias': player.alias}, status=201)
            else:
                return JsonResponse({'error': 'Player already exists'}, status=400)
        return JsonResponse({'error': 'Invalid data'}, status=400)

def index(request):
    return HttpResponse("Hello, world! This is the Pong app.")
