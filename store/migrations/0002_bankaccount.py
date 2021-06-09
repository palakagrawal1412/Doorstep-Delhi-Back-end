# Generated by Django 3.1.7 on 2021-06-08 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder_name', models.CharField(max_length=128)),
                ('account_number', models.CharField(max_length=18)),
                ('ifsc', models.CharField(max_length=12)),
                ('account_type', models.CharField(choices=[('S', 'Savings'), ('C', 'Current')], max_length=1)),
                ('bank_name', models.CharField(max_length=128)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.store')),
            ],
        ),
    ]