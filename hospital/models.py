from django.db import models

class baseName(models.Model):
    name = models.CharField(max_length=100, null=True)

    class Meta:
        abstract = True

class Specialty(baseName):
    
    def __str__(self):
        return self.name

class Department(baseName):

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
        






