# Generated by Django 4.1.3 on 2022-11-15 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operatorview', '0002_department_reporter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vulnurability',
            name='Comment',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vulnurability',
            name='Exploit_code',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vulnurability',
            name='How_to_replicate',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vulnurability',
            name='Potential_fix',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='vulnurability',
            name='Video_link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
