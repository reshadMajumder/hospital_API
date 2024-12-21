from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Doctor, Staff, HospitalStats

def update_hospital_stats():
    """Update the counts in HospitalStats"""
    stats = HospitalStats.objects.first()
    if stats:
        stats.doctorsCount = Doctor.objects.count()
        stats.staffsCount = Staff.objects.count()
        stats.save()

@receiver(post_save, sender=Doctor)
def doctor_saved(sender, instance, **kwargs):
    """Signal to update stats when a doctor is saved"""
    update_hospital_stats()

@receiver(post_delete, sender=Doctor)
def doctor_deleted(sender, instance, **kwargs):
    """Signal to update stats when a doctor is deleted"""
    update_hospital_stats()

@receiver(post_save, sender=Staff)
def staff_saved(sender, instance, **kwargs):
    """Signal to update stats when a staff member is saved"""
    update_hospital_stats()

@receiver(post_delete, sender=Staff)
def staff_deleted(sender, instance, **kwargs):
    """Signal to update stats when a staff member is deleted"""
    update_hospital_stats() 