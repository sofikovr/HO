from django.shortcuts import render

# Create your views here.
from django.views import View


class MainView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class DepartureView(View):

    def get(self, request, departure):
        return render(request, 'departure.html')

class TourView(View):

    def get(self, request, id):
        return render(request, 'tour.html')
