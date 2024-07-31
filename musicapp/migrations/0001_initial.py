# Generated by Django 4.2.5 on 2024-07-16 09:38

from django.db import migrations, models
import musicapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('track_img', models.ImageField(upload_to=musicapp.models.get_upload_path)),
                ('track', models.FileField(upload_to=musicapp.models.get_upload_path)),
                ('downloads', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('times_played', models.IntegerField()),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
