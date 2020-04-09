from django.contrib import admin

from .models import ContactProfile, CustomerProfile, InsuranceProfile, VehicleProfile, AgencyProfile, PermitProfile

admin.site.register(ContactProfile)
admin.site.register(CustomerProfile)
admin.site.register(InsuranceProfile)
admin.site.register(VehicleProfile)
admin.site.register(AgencyProfile)
admin.site.register(PermitProfile)