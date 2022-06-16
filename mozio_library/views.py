from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from shapely.geometry import Polygon, Point

from mozio_library.models import Provider, ServiceArea
from mozio_library.serializers import ProviderSerializer, ServiceAreaSerializer, QuerySerializer

# Create your views here.
def index(request):
    
     return HttpResponse('WELCOME TO MOZIO')

class ProviderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()
    
class ProviderList(generics.ListCreateAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()

class ServiceAreaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =  ServiceAreaSerializer
    queryset = ServiceArea.objects.all()

class ServiceAreaList(generics.ListCreateAPIView):
    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()
    
@api_view(['GET'])
def query(request):
    
    lat = request.GET.get('lat', None)
    lng = request.GET.get('lng', None)
    
    if lat is None or lng is None:
        return HttpResponse('Not Found')
    
    point = Point(float(lat), float(lng))
    
    selected_polygon = []
    
    queryset = ServiceArea.objects.all()
    
    for polygons in queryset:
        polygon_coordination = polygons.poly
        eval_polygon_coordination = eval(polygon_coordination)
        polygon = Polygon(eval_polygon_coordination)
        
        if polygon.contains(point):
            selected_polygon.append(polygons)
            
    if len(selected_polygon) == 0:
        return Response('Provider is not available')
    
    serializer = QuerySerializer(selected_polygon, many=True)
    return Response(serializer.data)

class Query(generics.ListAPIView):
    serializer_class = QuerySerializer
    def queryset(self):
        lat = request.GET.get('lat', None)
        lng = request.GET.get('lng', None)
        if lat is None or lng is None:
            return HttpResponse('Not Found')
        point = Point(float(lat), float(lng))
        selected_polygon = []
        queryset = ServiceArea.objects.all()
        for polygons in queryset:
            polygon_coordination = polygons.poly
            eval_polygon_coordination = eval(polygon_coordination)
            polygon = Polygon(eval_polygon_coordination)
            if polygon.contains(point):
                selected_polygon.append(polygons)
            
            return selected_polygon
        
