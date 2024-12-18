from django.urls import path
from .views import doctor_list, specialty_list, department_list, staff_list, review_list, hospital_info, patient_contact,staff_detail, review_detail

urlpatterns = [
    path('doctors/', doctor_list, name='doctor-list'),
    path('specialties/', specialty_list, name='specialty-list'),
    path('departments/', department_list, name='department-list'),
    path('staff/', staff_list, name='staff-list'),
    path('staff/<int:pk>/', staff_detail, name='staff-detail'),
    path('reviews/', review_list, name='review-list'),
    path('reviews/<int:pk>/', review_detail, name='review-detail'),
    path('hospital-info/', hospital_info, name='hospital-info'),
    path('contact/', patient_contact, name='patient-contact'),
]
