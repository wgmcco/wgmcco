# Generated by Django 3.0.5 on 2020-04-10 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permitprofile',
            name='pdf',
            field=models.FileField(blank=True, upload_to='permit_pdf', verbose_name='PDF'),
        ),
    ]
