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
        unique_cities_subquery = (
            Current.objects
            .filter(location__user=self.request.user, location_id=OuterRef('location_id'))
            .order_by('-last_updated')
            .values('id')[:1]
        )

        unique_cities = (
            Current.objects
            .filter(id__in=Subquery(unique_cities_subquery))
            .select_related('location')  # Assuming location is a ForeignKey in Current model
        )

        return unique_cities

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CityForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CityForm(request.POST)

        if form.is_valid():
            city = form.cleaned_data.get("city_name")
            if save_weather_data(city, request.user, aqi=True):
                messages.success(request, "Data saved to database")
            else:
                messages.error(request, "City not found")
        return self.get(request, *args, **kwargs)

class ClearDataView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        Location.objects.filter(user=request.user).delete()
        messages.success(request, "Weather data cleared successfully")
        return redirect(reverse('app:home'))


class RefreshDataView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # Perform the data refresh logic here
        # For example, you might want to retrieve the latest data for all saved cities
        saved_cities = Location.objects.filter(user=request.user)
        for city in saved_cities:
            save_weather_data(city.name, request.user, aqi=True)

        messages.success(request, "Weather data refreshed successfully")
        return redirect(reverse('app:home'))