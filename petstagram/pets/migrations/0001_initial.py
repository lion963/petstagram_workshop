# Generated by Django 3.2 on 2021-06-08 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('cat', 'cat'), ('dog', 'dog'), ('parrot', 'parrot')], max_length=20)),
                ('name', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pets.pet')),
            ],
        ),
    ]