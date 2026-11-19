from django.urls import path

from . import views, api
from DHT.views import dashboard

urlpatterns= [
    path('test/',views.test),
    path("api/get", api.Dlist, name='json'),
    path("api/post", api.Dhtviews.as_view(), name='json'),
    path("dashboard/", dashboard, name="dashboard"),
]