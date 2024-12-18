from django.db import models

# Create your models here.


from django.db import models


class Staff(models.Model):
    # Personal Information
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    adresse = models.CharField(max_length=255)
    date_naissance = models.DateField()

    # Password (as plain text, no hashing)
    mot_de_passe = models.CharField(max_length=255)

    # Role (e.g., Admin, Manager, etc.)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    class Meta:
        db_table = 'staff'




class Patient(models.Model):
    # Personal Information
    nss = models.CharField(max_length=15, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    mutuelle = models.CharField(max_length=100)
    personne_a_contacter = models.CharField(max_length=100)
    telephone_a_contacter = models.CharField(max_length=20)
  
     # Password (as plain text, no hashing)
    mot_de_passe = models.CharField(max_length=255)


    # medecin_traitant is a foreign key
    medecin_traitant = models.ForeignKey(Staff, on_delete=models.CASCADE) 
    #on_delete=models.CASCADE means that if the medecin_traitant is deleted
    #every patient associated with it will be deleted


    def __str__(self):
        return f"{self.nom} {self.prenom}"
    class Meta:
        
        db_table = 'patient'




class DossierPatient(models.Model):
    # un DossierPatient doit referencer le patient
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    etat = models.CharField(max_length=20)
    antécédents = models.TextField()

    def __str__(self):
        return f"Dossier for {self.patient.nom} {self.patient.prenom}"
    class Meta:
        db_table = 'Dossier_patient'