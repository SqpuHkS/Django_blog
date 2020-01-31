# Generated by Django 3.0.2 on 2020-01-31 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='site_blog.Tag'),
        ),
    ]
