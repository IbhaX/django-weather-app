# Django Imports
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Subquery, OuterRef, Max
from django.urls import reverse_lazy, reverse
from django.contrib import messages

# User imports
from .forms import CityForm
from .models import Current, Location
from .utils import save_weather_data

#----------------------------------------------------------

class HomeView(LoginRequiredMixin, ListView):
    model = Current
    template_name = 'app/home.html'
    context_object_name = 'weather_data'

    def get_queryset(self):
        # Retrieve the latest weather data for each unique city for the current user
        subquery = Current.objects.filter(user=self.request.user, location_id=OuterRef('location_id')).values('location_id').annotate(max_last_updated=Max('last_updated')).values('max_last_updated')
        unique_cities = Current.objects.filter(user=self.request.user, last_updated__in=subquery)
        return unique_cities

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CityForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CityForm(request.POST)

        if form.is_valid():
            city = form.cleaned_data.get("city_name")
            save_weather_data(city, request.user, aqi=True)
            messages.success(request, "Data saved to database")
            print("Data saved")

        return self.get(request, *args, **kwargs)


def clear_data(request):
    Current.objects.filter(user=request.user).delete()
    messages.success(request, "Weather data cleared successfully")
    return redirect(reverse('app:home'))