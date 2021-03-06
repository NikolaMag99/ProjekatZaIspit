# Generated by Django 3.1.6 on 2021-02-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concerts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('artist', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.CharField(blank=True, max_length=250, null=True)),
                ('concertimageurl', models.CharField(blank=True, db_column='concertImageUrl', max_length=250, null=True)),
                ('createdat', models.DateTimeField(db_column='createdAt')),
                ('updatedat', models.DateTimeField(db_column='updatedAt')),
            ],
            options={
                'db_table': 'Concerts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('artist', models.CharField(blank=True, max_length=250, null=True)),
                ('genre', models.CharField(blank=True, max_length=250, null=True)),
                ('album', models.CharField(blank=True, max_length=250, null=True)),
                ('albumimageurl', models.CharField(blank=True, db_column='albumImageUrl', max_length=250, null=True)),
                ('youtubeid', models.CharField(blank=True, db_column='youtubeId', max_length=250, null=True)),
                ('lyrics', models.TextField(blank=True, null=True)),
                ('tab', models.TextField(blank=True, null=True)),
                ('createdat', models.DateTimeField(db_column='createdAt')),
                ('updatedat', models.DateTimeField(db_column='updatedAt')),
            ],
            options={
                'db_table': 'Songs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('password', models.CharField(blank=True, max_length=250, null=True)),
                ('createdat', models.DateTimeField(db_column='createdAt')),
                ('updatedat', models.DateTimeField(db_column='updatedAt')),
            ],
            options={
                'db_table': 'Users',
                'managed': False,
            },
        ),
    ]
