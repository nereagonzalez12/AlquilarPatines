# Generated by Django 5.0.2 on 2024-02-08 13:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patinete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(unique=True)),
                ('tipo', models.CharField(max_length=50)),
                ('precio_desbloqueo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('precio_minuto', models.DecimalField(decimal_places=2, max_digits=12)),
                ('estado', models.CharField(max_length=50)),
                ('fecha_desbloqueo', models.DateField()),
                ('fecha_entrega', models.DateField()),
                ('coste_final', models.DecimalField(decimal_places=2, max_digits=12)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debito', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
