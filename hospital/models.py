from django.db import models

class baseName(models.Model):
    name = models.CharField(max_length=100, null=True)

    class Meta:
        abstract = True

class Specialty(baseName):
    
    def __str__(self):
        return self.name

class Department(baseName):
    icon = models.ImageField(upload_to='images/departments/', null=True)
    bedsCount = models.IntegerField(default=0,null=True)
    monthlyPatients = models.IntegerField(default=0,null=True)
    is_Staff_Department =models.BooleanField(default=False)
    is_Doctor_Department =models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Education(baseName):

    def __str__(self):
        return self.name
    
class BaseInfo(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    education = models.ManyToManyField(Education, blank=True)
    experience = models.CharField(max_length=100, null=True, blank=True)
    recognition = models.CharField(max_length=100, null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)
    WorkingDays = models.CharField(max_length=100, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        abstract = True

class Doctor(BaseInfo):
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/doctors/', null=True, blank=True)
    schedule = models.CharField(max_length=100, null=True, blank=True)
    bmdc_registration = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        specialty_name = self.specialty.name if self.specialty else "No Specialty"
        department_name = self.department.name if self.department else "No Department"
        return f'{self.name} - {specialty_name} - {department_name}'

class Staff(BaseInfo):
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, null=True, blank=True)
    employee_id = models.CharField(max_length=100, null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/staff/', null=True, blank=True)
    schedule = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name if self.name else "No Name"} - {self.specialty.name if self.specialty else "No Specialty"} - {self.department if self.department else "No Department"}'

class Reviews(models.Model):
    name = models.CharField(max_length=100, null=True)
    review = models.TextField(null=True)
    email_or_Phone = models.CharField(max_length=100, null=True)
    rating = models.IntegerField(null=True)
    date = models.DateField(null=True)
    visibility = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Review"  # Added this line to change the display name in the admin panel
        verbose_name_plural = "Reviews"  # Added this line to ensure the plural form is correct

    def __str__(self):
        return f'{self.name} - {self.rating}' if self.name and self.rating is not None else 'No Name - No Rating'

class HospitalInfo(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100, null=True)
    phone_Two = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    home_Banner = models.ImageField(upload_to='images/home_banner/', null=True)
    home_header = models.CharField(max_length=100, null=True)
    home_header_two = models.CharField(max_length=100, null=True)


    def __str__(self):
        return f'{self.name if self.name else "No Name"}'

class PatientContactInfo(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    pending = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.subject}' if self.name and self.subject else 'No Name - No Subject'
    
    
class HospitalStats(models.Model):
    hospitalAge = models.IntegerField(null=True)
    patientsTreated = models.IntegerField(null=True)
    doctorsCount = models.IntegerField(default=0,null=True)
    staffsCount = models.IntegerField(default=0,null=True)

    class Meta:
        verbose_name = "HospitalStat"
        verbose_name_plural = "HospitalStats"

    def __str__(self):
        return f'Hospital stats: {self.hospitalAge} - {self.patientsTreated} - {self.doctorsCount} - {self.staffsCount}'

    def save(self, *args, **kwargs):
        """Override save to ensure counts are updated"""
        if not self.pk:  # If this is a new instance
            super().save(*args, **kwargs)
            self.update_counts()
        else:
            super().save(*args, **kwargs)

    def update_counts(self):
        """Method to update doctorsCount and staffsCount"""
        self.doctorsCount = Doctor.objects.count()
        self.staffsCount = Staff.objects.count()
        self.save()



class CardSliderItems(models.Model):
    title = models.CharField(max_length=100, null=True)
    class Meta:
        verbose_name = "CardSliderItem"  # Added this line to change the display name in the admin panel
        verbose_name_plural = "cardSliderItems"  # Added this line to ensure the plural form is correct
    def __str__(self):
        return f'{self.title}'

class CardSlider(models.Model):
    title = models.CharField(max_length=100, choices=[
        ('OurServices', 'Our Services'),
        ('Departments', 'Departments'),
        ('Doctors', 'Doctors'),
        ('Staffs', 'Staffs'),
    ], null=True)

    
    icon = models.ImageField(upload_to='images/cards/', null=True)
    items = models.ManyToManyField(CardSliderItems, blank=True)
    path = models.CharField(max_length=100, choices=[
        ('/services', 'Services'),
        ('/departments', 'Departments'),
        ('/doctors', 'Doctors'),
        ('/staffs', 'Staffs'),
    ], null=True)
    def __str__(self):
        return f'{self.title}'
    

class Footer(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)


    def __str__(self):
        return f'{self.title}'


class AboutPageSliderImage(models.Model):
    image = models.ImageField(upload_to='images/about/', null=True)

    def __str__(self):
        return f'{self.image}'
class AboutPagePointedText(models.Model):
    text = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.text}'
class AboutPageCardText(models.Model):
    icon = models.ImageField(upload_to='images/about_page_cards/', null=True)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.title}'

class About(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image_slider = models.ManyToManyField(AboutPageSliderImage, blank=True)
    image_two = models.ImageField(upload_to='images/about/', null=True)
    title_two = models.CharField(max_length=100, null=True)
    description_two = models.TextField(null=True)
    pointed_text = models.ManyToManyField(AboutPagePointedText, blank=True)
    card_text = models.ManyToManyField(AboutPageCardText, blank=True)

    def __str__(self):
        return f'{self.title}'


#services page models
class Services_list(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = "Services_list"
        verbose_name_plural = "Services_lists"


class Service(models.Model):
    icon = models.ImageField(upload_to='images/services/', null=True)
    title = models.CharField(max_length=100, null=True)
    services = models.ManyToManyField(Services_list, blank=True)

    def __str__(self):
        return f'{self.title}'

class Why_Trust_us(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    icon = models.ImageField(upload_to='images/why_trust_us/', null=True)

    class Meta:
        verbose_name = "Why Trust Us"
        verbose_name_plural = "Why Trust Uss"

    def __str__(self):
        return f'{self.title}'
    

