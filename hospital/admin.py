from django.contrib import admin
from django.utils.html import format_html
from django import forms

# Register your models here.
from .models import Doctor, Specialty, Department,Education,Staff,Reviews,HospitalInfo,PatientContactInfo,HospitalStats,CardSlider,CardSliderItems, About, AboutPageSliderImage, AboutPagePointedText, AboutPageCardText,Service,Services_list,Footer, Why_Trust_us






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

        # Define Main Content and Extra Content sections
        main_content = [
            'Doctor', 'Department', 'Staff', 'Reviews', 
            'HospitalInfo', 'HospitalStats', 'Service', 'About',
            'Footer', 'Why_Trust_us'
        ]
        extra_content = [
            'Specialty', 'Education', 'PatientContactInfo', 
            'CardSlider', 'CardSliderItems', 'AboutPageSliderImage',
            'AboutPagePointedText', 'AboutPageCardText', 'Services_list'
        ]

        grouped_apps = [
            {
                'name': _('Main Content'),
                'models': []
            },
            {
                'name': _('Extra Content'),
                'models': []
            }
        ]

        # Group Models
        for app in app_dict.values():
            for model in app['models']:
                model_name = model['object_name']
                if model_name in main_content:
                    grouped_apps[0]['models'].append(model)
                elif model_name in extra_content:
                    grouped_apps[1]['models'].append(model)

        return grouped_apps


# Register Custom Admin Site
custom_admin_site = CustomAdminSite(name='custom_admin')

# Import and Register Models



custom_admin_site.register(Doctor,DoctorAdmin)
custom_admin_site.register(Department)
custom_admin_site.register(Staff,StaffAdmin)
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

# # Main Content
# admin.site.register(Doctor, DoctorAdmin)
# admin.site.register(Department)
# admin.site.register(Staff, StaffAdmin)
# admin.site.register(Reviews)
# admin.site.register(HospitalInfo)
# admin.site.register(HospitalStats)
# admin.site.register(About)
# admin.site.register(Service)
# admin.site.register(Footer)
# admin.site.register(Why_Trust_us)


# # Other Items
# admin.site.register(Specialty)
# admin.site.register(Education)
# admin.site.register(PatientContactInfo)
# admin.site.register(CardSlider)
# admin.site.register(CardSliderItems)
# admin.site.register(AboutPageSliderImage)
# admin.site.register(AboutPagePointedText)
# admin.site.register(AboutPageCardText)
# admin.site.register(services_list)
