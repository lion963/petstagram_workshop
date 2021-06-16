# Generated by Django 3.2 on 2021-06-16 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0004_alter_like_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('pet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
        ),
    ]