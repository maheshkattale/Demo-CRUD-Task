from django.shortcuts import render, redirect, HttpResponse
import requests
import json
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from helpers.static_info import hosturl

def landing_page(request):
    if request.method == 'GET':
        users_url=hosturl+'/api/user/user-list-api'
        users_request = requests.get(users_url)
        users_response = users_request.json()


        third_party_url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(third_party_url, timeout=10)
        response.raise_for_status() 
        third_party_data = response.json()

        context = {
            'users': users_response['data'],
            'third_party_data': third_party_data
        }
        
        return render(request, 'landing.html', context)
    else:
        return HttpResponse("Invalid Method")