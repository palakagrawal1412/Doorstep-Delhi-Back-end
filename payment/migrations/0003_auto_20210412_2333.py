# Generated by Django 3.1.7 on 2021-04-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20210331_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='action_required_data',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='gateway_response',
            field=models.TextField(),
        ),
    ]