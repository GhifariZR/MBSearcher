from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import requests
import json
# Create your views here.
def tampilan(request):
    response={}
    return render(request,'books/search.html',response)

def pengolahan_data(request):
    url= "https://www.googleapis.com/books/v1/volumes?q=" + request.GET['q']
    ret= requests.get(url)
    data= json.loads(ret.content)
    return JsonResponse(data,safe=False)