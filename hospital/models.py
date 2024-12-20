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

    def __str__(self):
        return self.name
    
class Education(baseName):

    def __str__(self):
        return self.name
    
class BaseInfo(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    education = models.ManyToManyField(Education, null=True)
    experience = models.CharField(max_length=100, null=True)
    recognition = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=100, null=True)
    WorkingDays = models.CharField(max_length=100, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)

    class Meta:
        abstract = True

class Doctor(BaseInfo):
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/doctors/', null=True)
    schedule = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.name} - {self.specialty.name} - {self.department.name}'

class Staff(BaseInfo):
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/staff/', null=True)
    schedule = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.name} - {self.specialty.name} - {self.department.name}'

class Reviews(models.Model):
    name = models.CharField(max_length=100, null=True)
    review = models.TextField(null=True)
    rating = models.IntegerField(null=True)
    date = models.DateField(null=True)
    visibility = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Review"  # Added this line to change the display name in the admin panel
        verbose_name_plural = "Reviews"  # Added this line to ensure the plural form is correct

    def __str__(self):
        return f'{self.name} - {self.rating}'

class HospitalInfo(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'

class PatientContactInfo(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'
        
class HospitalStats(models.Model):
    hospitalAge = models.IntegerField(null=True)
    patientsTreated = models.IntegerField(null=True)
    doctorsCount = models.IntegerField(default=0, null=True)  # Use 0 as the default value
    staffsCount = models.IntegerField(default=0, null=True)  # Use 0 as the default value

    class Meta:
        verbose_name = "HospitalStat"  # Changed display name in admin panel
        verbose_name_plural = "HospitalStats"  # Correct plural form

    def __str__(self):
        return f'Hospital stats: {self.hospitalAge} - {self.patientsTreated} - {self.doctorsCount} - {self.staffsCount}'

    def update_counts(self):
        """Method to update doctorsCount and staffsCount dynamically."""
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
    items = models.ManyToManyField(CardSliderItems, null=True)
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
        return f'{self.name}'
