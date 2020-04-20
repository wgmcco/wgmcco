from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import PermitProfile, AgencyProfile, InsuranceProfile, ContactProfile, SubProfile, VehicleProfile

class PermitProfileListView(ListView):
    model = PermitProfile

def home(request):
    trucks = VehicleProfile.objects.all()
    return render(request, 'permits/dashboard.html', {'trucks': trucks})


def truck(request):
    trucks = VehicleProfile.objects.all()
    return render(request, 'permits/truck.html', {'trucks': trucks})


def sub(request):
    subs = SubProfile.objects.all()
    return render(request, 'permits/sub.html', {'subs': subs})


def contact(request):
    contacts = ContactProfile.objects.all()
    return render(request, 'permits/contact.html', {'contacts': contacts})


def insurance(request):
    insurances = InsuranceProfile.objects.all()
    return render(request, 'permits/insurance.html', {'insurances': insurance})


def agency(request):
    agencies = AgencyProfile.objects.all()
    return render(request, 'permits/agency.html', {'agencies': agencies})


def permit(request):
    permits = PermitProfile.objects.all()
    return render(request, 'permits/permit.html', {'permits': permits})


