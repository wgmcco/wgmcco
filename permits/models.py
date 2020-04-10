from django.db import models
from django.utils import timezone


class ContactProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    st = models.CharField(max_length=150, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    fax = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    ss = models.CharField(max_length=9, blank=True)
    emergence_name = models.CharField(max_length=20, blank=True)
    emergence_phone = models.CharField(max_length=20, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )
    employer = models.ForeignKey('SubProfile', on_delete=models.CASCADE, null=True, blank=True)
    experience = models.TextField(blank=True)
    dob = models.DateField()
    cdl = models.ImageField(upload_to='contact_cdl', blank=True)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta(object):
        unique_together = ("first_name", "last_name")
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SubProfile(models.Model):
    name = models.CharField(max_length=150, unique=True)
    contact_name = models.ForeignKey(ContactProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    st = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    email = models.EmailField(max_length=150)
    website = models.CharField(max_length=200)
    ein_ss = models.CharField(max_length=9)
    business_lic = models.CharField(max_length=9)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta(object):
        verbose_name = "Sub Contractor"
        verbose_name_plural = "Sub Contractors"

    def __str__(self):
        return f"{self.name}"


class InsuranceProfile(models.Model):
    CERT_CHOICES = (
        ('WC', 'Work Comp'),
        ('GL', 'General Liability'),
        ('AT', 'Auto'),
        ('UM', 'Umbrella')
    )
    name = models.ForeignKey(SubProfile, on_delete=models.CASCADE)
    cert_number = models.CharField(max_length=50)
    cert_type = models.CharField(
        max_length=2,
        choices=CERT_CHOICES,
    )
    policy_number = models.CharField(max_length=150)
    expires = models.DateField()
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} -  {self.cert_type}"


class AgencyProfile(models.Model):
    name = models.CharField(max_length=150, unique=True)
    point_name = models.ManyToManyField(ContactProfile)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    st = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    email = models.EmailField(max_length=150, default='unk@unk.com')
    website = models.CharField(max_length=200, blank=True)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class VehicleProfile(models.Model):
    ENGINE_CHOICES = (
        (8, '8 Cylinder'),
        (6, '6 Cylinder'),
        (4, '4 Cylinder'),
    )
    TRAN_CHOICES = (
        ('A', 'Automatic'),
        ('S', 'Standard'),
    )
    AXLE_CHOICES = (
        (2, '2 axles'),
        (3, '3 axles'),
        (4, '4 axles'),
    )
    EQUIPMENT_CHOICES = (
        ('SU', 'Super Dump'),
        ('LB', 'Low Bed'),
        ('SW', 'Sweeper'),
        ('WT', 'Water Truck'),
        ('FB', 'Flat Bed'),
    )
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('D', 'Down In Shop'),
        ('N', 'Non-Op'),
        ('J', 'Junked'),
        ('S', 'Sold'),
    )

    eq_number = models.CharField(max_length=150, unique=True)
    make = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    year = models.CharField(max_length=150)
    lic = models.CharField(max_length=150)
    vin = models.CharField(max_length=150)
    veh_type = models.CharField(
        max_length=2,
        choices=EQUIPMENT_CHOICES,
    )
    description = models.CharField(max_length=150)
    attached_to = models.CharField(max_length=150, blank=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default='A',
    )
    mileage = models.CharField(max_length=150)
    hours = models.CharField(max_length=150)
    color = models.CharField(max_length=150)
    length = models.CharField(max_length=150)
    width = models.CharField(max_length=150)
    height = models.CharField(max_length=150)
    wheelbase = models.CharField(max_length=150)
    gvw = models.CharField("GVW", max_length=150)
    engine_size = models.PositiveSmallIntegerField(
        choices=ENGINE_CHOICES,
        default=8,
    )
    transmission = models.CharField(
        max_length=1,
        choices=TRAN_CHOICES,
    )
    axle = models.PositiveSmallIntegerField(
        choices=AXLE_CHOICES,
        default=2,
    )
    front_size = models.CharField(max_length=150)
    rear_size = models.CharField(max_length=150)
    veh_picture = models.ImageField(upload_to='veh_images', blank=True)
    owner = models.ForeignKey(SubProfile, on_delete=models.CASCADE)
    driver = models.ForeignKey(ContactProfile, on_delete=models.CASCADE)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta(object):
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

    def __str__(self):
        return f"{self.owner.name} - {self.eq_number}"


class PermitProfile(models.Model):
    permit_cn = models.CharField("Permit number", max_length=150, unique=True)
    agency_name = models.ForeignKey(AgencyProfile, on_delete=models.PROTECT)
    sub_name = models.ForeignKey(SubProfile, on_delete=models.CASCADE)
    valid_from = models.DateField()
    valid_to = models.DateField()
    permit_class = models.CharField(max_length=150)
    eq_number = models.ForeignKey(VehicleProfile, on_delete=models.CASCADE)
    pdf = models.FileField('PDF', upload_to='permit_pdf', blank=True)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.permit_cn

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)


