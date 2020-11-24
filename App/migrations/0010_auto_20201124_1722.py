# Generated by Django 3.1.1 on 2020-11-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20201124_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintregister',
            name='complaint_type',
            field=models.CharField(choices=[('Credit Card Fraud', 'Credit Card Fraud'), ('Fraud', 'Fraud'), ('Harassment', 'Harassment'), ('Kidnapping', 'Kidnapping'), ('Money Laundering', 'Money Laundering'), ('Murder', 'Murder'), ('Public Intoxication', 'Public Intoxication'), ('Rape', 'Rape'), ('Robbery', 'Robbery'), ('Sexual Assault', 'Sexual Assault'), ('Shoplifting', 'Shoplifting'), ('Statutory Rape', 'Statutory Rape'), ('Theft', 'Theft'), ('Wire Fraud', 'Wire Fraud'), ('Insurance Fraud', 'Insurance Fraud'), ('Identity Theft', 'Identity Theft'), ('Perjury', 'Perjury')], max_length=100),
        ),
        migrations.AlterField(
            model_name='complaintregister',
            name='distict_place',
            field=models.CharField(choices=[('Agra', 'Agra'), ('Aligarh', 'Aligarh'), ('\tAllahabad', 'Allahabad'), ('Azamgarh', 'Azamgarh'), ('Chitrakoot', 'Chitrakoot'), ('Faizabad', 'Faizabad'), ('Gorakhpur', 'Gorakhpur'), ('Jhansi', 'Jhansi'), ('Kanpur ', 'Kanpur '), ('Lucknow', 'Lucknow'), ('Meerut', 'Meerut'), ('Mirzapur', 'Mirzapur'), ('Moradabad', 'Moradabad'), ('Varanasi', 'Varanasi'), ('Etawah', 'Etawah'), ('Ghaziabad\t', 'Ghaziabad\t'), ('Jaunpur', 'Jaunpur'), ('Kasganj', 'Kasganj'), ('Farrukhabad', 'Farrukhabad'), ('Shahdara', 'Shahdara'), ('\tCentral Delhi', 'Central Delhi'), ('New Delhi ', 'New Delhi '), ('South Delhi', 'South Delhi'), ('South West Delhi', 'South West Delhi'), ('Bareilly', 'Bareilly')], max_length=100),
        ),
        migrations.AlterField(
            model_name='complaintregister',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=100),
        ),
        migrations.AlterField(
            model_name='complaintregister',
            name='state',
            field=models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('\tBihar', '\tBihar'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Telangana', 'Telangana'), ('Tamil Nadu', 'Tamil Nadu'), ('Rajasthan', 'Rajasthan'), ('Odisha', 'Odisha'), ('Uttar Pradesh', 'Uttar Pradesh'), ('\tUttarakhand', '\tUttarakhand')], max_length=100),
        ),
        migrations.AlterField(
            model_name='missingperson',
            name='age',
            field=models.IntegerField(),
        ),
    ]