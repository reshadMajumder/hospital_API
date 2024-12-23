from django.urls import path
from .views import doctor_list, specialty_list, department_list, staff_list, review_list, hospital_info, patient_contact,staff_detail, hospital_stats,review_detail,card_slider, search_doctors, single_doctor_detail, about_page, services_page,footer, why_trust_us

urlpatterns = [
    path('doctors/', doctor_list, name='doctor-list'),
    path('doctors/<int:pk>/', single_doctor_detail, name='doctor-detail'),
    path('specialties/', specialty_list, name='specialty-list'),
    path('departments/', department_list, name='department-list'),
    path('staff/', staff_list, name='staff-list'),
    path('staff/<int:pk>/', staff_detail, name='staff-detail'),
    path('reviews/', review_list, name='review-list'),
    path('reviews/<int:pk>/', review_detail, name='review-detail'),
    path('hospital-info/', hospital_info, name='hospital-info'),
    path('contact/', patient_contact, name='patient-contact'),
    path('hospital-stats/', hospital_stats, name='hospital-stats'),
    path('card-slider/', card_slider, name='card-slider'),
    path('why-trust-us/', why_trust_us, name='why-trust-us'),
    path('doctors/search/', search_doctors, name='search-doctors'),
    path('about/', about_page, name='about-page'),
    path('services/', services_page, name='services-page'),
    path('footer/', footer, name='footer'), #footer
]
