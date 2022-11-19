# Generated by Django 4.1.3 on 2022-11-15 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operatorview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_name', models.CharField(max_length=200)),
                ('Department_email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(default='anonymous', max_length=100)),
                ('Last_name', models.CharField(default='anonymous', max_length=100)),
                ('Email_address', models.CharField(default='anonymous', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='vulnurability',
            name='Email_address',
        ),
        migrations.RemoveField(
            model_name='vulnurability',
            name='First_name',
        ),
        migrations.RemoveField(
            model_name='vulnurability',
            name='Last_name',
        ),
        migrations.AddField(
            model_name='vulnurability',
            name='Reported_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='public_user', to='operatorview.reporter'),
        ),
        migrations.AlterField(
            model_name='vulnurability',
            name='Assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Dept', to='operatorview.department'),
        ),
    ]
