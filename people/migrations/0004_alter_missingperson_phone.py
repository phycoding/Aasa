# Generated by Django 4.0.4 on 2022-05-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_alter_missingperson_contact_person_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingperson',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Contact Number'),
        ),
    ]