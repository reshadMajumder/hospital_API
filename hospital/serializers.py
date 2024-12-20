from rest_framework import serializers
from .models import Doctor, Specialty, Department, HospitalInfo, PatientContactInfo,Reviews,Staff ,Education, HospitalStats, CardSlider, CardSliderItems

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer()
    education = EducationSerializer(many=True)
    department = DepartmentSerializer()

    class Meta:
        model = Doctor
        fields = '__all__'
        
        # def get_image(self, obj):
        #     request = self.context.get('request')
        #     if obj.image:
        #         return request.build_absolute_uri(obj.image.url)
        #     return None

class HospitalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalInfo
        fields = '__all__'

class PatientContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientContactInfo
        fields = '__all__'

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer()
    education = EducationSerializer(many=True)
    department = DepartmentSerializer()

    class Meta:
        model = Staff
        fields = '__all__'
        


class HospitalStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalStats
        fields = '__all__'


class CardSliderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardSliderItems
        fields = '__all__'


class CardSliderSerializer(serializers.ModelSerializer):
    items = CardSliderItemsSerializer(many=True)
    class Meta:
        model = CardSlider
        fields = '__all__'

