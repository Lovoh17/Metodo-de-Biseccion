# Generated by Django 5.0.6 on 2024-06-17 00:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = [
        migrations.AddField(
            model_name='biseccionhistory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
    ]

    operations = [
        migrations.CreateModel(
            name='membresias',
            fields=[
                ('id_membresia', models.AutoField(primary_key=True, serialize=False)),
                ('categoria_membresia', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equation', models.CharField(max_length=255)),
                ('x_value', models.FloatField()),
                ('h_value', models.FloatField()),
                ('forward_derivative', models.FloatField()),
                ('backward_derivative', models.FloatField()),
                ('central_derivative', models.FloatField()),
                ('forward_error', models.FloatField()),
                ('backward_error', models.FloatField()),
                ('central_error', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_User', models.CharField(max_length=200)),
                ('apellido_User', models.CharField(max_length=200)),
                ('correo_User', models.CharField(max_length=200)),
                ('password_User', models.CharField(max_length=200)),
                ('membresia_id_user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='myapp.membresias')),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id_Historial', models.AutoField(primary_key=True, serialize=False)),
                ('Procesos_Historial', models.TextField()),
                ('id_user_Historial', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='myapp.usuarios')),
            ],
        ),
    ]
