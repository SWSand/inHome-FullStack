# Generated by Django 5.0.4 on 2024-04-11 21:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apartment_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_address', models.CharField(max_length=255)),
                ('current_landlord', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('pets', models.BooleanField(default=False)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_appartment', to='apartment_app.apartment')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
