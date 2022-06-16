from django.contrib import admin
from django.urls import path, include
from mozio_library.views import index, ProviderDetail, ProviderList, ServiceAreaDetail, ServiceAreaList, query

urlpatterns = [
    path('', index),
    path('main_provider/', ProviderList.as_view()),
    path('provider/<int:pk>/', ProviderDetail.as_view()),
    path('main_polygon/', ServiceAreaList.as_view()),
    path('polygon/<int:pk>/', ServiceAreaDetail.as_view()),
    path('query/', query),
]