# Generated by Django 2.2.5 on 2019-10-20 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import skadmin.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(blank=True, max_length=55, null=True)),
                ('mobile', models.CharField(max_length=10, unique=True, validators=[skadmin.validators.validate_phone])),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('emails', models.EmailField(blank=True, max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]