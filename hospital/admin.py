from django.contrib import admin
from django.utils.html import format_html
from django import forms
from django.utils.translation import gettext_lazy as _

# Register your models here.
from .models import (
    Doctor, Specialty, Department, Education, Staff, Reviews,
    HospitalInfo, PatientContactInfo, HospitalStats, CardSlider,
    CardSliderItems, About, AboutPageSliderImage, AboutPagePointedText,
    AboutPageCardText, Service, Services_list, Footer, Why_Trust_us
)






class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'department', 'show_image')
    readonly_fields = ['image_tag']  # Make it visible in the detail view


    def show_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 30px; height: 30px;" />', obj.image.url)
        return "No Image"
    show_image.short_description = 'Image'

    def image_tag(self, obj):
        if obj.image:  # Check if an image exists
            return format_html('<img src="{}" style="max-width: 150px; height: auto;" />', obj.image.url)
        return "No Image"
    image_tag.short_description = 'Current Image'



class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'department', 'show_image')
    readonly_fields = ['image_tag']  # Make it visible in the detail view

    def show_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 30px; height: 30px;" />', obj.image.url)
        return "No Image"
    show_image.short_description = 'Image'

    def image_tag(self, obj):
        if obj.image:  # Check if an image exists
            return format_html('<img src="{}" style="max-width: 150px; height: auto;" />', obj.image.url)
        return "No Image"
    image_tag.short_description = 'Current Image'










from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Custom Admin Site
class CustomAdminSite(admin.AdminSite):
    site_header = "Hospital Admin Panel"
    site_title = "Hospital Admin"
    index_title = "Welcome to the Hospital Admin Panel"

    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        
        # Define your model groups with proper names
        main_content = {
            'Doctor': 'Doctors Management',
            'Department': 'Departments',
            'Staff': 'Staff Members',
            'Reviews': 'Patient Reviews',
            'HospitalInfo': 'Hospital Information',
            'HospitalStats': 'Hospital Statistics',
            'Service': 'Services Management',
            'About': 'About Page Content',
            'Footer': 'Footer Content',
            'Why_Trust_us': 'Why Trust Us Section'
        }
        
        extra_content = {
            'Specialty': 'Medical Specialties',
            'Education': 'Educational Qualifications',
            'PatientContactInfo': 'Patient Inquiries',
            'CardSlider': 'Homepage Cards',
            'CardSliderItems': 'Card Items',
            'AboutPageSliderImage': 'About Page Images',
            'AboutPagePointedText': 'About Page Points',
            'AboutPageCardText': 'About Page Cards',
            'Services_list': 'Services List'
        }

        grouped_apps = [
            {
                'name': _('Main Content'),
                'models': []
            },
            {
                'name': _('Additional Content'),
                'models': []
            }
        ]

        # Group Models with proper names
        for app in app_dict.values():
            for model in app['models']:
                model_name = model['object_name']
                if model_name in main_content:
                    model['name'] = main_content[model_name]
                    grouped_apps[0]['models'].append(model)
                elif model_name in extra_content:
                    model['name'] = extra_content[model_name]
                    grouped_apps[1]['models'].append(model)

        # Sort models alphabetically within each group
        for group in grouped_apps:
            group['models'].sort(key=lambda x: x['name'])

        return grouped_apps


# Register Custom Admin Site
custom_admin_site = CustomAdminSite(name='custom_admin')

# Register models with custom names
custom_admin_site.register(Doctor, DoctorAdmin)
custom_admin_site.register(Department)
custom_admin_site.register(Staff, StaffAdmin)
custom_admin_site.register(Reviews)
custom_admin_site.register(HospitalInfo)
custom_admin_site.register(HospitalStats)
custom_admin_site.register(About)
custom_admin_site.register(Service)
custom_admin_site.register(Footer)
custom_admin_site.register(Why_Trust_us)
custom_admin_site.register(Specialty)
custom_admin_site.register(Education)
custom_admin_site.register(PatientContactInfo)
custom_admin_site.register(CardSlider)
custom_admin_site.register(CardSliderItems)
custom_admin_site.register(AboutPageSliderImage)
custom_admin_site.register(AboutPagePointedText)
custom_admin_site.register(AboutPageCardText)
custom_admin_site.register(Services_list)
