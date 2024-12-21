from django.core.management.base import BaseCommand
from hospital.models import HospitalStats

class Command(BaseCommand):
    help = 'Updates the hospital statistics counts'

    def handle(self, *args, **kwargs):
        stats = HospitalStats.objects.first()
        if stats:
            stats.update_counts()
            self.stdout.write(self.style.SUCCESS('Successfully updated hospital stats'))
        else:
            self.stdout.write(self.style.ERROR('No HospitalStats instance found')) 