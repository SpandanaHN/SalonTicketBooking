# Generated by Django 2.2.6 on 2020-05-20 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beauty.User_status'),
        ),
    ]
