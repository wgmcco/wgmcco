from django.contrib import admin

from .models import ContactProfile, SubProfile, InsuranceProfile, VehicleProfile, AgencyProfile, PermitProfile

admin.site.register(ContactProfile)
admin.site.register(SubProfile)
admin.site.register(InsuranceProfile)
admin.site.register(VehicleProfile)
admin.site.register(AgencyProfile)
admin.site.register(PermitProfile)