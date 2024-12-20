from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Doctor, Specialty, Department,Education,Staff,Reviews,HospitalInfo,PatientContactInfo,HospitalStats,CardSlider,CardSliderItems



    

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



admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Specialty)
admin.site.register(Department)
admin.site.register(Education)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Reviews)
admin.site.register(HospitalInfo)
admin.site.register(PatientContactInfo)
admin.site.register(HospitalStats)
admin.site.register(CardSlider)
admin.site.register(CardSliderItems)
