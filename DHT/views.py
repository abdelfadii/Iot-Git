from django.http import HttpResponse
from django.shortcuts import render


def test(request) :
    return HttpResponse('Abdellah fadhi, Ahmed Azzaoui')
def dashboard(request):
    return render(request, "dashboard.html")