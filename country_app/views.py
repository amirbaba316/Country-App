from django.shortcuts import render
from django.views import View
from .forms import NameForm
import requests
import json
import folium 

DATA=[]

def index(country):
    response = requests.get("https://restcountries-v1.p.rapidapi.com/name/"+country,
    headers={
    "X-RapidAPI-Host": "restcountries-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "08e9ab565fmsh7c70bca2b876f81p118bd5jsna8ccec295ff9"
    }
    )
    return response.text

class Country_detail(View):
    form_class=NameForm
    def get(self,request):
        return render(request, 'country_current/detail.html',{'form': self.form_class()})

    def post(self,request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            name=bound_form.cleaned_data.get('Country')
            try:
                detail=json.loads(index(name))
                for i in detail:
                    if i["name"]==name.title():
                        det_keys=i.keys()
                        det_values=i.values()
                        myList=zip(det_keys,det_values)
                        global DATA
                        DATA=[]
                        DATA.append(i['latlng'][0])
                        DATA.append(i['latlng'][1])
                        DATA.append(i['name'])
                        break
                return render(request,"country_current/country.html",{'myList':myList})
            except:
                return render(request,"country_current/oops.html",{'d':name+"  is not a country."})
        else:
            return render(request,'country_current/detail.html',{'form': bound_form})

class map_view(View):
    def get(self, request):
        lat= DATA[0]
        lon= DATA[1]
        name=DATA[2]
        map5 = folium.Map(location=[lat,lon],zoom_start=6,tiles = "Stamen Terrain")  
        folium.Marker(location=[lat,lon],popup=name, icon= folium.Icon(color="red",icon_color='white',icon='info-sign')).add_to(map5) 
        map5.save('templates/country_current/map.html')
        return render(request, 'country_current/map.html')
            





# Create your views here.
