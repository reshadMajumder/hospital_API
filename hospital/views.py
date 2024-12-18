from rest_framework.decorators import api_view
from .models import Doctor, Specialty, Department,Staff,Reviews, HospitalInfo, PatientContactInfo
from .serializers import DoctorSerializer, SpecialtySerializer, DepartmentSerializer, StaffSerializer, ReviewsSerializer, HospitalInfoSerializer, PatientContactInfoSerializer
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def doctor_list(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def specialty_list(request):
    if request.method == 'GET':
        specialties = Specialty.objects.all()
        serializer = SpecialtySerializer(specialties, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SpecialtySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def department_list(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def staff_list(request):
    if request.method == 'GET':
        staffs = Staff.objects.all()
        serializer = StaffSerializer(staffs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        # Only return visible reviews
        reviews = Reviews.objects.filter(visibility=True)
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def hospital_info(request):
    """
    Get hospital information. Since there should only be one record,
    we'll return the first one or create a default if none exists.
    """
    try:
        info = HospitalInfo.objects.first()
        if not info:
            # Create default hospital info if none exists
            info = HospitalInfo.objects.create(
                name="Default Hospital Name",
                email="default@hospital.com",
                phone="123-456-7890",
                address="Default Address"
            )
        serializer = HospitalInfoSerializer(info)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['POST'])
def patient_contact(request):
    """
    Handle patient contact form submissions
    """
    if request.method == 'POST':
        serializer = PatientContactInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Thank you for contacting us. We will get back to you soon.",
                "data": serializer.data
            }, status=201)
        return Response(serializer.errors, status=400)

# Optional: Individual detail views for each model
@api_view(['GET', 'PUT', 'DELETE'])
def staff_detail(request, pk):
    try:
        staff = Staff.objects.get(pk=pk)
    except Staff.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = StaffSerializer(staff)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        staff.delete()
        return Response(status=204)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):
    try:
        review = Reviews.objects.get(pk=pk)
    except Reviews.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ReviewsSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewsSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=204)



