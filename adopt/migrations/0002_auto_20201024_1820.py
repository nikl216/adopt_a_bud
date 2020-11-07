# Generated by Django 3.1.1 on 2020-10-24 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Age',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='District',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='HasGarder',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='Name',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='Occupation',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='PastPetExperience',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='Phone',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='State',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.TextField()),
                ('desc', models.TextField()),
                ('age', models.DecimalField(decimal_places=1, max_digits=2)),
                ('imageurl', models.URLField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]