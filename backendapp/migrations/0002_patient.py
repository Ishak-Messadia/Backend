# Generated by Django 5.1.4 on 2024-12-18 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nss', models.CharField(max_length=15, unique=True)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('date_naissance', models.DateField()),
                ('adresse', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=20)),
                ('mutuelle', models.CharField(max_length=100)),
                ('personne_a_contacter', models.CharField(max_length=100)),
                ('telephone_a_contacter', models.CharField(max_length=20)),
                ('mot_de_passe', models.CharField(max_length=255)),
                ('medecin_traitant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendapp.staff')),
            ],
            options={
                'db_table': 'patient',
            },
        ),
    ]
