# Generated by Django 4.1.10 on 2023-08-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_feedback_govuk', '0003_restructure_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basefeedback',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
