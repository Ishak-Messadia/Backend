from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Staff
from .models import Patient
from .models import DossierPatient
from .serializers import StaffSerializer
from .serializers import PatientSerializer
from .serializers import DossierPatientSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes

@api_view(['POST'])
def register_staff(request):
    # Instantiate the serializer with the incoming data
    serializer = StaffSerializer(data=request.data)

    # Validate and save the data
    if serializer.is_valid():
        # Save the staff instance to the database
        serializer.save()

        # Return a success message and 201 status code (Created)
        return Response({"message": "Staff registered successfully!"}, status=status.HTTP_201_CREATED)

    # If validation fails, return the errors with a 400 status code (Bad Request)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def register_patient(request):
    # Instantiate the serializer with the incoming data
    serializer = PatientSerializer(data=request.data)

    # Check if the serializer is valid
    if serializer.is_valid():
        # Save the patient instance to the database
        patient = serializer.save()

        # Now, create the DossierPatient for the newly created patient
        dossier_data = {
            'patient': patient.id,  # Link the dossier to the patient
            'etat': 'Actif',         # Default value for "etat" (Active)
            'antécédents': '/'       # Default value for "antécédents" (can be updated later)
        }

        # Create the DossierPatient
        dossier_serializer = DossierPatientSerializer(data=dossier_data)

        if dossier_serializer.is_valid():
            dossier_serializer.save()  # Save the DossierPatient

            # Return a success message along with a 201 status code
            return Response({"message": "Patient registered and DossierPatient created succesfuly!"}, status=status.HTTP_201_CREATED)
        else:
            # If DossierPatient validation fails, delete the patient and return an error
            patient.delete()
            return Response(dossier_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # If the patient serializer validation fails, return the error
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def get_medecins(request):
    # Fetch all staff with the role 'medecin' (doctor)
    staff_members = Staff.objects.filter(role='medecin')
    
    # Serialize the staff data
    serializer = StaffSerializer(staff_members, many=True)
    
    # Return the serialized data as a JSON response
    return Response(serializer.data)





@api_view(['POST'])
def login_staff(request):
    # Extract email and password from request data
    email = request.data.get('email')
    password = request.data.get('mot_de_passe')


    # Check if staff exists in the database
    try:
        staff = Staff.objects.get(email=email)
    except Staff.DoesNotExist:
        return Response({"message": "Staff not found"}, status=status.HTTP_404_NOT_FOUND)

    # Compare provided password with the stored one (plain text comparison)
    if staff.mot_de_passe != password:
        return Response({"message": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)

    # If the credentials are correct, return success message
    return Response({"message": "Login successful"}, status=status.HTTP_200_OK)



@api_view(['POST'])
def login_patient(request):
    # Extract nss (National Social Security number) and password from request data
    nss = request.data.get('nss')
    password = request.data.get('mot_de_passe')

    # Check if patient exists in the database
    try:
        patient = Patient.objects.get(nss=nss)
    except Patient.DoesNotExist:
        return Response({"message": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

    # Compare provided password with the stored one (plain text comparison)
    if patient.mot_de_passe != password:
        return Response({"message": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)

    # If the credentials are correct, return success message
    return Response({"message": "Login successful"}, status=status.HTTP_200_OK)




@api_view(['POST'])
def rechercher_patient_par_NSS(request):
    nss = request.data.get('nss')  # Getting NSS from the request data
    try:
        # Try to fetch the patient by NSS
        patient = Patient.objects.get(nss=nss)

        # Fetch the associated DossierPatient
        dossier_patient = DossierPatient.objects.get(patient=patient)

        # Serialize both the patient and dossier data
        patient_serializer = PatientSerializer(patient)
        dossier_patient_serializer = DossierPatientSerializer(dossier_patient)

        # Return both the patient and dossier data in the response
        return Response({
            "patient": patient_serializer.data,
            "dossier_patient": dossier_patient_serializer.data
        }, status=status.HTTP_200_OK)

    except Patient.DoesNotExist:
        # If no patient is found, return an error message
        return Response({"message": "No patient found with the provided NSS."}, status=status.HTTP_404_NOT_FOUND)
    except DossierPatient.DoesNotExist:
        # If no DossierPatient is found, return an error message
        return Response({"message": "No DossierPatient found for the provided patient."}, status=status.HTTP_404_NOT_FOUND)
