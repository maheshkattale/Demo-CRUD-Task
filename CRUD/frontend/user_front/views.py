from django.shortcuts import render, redirect, HttpResponse
import requests
import json
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from helpers.static_info import hosturl
# Trip API URLs

def landing_page(request):
    if request.method == 'GET':
        users_url=hosturl+'/api/user/user-list-api'
        users_request = requests.get(users_url)
        users_response = users_request.json()
        print("users_response",users_response)

        context = {
            'users': users_response['data'],
        }
        
        return render(request, 'landing.html', context)
    else:
        return HttpResponse("Invalid Method")