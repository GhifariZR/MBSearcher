from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import requests
import json

def tampilan_music(request):
    response={}
    return render(request,'musics/search.html',response)

def pengolahan_data_music(request):
	url = "https://spotify23.p.rapidapi.com/search/"
	querystring = {"q":request.GET['q'],"type":"multi","offset":"0","limit":"10","numberOfTopResults":"5"}
	headers = {
	"X-RapidAPI-Key": "1a66cd301cmshebed91db003ba62p1ef918jsnedb81fae8faf",
	"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	data= json.loads(response.content)
	return JsonResponse(data,safe=False)
# Create your views here.
